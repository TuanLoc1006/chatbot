const socket = io();

////////////Khởi tạo adminID
const adminID = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-';
socket.emit('adminID', adminID);
// console.log('ADMIN ID LA '+adminID)




//nhận tin nhắn realtime từ người dùng
socket.on('server_send_to_admin', (msg) => {

    //tin nhắn được gửi tới
    console.log(msg)

    ////////////////HIỂN THỊ BÊN LIST
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
                    <span>${msg.senderName}</span>
                    <p style="font-size: 16px;">${msg.message}</p>
                </div>
                <div class="status-dot '. $offline .'"><i class="fas fa-circle"></i></div>
                </a>
            </div>`;
    } else {
        //người dùng đã có giao diện, chỉ thay đổi lại
        sender_div.querySelector('p').innerHTML = msg.message;
    }

    ///////////////HIỂN THỊ TIN NHẮN TRONG Ô CHAT
    const window_chat = document.getElementsByClassName(`mess-padding-${msg.senderID}`)[0]
    if(window_chat) {
        const newDiv = document.createElement('div')
        newDiv.innerHTML += `
        <div class="mess-user-${msg.senderID}">
            <div class="d-flex justify-content-between">
                <p class="small mb-1">${msg.senderName}</p>
                <p class="small mb-1 text-muted">${msg.timestamp}</p>
            </div>
            <div class="d-flex flex-row justify-content-start">
                <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava5-bg.webp" alt="avatar 1" style="width: 45px; height: 100%;">
                <div>
                    <p class="small p-2 ms-3 mb-3 rounded-3" style="background-color: #f5f6f7;">${msg.message}</p>
                </div>
            </div>
        </div>
        `
        window_chat.appendChild(newDiv)
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
                <p style="font-size: 16px; margin-bottom:0">${user.lastMessage}</p>
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
    var right = 380;
    var iii = 0;
    for (iii; iii < total_popups; iii++) {
        if (popups[iii] != undefined) {
            var element = document.getElementById(popups[iii]);
            element.style.right = right + "px";
            right = right + 400;
            element.style.display = "flex";
            element.style.flexDirection = "column";
            element.style.justifyContent = "space-between";
        }
    }

    for (var jjj = iii; jjj < popups.length; jjj++) {
        var element = document.getElementById(popups[jjj]);
        element.style.display = "none";
    }
}

////////////////////////////////////////////////////////////////////////////////////////////////

async function callAPIGetMessage(userid){
    try {
        const response = $.ajax({
            type: 'GET',
            dataType: 'json', 
            url: '/api/get_mess_user',
            data: {userid : userid},
        });
        console.log('CALL API THÀNH CÔNG')
        return response;
    } catch(err){
        console.log(err);
        return null;
    }
}


// Hàm hiển thị popup tin nhắn
async function register_popup(userid, username) {
    //hiển thị ID của popup
    // console.log(`ID popup la ${userid}`)

    // Kiểm tra nếu popup đã tồn tại trong mảng
    const existingIndex = popups.indexOf(userid);
    if (existingIndex !== -1) {
        
        popups.splice(existingIndex, 1);
        popups.unshift(userid);
        calculate_popups();
        return;
    }

    // tạo thẻ div chứa tin nhắn của từng user
    const popupBox = document.createElement('div');
    popupBox.classList.add('popup-box');
    popupBox.id = userid;
    var messageHTML = '';
    //gọi hàm lấy tất cả message của người dùng theo userid
    const userListMessage = await callAPIGetMessage(userid)
    // console.log(userListMessage);
    userListMessage.forEach(userMessage=>{
        
        messageHTML +=`
            <div class="mess-user-${userMessage.senderID}">
                <div class="d-flex justify-content-between">
                    <p class="small mb-1">${userMessage.senderName}</p>
                    <p class="small mb-1 text-muted">${userMessage.timestamp}</p>
                </div>
                <div class="d-flex flex-row justify-content-start">
                    <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava5-bg.webp" alt="avatar 1" style="width: 45px; height: 100%;">
                    <div>
                        <p class="small p-2 ms-3 mb-3 rounded-3" style="background-color: #f5f6f7;">${userMessage.message}</p>
                    </div>
                </div>
            </div>
        `
    })


    popupBox.innerHTML = `
    <div class="popup-head">
        <div class="popup-head-left">${username}</div>
        <div class="popup-head-right"><a href="javascript:close_popup('${userid}');">&#10005;</a></div>
        <div style="clear: both"></div>
    </div>
     
    <div class="popup-messages">
        <div class="mess-padding-${userid}" style="padding:14px">

            <!-- người khác gửi đến -->
            ${messageHTML}

            <!-- của người chat -->
            <div class="mess-admin">
                <div class="d-flex justify-content-between">
                    <p class="small mb-1 text-muted">23 Jan 2:05 pm</p>
                    <p class="small mb-1">Johny Bullock</p>
                </div>
                <div class="d-flex flex-row justify-content-end mb-4 pt-1">
                <div>
                    <p class="small p-2 me-3 mb-3 text-white rounded-3 bg-warning">Thank you for your believe in our supports</p>
                </div>
                <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava6-bg.webp" alt="avatar 1" style="width: 45px; height: 100%;">
                </div>
            </div>


        </div>
    </div>

    <div class="popup-bottom">
        <div class="input-group">
            <input idOfUser="${userid}" type="text" class="form-control input-mess">
            <span class="input-group-text"><i class="fa-solid fa-paper-plane"></i></span> 
        </div>
    </div>
    `;

    // thêm phần tử mới vào body
    document.body.appendChild(popupBox);

    popups.unshift(userid);
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

