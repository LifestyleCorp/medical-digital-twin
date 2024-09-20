// backend/nodejs_backend/server.js

const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const winston = require('winston');

const app = express();
const server = http.createServer(app);
const io = socketIo(server, {
  cors: {
    origin: "http://localhost:3000",
    methods: ["GET", "POST"]
  }
});

// Setup Winston logger
const logger = winston.createLogger({
  level: 'info',
  format: winston.format.json(),
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({ filename: 'combined.log' })
  ],
});

io.on('connection', (socket) => {
  logger.info('New client connected');

  socket.on('disconnect', () => {
    logger.info('Client disconnected');
  });

  socket.on('sendData', (data) => {
    logger.info('Received data:', data);
    socket.broadcast.emit('receiveData', data);
  });
});

const PORT = process.env.PORT || 4000;
server.listen(PORT, () => logger.info(`Node.js server running on port ${PORT}`));
