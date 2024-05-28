const express = require('express');
const {Server} = require('socket.io');
// const { join }= require('node:path');
const { createServer } = require('node:http');
const mongoose = require('mongoose');

const app = express();
const server = createServer(app)
const io = new Server(server, {
    connectionStateRecovery: {}
});

app.use(express.static(__dirname));

const Message = require('./model/message');
const User = require('./model/user')

// const connectDB = async () => {
//     try {
//         await mongoose.connect('mongodb://localhost:27017/chat');
//         console.log('Kết nối MongoDB thành công');
//     } catch (err) {
//         console.error('Lỗi khi kết nối cơ sở dữ liệu:', err);
//     }
// };
// connectDB();

const connectDB = async () => {
    try {
        await mongoose.connect('mongodb://127.0.0.1:27017/chat');
        console.log('Kết nối MongoDB thành công');
    } catch (err) {
        console.error('Lỗi khi kết nối cơ sở dữ liệu:', err);
    }
};
connectDB();
// function generateRandomString(length) {
//     const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
//     let result = '';
//     const charactersLength = characters.length;
//     for (let i = 0; i < length; i++) {
//         result += characters.charAt(Math.floor(Math.random() * charactersLength));
//     }
//     return result;
// }
// const adminID = generateRandomString(100);

app.get('/', (req, res) => {
    res.sendFile(__dirname+'/view/user.html');
});

app.get('/admin-chat', (req, res) => {
    res.sendFile(__dirname+'/view/admin_chat.html');
})

//API lấy user
app.get('/api/get_user', async (req, res) => {
    //lấy người dùng gửi về admin
    const user_data = await User.find()
    res.status(200).send(user_data)
})

io.on('connection', (socket) => {

    /////////////////////CLIENT

    //lấy tin nhắn của user từ database
    socket.on('getUserMessages', async (data) => {
        
        const uID = data.saveUID;

        const messages = await Message.find({senderID: uID})

        //gửi tin nhắn từ database cho user 
        socket.emit(uID, (messages));

    });

    //nhận tin nhắn trực tiếp từ người dùng
    socket.on('send_to_server', async (msg) => {
        const vietnamTime = new Date(new Date().getTime() + 7 * 60 * 60 * 1000).toISOString();

        var data = {
            'senderID': msg.uID,
            'senderName': msg.uName,
            'receiverID': 'ADMIN',
            'message': msg.message,
            'timestamp': vietnamTime
        }

        //thêm người dùng
        
        try {
            //kiểm tra người dùng tồn tại
            const getUser = await User.findOne({userID:msg.uID})
            if(!getUser){
                var user = {
                    'userID': msg.uID,
                    'userName': msg.uName,
                    'lastMessage': msg.message,
                    'status': 'on',
                }
                const userModel = new User(user)
                await userModel.save()
                console.log('Thêm người dùng thành công')
            } else {
                //cập nhật tin nhắn cuối
                await User.findOneAndUpdate(
                    {userID: msg.uID},
                    { $set:{lastMessage : msg.message} }
                )
            }
        } catch(err){
            console.log('Lỗi khi thêm user', err)
        }

        //gửi lại đoạn chat client vừa nhập
        socket.emit('server_send_to_client', msg.message);

        //gửi đoạn chat người dùng đến admin
        io.emit('server_send_to_admin', data);

        // lưu vào db
        const newMessage = new Message(data);
        try {
            await newMessage.save();
            console.log('Đã thêm tin nhắn');
        } catch (err) {
            console.log('Lỗi khi thêm dữ liệu: ', err);
        }

        
    });
    ////////////////////////// ADMIN
});

server.listen(3000, () => {
    console.log('Server running at http://localhost:3000');
});