import express from 'express';
import Redic from 'redic';
import kue from 'kue';
import { promisify } from 'util';

const app = express();
const client = new Redic();
const queue = kue.createQueue();

const promisifiedGet = promisify(client.get).bind(client);
const promisifiedSet = promisify(client.set).bind(client);

// Set the initial number of available seats to 50
promisifiedSet('available_seats', 50);

// Initialize reservationEnabled to true
let reservationEnabled = true;

// Function to reserve a seat
const reserveSeat = async (number) => {
  await promisifiedSet('available_seats', number);
};

// Function to get the current number of available seats
const getCurrentAvailableSeats = async () => {
  const numberOfAvailableSeats = await promisifiedGet('available_seats');
  return parseInt(numberOfAvailableSeats, 10);
};

// Express route to get the number of available seats
app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: numberOfAvailableSeats.toString() });
});

// Express route to reserve a seat
app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    }

    return res.json({ status: 'Reservation in process' });
  });

  // Event handler for a successfully completed job
  job.on('complete', (result) => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  // Event handler for a failed job
  job.on('failed', (err) => {
    console.error(`Seat reservation job ${job.id} failed: ${err}`);
  });
});

// Express route to process the queue
app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  // Process the queue
  queue.process('reserve_seat', async (job, done) => {
    const currentAvailableSeats = await getCurrentAvailableSeats();

    if (currentAvailableSeats === 0) {
      reservationEnabled = false;
    }

    if (currentAvailableSeats >= 0) {
      // Update the number of available seats
      await reserveSeat(currentAvailableSeats - 1);
      done();
    } else {
      // Fail the job if not enough seats available
      done(new Error('Not enough seats available'));
    }
  });
});

const PORT = 1245;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
