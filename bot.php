<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rasa app</title>

    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.min.js" integrity="sha512-v2CJ7UaYy4JwqLDIrZUI/4hqeoQieOmAZNXBeQyjo21dadnwR+8ZaIJVT8EE2iyI61OV8e6M8PP2/4hpQINQ/g==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>

    <link rel="stylesheet" href="./assets/css/bot.css">
</head>

<body>

    <div class="container">
        <button id="chat-widget-button" type="button" class="btn btn-primary rounded-circle chat-sign-button position-fixed" style="bottom: 20px; right: 20px;">💬</button>

        <div id="chat-widget" class="card position-fixed shadow d-none" style="bottom: 100px; right:20px ; width: 300px;">

            <div class="card-header bg-primary text-white">
                ChatBot
                <button id="chat-widget-close-button" type="button" class=" btn btn-light">X</button>
            </div>

            <div id="chat-widget-messages" class="card-body">
                <!-- chat here -->
            </div>
            <div class="card-footer">
                <input type="text" class="form-control" id="chat-widget-input" placeholder="Type your message...">
            </div>
            <div id="myModal" class="modal">
                <span class="close" onclick="document.getElementById('myModal').style.display='none'">&times;</span>
                <img class="modal-content" id="img01">
            </div>
        </div>
    </div>

    <script>
        $(document).ready(function() {
            $("#chat-widget-button").on("click", function() {
                $("#chat-widget").toggleClass("d-none");
                scrollChatToBottom(); // Khi mở chat widget, tự động cuộn xuống dưới cùng
            });

            $("#chat-widget-close-button").on("click", function() {
                $("#chat-widget").addClass("d-none");
            });

            $("#chat-widget-input").keypress(function(event) {
                if (event.which === 13) {
                    let userMessage = $("#chat-widget-input").val();
                    $("#chat-widget-input").val("");

                    $("#chat-widget-messages").append("<div><strong>Bạn:</strong> " + userMessage + "</div>");
                    console.log(userMessage);
                    $.ajax({
                        type: "POST",
                        url: "chat_handler.php", // Đường dẫn tới tệp PHP xử lý yêu cầu
                        contentType: "application/json",
                        data: JSON.stringify({
                            message: userMessage
                        }),
                        success: function(res) {
                            console.log(res);
                            try {
                                let responses = JSON.parse(res);
                                responses.forEach(function(response) {
                                    // Kiểm tra nếu response là một đường dẫn hình ảnh
                                    if (/\.(png|jpg|jpeg|gif)$/i.test(response)) {
                                        var img = '<img class="myImg" style="width:100%;max-width:300px" src="' + response + '" alt="Image" />';
                                        $("#chat-widget-messages").append("<div><strong class='text-danger'>Bot:</strong> " + img + "</div>");
                                        // click để hiển thị modal hình ảnh
                                        $("#chat-widget-messages .myImg").last().on("click", function() {
                                            displayImageModal(this.src);
                                        });
                                    }
                                    // Kiểm tra nếu response có chứa các URL
                                    else if (containsURL(response)) {
                                        // Chuyển các URL thành liên kết
                                        response = response.replace(/\b(http[s]?:\/\/\S+)/gi, "<a href='$1' target='_blank'>$1</a>");
                                        $("#chat-widget-messages").append("<div><strong>CTUMP:</strong> " + response + "</div>");
                                    } else {
                                        $("#chat-widget-messages").append("<div><strong>CTUMP:</strong> " + response + "</div>");
                                    }
                                });
                                scrollChatToBottom(); // Sau khi thêm tin nhắn mới, tự động cuộn xuống dưới cùng
                            } catch (e) {
                                console.log("Invalid JSON response from server");
                            }
                        },
                        error: function(error) {
                            console.log('Error: ', error);
                        }
                    });
                }
                scrollChatToBottom();
            });
        });

        // Hàm kiểm tra xem một chuỗi có chứa URL hay không
        function containsURL(str) {
            var urlPattern = /\b(http[s]?:\/\/\S+)/gi;
            return urlPattern.test(str);
        }

        function displayImageModal(src) {
            document.getElementById('img01').src = src;
            document.getElementById('myModal').style.display = "block";
        }

        // Hàm tự động cuộn xuống dưới cùng của khung chat
        function scrollChatToBottom() {
            var chatMessages = document.getElementById('chat-widget-messages');
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }
    </script>

</body>

</html>
