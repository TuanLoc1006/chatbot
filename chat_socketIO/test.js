// WARNING: the client will NOT be able to connect!

const {Server} = require('socket.io');
// const { join }= require('node:path')
// const socket = io("ws://echo.websocket.org");

socket.emit("hello", "world", (response) => {
    console.log(response); // "got it"
  });