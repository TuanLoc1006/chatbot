const socket = io();

////////////Khởi tạo adminID
const adminID = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-';
socket.emit('adminID', adminID);
// console.log('ADMIN ID LA '+adminID)

//nhận tin nhắn realtime từ người dùng
//hiển thị chat người dùng gửi đến
socket.on('server_send_to_admin', (msg) => {
    
    console.log(msg)

    //tạo div chứa tin nhắn
    const messContainer = document.createElement('div');
    const userList = document.querySelector('.users-list')
    userList.innerHTML += `<a href="#">
    <div class="content">
    <img src="https://t4.ftcdn.net/jpg/02/29/75/83/360_F_229758328_7x8jwCwjtBMmC6rgFzLFhZoEpLobB6L8.jpg" alt="">
    <div class="details">
        <span>${msg.senderName}</span>
        <p>${msg.message}</p>
    </div>
    </div>
    <div class="status-dot '. $offline .'"><i class="fas fa-circle"></i></div>
</a>`
})


/////////////CALL API LẤY DANH SÁCH NGƯỜI DÙNG
document.addEventListener('DOMContentLoaded', async function (e) {
    const response = await fetch('/api/get_user');
    const users = await response.json();
    const userList = document.querySelector('.users-list')
    users.forEach(user => {
        userList.innerHTML += `<a href="#">
        <div class="content">
        <img src="https://t4.ftcdn.net/jpg/02/29/75/83/360_F_229758328_7x8jwCwjtBMmC6rgFzLFhZoEpLobB6L8.jpg" alt="">
        <div class="details">
            <span>${user.userName}</span>
            <p>${user.lastMessage}</p>
        </div>
        </div>
        <div class="status-dot '. $offline .'"><i class="fas fa-circle"></i></div>
    </a>`
    })
});


