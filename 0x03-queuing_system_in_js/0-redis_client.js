import redis from 'redis';
const redisClient = redis.createClient();

(async () => {
  await redisClient.connect();
})();

redisClient.on('ready', () => {
  console.log('Redis client connected to the server');
});

redisClient.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});
