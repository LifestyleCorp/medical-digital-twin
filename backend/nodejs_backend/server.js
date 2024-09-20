// backend/nodejs_backend/server.js

const express = require('express');
const http = require('http');
const socketIo = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = socketIo(server, {
  cors: {
    origin: "http://localhost:3000",
    methods: ["GET", "POST"]
  }
});

io.on('connection', (socket) => {
  console.log('New client connected');

  socket.on('disconnect', () => {
    console.log('Client disconnected');
  });

  // Example event
  socket.on('sendData', (data) => {
    console.log('Received data:', data);
    // Emit to other clients or process data
    socket.broadcast.emit('receiveData', data);
  });
});

const PORT = process.env.PORT || 4000;
server.listen(PORT, () => console.log(`Node.js server running on port ${PORT}`));
