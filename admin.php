<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rasa app</title>

    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.min.js" integrity="sha512-v2CJ7UaYy4JwqLDIrZUI/4hqeoQieOmAZNXBeQyjo21dadnwR+8ZaIJVT8EE2iyI61OV8e6M8PP2/4hpQINQ/g==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <style>
        #chat-widget-button{
            right: inherit;
        }
    </style>
    <!-- <link rel="stylesheet" href="./assets/css/bot.css"> -->
</head>

<body>

    <div class="container">
        <button id="chat-widget-button" type="button" class="btn btn-primary rounded-circle chat-sign-button position-fixed" style="bottom: 20px; left: 0px">Admin</button>

        <div id="chat-widget" class="card position-fixed shadow d-none " style="bottom: 100px; left: 0px ;width: 400px;height: 500px;">
            <div class="card-header bg-primary text-white">
                <h6 id="title-chatbot">CTUMP</h6>
                <button id="chat-widget-close-button" type="button" class="btn btn-light">X</button>
            </div>

            <div id="chat-widget-messages" class="card-body">
                <!-- chat here -->
            </div>
            <div class="card-footer" style="display: flex;">
                <input type="text" class="form-control" id="chat-widget-input" placeholder="Type your message..." style="flex: 1;">
                <!-- Thêm nút gửi -->
                <button id="send-message-button" type="button" class="btn btn-primary" style="margin-left: 10px;">Send</button>
            </div>
            <div id="myModal" class="modal">
                <span class="close" onclick="document.getElementById('myModal').style.display='none'">&times;</span>
                <img class="modal-content" id="img01">
            </div>
        </div>
    </div>

    <script>
    $(document).ready(function() {
        let welcomeMessageShown = false; // Variable to check if the welcome message has been displayed

        // Toggle chat widget visibility
        $("#chat-widget-button").on("click", function() {
            $("#chat-widget").toggleClass("d-none");
            if (!welcomeMessageShown) { // Check if the welcome message has not been displayed
                $("#chat-widget-messages").append(`
                    <div style='background-color: #ccc; padding: 10px; border-radius: 12px; margin-bottom: 10px; color: black;'>
                        <strong>CTUMP:</strong> Xin chào, tôi có thể giúp bạn tìm kiếm thông tin về:
                        <br> - Thông tin trường này
                        <br> - Các ngành đào tạo
                        <br> - Chương trình đào tạo mỗi ngành
                        <br> - Thông tin các khoa, phòng ban (địa điểm, email, số điện thoại)
                        <br> - Thông tin học phí theo năm
                        <br> - Cấp lại thẻ sinh viên, email, bảo hiểm tai nạn, tài khoản quản lý đào tạo
                        <br> - Các ngành đào tạo sau đại học
                        <br> - Quy trình tuyển sinh
                        <br> - Thông tin học bổng
                    </div>
                `);
                welcomeMessageShown = true; // Mark the welcome message as displayed
                scrollChatToBottom(); // Automatically scroll to the bottom
            }
            scrollChatToBottom(); // Automatically scroll to the bottom
        });

        // Close chat widget
        $("#chat-widget-close-button").on("click", function() {
            $("#chat-widget").addClass("d-none");
        });

        // Send message on pressing Enter
        $("#chat-widget-input").keypress(function(event) {
            if (event.which === 13) {
                sendMessage(); // Send message on Enter key press
            }
        });

        // Send message on clicking the send button
        $("#send-message-button").on("click", function() {
            sendMessage();
        });

        // Function to send a message
        function sendMessage() {
            let userMessage = $("#chat-widget-input").val();
            $("#chat-widget-input").val(""); // Clear the input field

            $("#chat-widget-messages").append(`
                <div style='background-color: #4291e6; padding: 10px; border-radius: 12px; margin-bottom: 10px; color: white;'>
                    <strong>Bạn:</strong> ${userMessage}
                </div>
            `);
            console.log(userMessage);

            $.ajax({
                type: "GET",
                url: "/api/get_mess_user", // URL to the PHP handler
                contentType: "application/json",
                data: JSON.stringify({ message: userMessage }),
                success: function(res) {
                    console.log(res);
                    try {
                        let responses = JSON.parse(res);
                        responses.forEach(function(response) {
                            if (/\.(png|jpg|jpeg|gif)$/i.test(response)) {
                                var img = `<img class="myImg" style="width:100%;max-width:300px" src="${response}" alt="Image" />`;
                                $("#chat-widget-messages").append(`
                                    <div><strong class='text-danger'>Bot:</strong> ${img}</div>
                                `);
                                // Click to display image modal
                                $("#chat-widget-messages .myImg").last().on("click", function() {
                                    displayImageModal(this.src);
                                });
                            } else if (containsURL(response)) {
                                response = response.replace(/\b(http[s]?:\/\/\S+)/gi, "<a href='$1' target='_blank'>$1</a>");
                                $("#chat-widget-messages").append(`
                                    <div style='background-color: #ccc; padding: 10px; border-radius: 12px; margin-bottom: 10px; color: black;'>
                                        <strong>CTUMP:</strong> ${response}
                                    </div>
                                `);
                            } else {
                                $("#chat-widget-messages").append(`
                                    <div style='background-color: #ccc; padding: 10px; border-radius: 12px; margin-bottom: 10px; color: black;'>
                                        <strong>CTUMP:</strong> ${response}
                                    </div>
                                `);
                            }
                        });
                        scrollChatToBottom(); // Automatically scroll to the bottom
                    } catch (e) {
                        console.log("Invalid JSON response from server");
                        displayErrorMessage("Server hiện đang cập nhât, liên hệ admin để nhận hỗ trợ !");
                    }
                },
                error: function(error) {
                    console.log('Error: ', error);
                    displayErrorMessage("Đã xảy ra lỗi kết nối server: Failed to connect to localhost port 5005 after 2260 ms: Connection refused");
                }
            });
            scrollChatToBottom(); // Automatically scroll to the bottom
        }

        // Function to check if a string contains a URL
        function containsURL(str) {
            var urlPattern = /\b(http[s]?:\/\/\S+)/gi;
            return urlPattern.test(str);
        }

        // Function to display an image modal
        function displayImageModal(src) {
            document.getElementById('img01').src = src;
            document.getElementById('myModal').style.display = "block";
        }

        // Function to automatically scroll to the bottom of the chat
        function scrollChatToBottom() {
            var chatMessages = document.getElementById('chat-widget-messages');
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }

        // Function to display error messages in the chat
        function displayErrorMessage(message) {
            $("#chat-widget-messages").append(`
                <div style='background-color: #f8d7da; padding: 10px; border-radius: 12px; margin-bottom: 10px; color: black;'>
                    <strong>CTUMP:</strong> ${message}
                </div>
            `);
            scrollChatToBottom(); // Automatically scroll to the bottom
        }
    });
</script>




</body>

</html>