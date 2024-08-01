 import redis from 'redis';

// create a redis client
const client = redis.createClient();

// Handler for sucessful connection
client.on('connect', () => {
	console.log("Redis client connected to the server");
});

// Handler for comnection error
client.on('error', (err) => {
	console.log(`Redis client not connected to the server: ${err}`);
});

