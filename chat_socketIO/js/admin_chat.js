const socket = io();

////////////Khởi tạo adminID
const adminID = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-';
socket.emit('adminID', adminID);
// console.log('ADMIN ID LA '+adminID)

//nhận tin nhắn realtime từ người dùng
socket.on('server_send_to_admin', (msg) => {

    //tin nhắn được gửi tới
    console.log(msg)

    const sender_div = document.querySelector(`[data-user-id="${msg.senderID}"]`);

    //kiểm tra Id của người dùng có trên giao diện hay chưa
    if(!sender_div) {
        //hiển thị tin nhắn lên giao diện list user
        const userList = document.querySelector('.userList');
        userList.innerHTML +=
            `<div data-user-id="${msg.senderID}" class="sidebar-name">
                <a href="javascript:register_popup('${msg.senderID}', '${msg.senderName}');">
                    <img width="30" height="30" src="https://t4.ftcdn.net/jpg/02/29/75/83/360_F_229758328_7x8jwCwjtBMmC6rgFzLFhZoEpLobB6L8.jpg" />
                <div class="chatContent">
                    <span'>${msg.senderName}</span>
                    <p style="font-size: 16px;">${msg.message}</p>
                </div>
                <div class="status-dot '. $offline .'"><i class="fas fa-circle"></i></div>
                </a>
            </div>`;
    } else {
        //người dùng đã có giao diện, chỉ thay đổi lại
        sender_div.querySelector('p').innerHTML = msg.message;
    }
})

// /////////////CALL API LẤY DANH SÁCH NGƯỜI DÙNG
document.addEventListener('DOMContentLoaded', async function (e) {
    const response = await fetch('/api/get_user');
    const users = await response.json();
    const userList = document.querySelector('.userList');
    users.forEach(user => {
        userList.innerHTML +=
        `<div data-user-id="${user.userID}" class="sidebar-name">
            <a href="javascript:register_popup('${user.userID}', '${user.userName}');">
                <img width="30" height="30" src="https://t4.ftcdn.net/jpg/02/29/75/83/360_F_229758328_7x8jwCwjtBMmC6rgFzLFhZoEpLobB6L8.jpg" />
            <div class="chatContent">
                <span>${user.userName}</span>
                <p style="font-size: 16px;">${user.lastMessage}</p>
            </div>
            <div class="status-dot '. $offline .'"><i class="fas fa-circle"></i></div>
            </a>
        </div>`
    })
});



//////////// START SCRIPT POPUP CHAT

//this function can remove a array element.
Array.remove = function (array, from, to) {
    var rest = array.slice((to || from) + 1 || array.length);
    array.length = from < 0 ? array.length + from : from;
    return array.push.apply(array, rest);
};

//this variable represents the total number of popups can be displayed according to the viewport width
var total_popups = 0;

//arrays of popups ids
var popups = [];

//this is used to close a popup
function close_popup(id) {
    for (var iii = 0; iii < popups.length; iii++) {
        if (id == popups[iii]) {
            Array.remove(popups, iii);
            document.getElementById(id).style.display = "none";
            calculate_popups();
            return;
        }
    }
}

//displays the popups. Displays based on the maximum number of popups that can be displayed on the current viewport width
function display_popups() {
    var right = 500;
    var iii = 0;
    for (iii; iii < total_popups; iii++) {
        if (popups[iii] != undefined) {
            var element = document.getElementById(popups[iii]);
            element.style.right = right + "px";
            right = right + 320;
            element.style.display = "block";
        }
    }

    for (var jjj = iii; jjj < popups.length; jjj++) {
        var element = document.getElementById(popups[jjj]);
        element.style.display = "none";
    }
}

//creates markup for a new popup. Adds the id to popups array.
// Tạo mã HTML cho một popup mới và thêm id vào mảng popups.
function register_popup(id, name) {
    console.log('List la ' + popups);
    
    // Kiểm tra nếu popup đã tồn tại trong mảng
    const existingIndex = popups.indexOf(id);
    if (existingIndex !== -1) {
        // Đã đăng ký, đưa nó lên đầu
        popups.splice(existingIndex, 1);
        popups.unshift(id);
        calculate_popups();
        return;
    }

    // tạo phần tử popup mới
    const popupBox = document.createElement('div');
    popupBox.classList.add('popup-box', 'chat-popup');
    popupBox.id = id;
    popupBox.innerHTML = `
        <div class="popup-head">
            <div class="popup-head-left">${name}</div>
            <div class="popup-head-right"><a href="javascript:close_popup('${id}');">&#10005;</a></div>
            <div style="clear: both"></div>
        </div>

        <div class="popup-messages">messages..</div>
        <div class="popup-type">
            <input type="text">
            <input type="submit">
        </div>
        <div class="popup-bottom"></div>
    `;

    // thêm phần tử mới vào body
    document.body.appendChild(popupBox);
    
    // thêm id vào đầu mảng popups và tính toán lại các popup hiển thị
    popups.unshift(id);
    calculate_popups();
}


//calculate the total number of popups suitable and then populate the toatal_popups variable.
function calculate_popups() {
    var width = window.innerWidth;
    if (width < 540) {
        total_popups = 0;
    } else {
        width = width - 200;
        //320 is width of a single popup box
        total_popups = parseInt(width / 320);
    }
    display_popups();

}

//recalculate when window is loaded and also when window is resized.
window.addEventListener("resize", calculate_popups);
window.addEventListener("load", calculate_popups);

//////////// END SCRIPT POPUP CHAT