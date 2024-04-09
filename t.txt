$(document).ready(function () {
    $('#chat-widget-button').on("click", function () {
        $("#chat-widget").toggleClass("d-none");
        if (!$("#chat-widget").hasClass("d-none")) {
            scrollChatToBottom();
        }
    });

    $("#chat-widget-close-button").on("click", function () {
        $("#chat-widget").addClass("d-none");
    });

    $("#chat-widget-input").keypress(function (event) {
        if (event.which == 13) {
            let userMessage = $("#chat-widget-input").val();
            $("#chat-widget-input").val("");

            $("#chat-widget-messages").append("<div><strong>You: </strong>" + userMessage +"</div>");
            scrollChatToBottom();
            data_send = {
                'message': userMessage
            }
            $.ajax({
                type: "POST",
                url: "/webhook",
                contentType: "application/json",
                data: JSON.stringify({
                    message: userMessage
                }),
                success: function (res) {
                    console.log(res);
                    if (res.endsWith(".jpg") || res.endsWith(".png")) {
                        var img ='<img class="myImg" style="width:100%;max-width:300px" src="' +res+'" alt="Image" />';
                        $("#chat-widget-messages").append("<div ><strong class='text-danger'>Bot:</strong> " + img + "</div>");

                        // click de hien thi modal hinh anh
                        $("#chat-widget-messages .myImg").last().on("click", function() {
                            displayImageModal(this.src);
                        });

                    } else if (res && res.startsWith("https")) {
                        var link = '<a class="text-info" href="' + res + '" target="_blank">' + res + '</a>';
                        $("#chat-widget-messages").append("<div><strong class='text-danger'>Bot:</strong> " + link + "</div>");
                    } else {
                        $("#chat-widget-messages").append("<div><strong class='text-danger'>Bot:</strong> " + res + "</div>");
                    }
                    scrollChatToBottom();
                },
                error: function (error) {
                    console.log('lỗi ');
                }
            });
        }
    });

    function scrollChatToBottom() {
        var chatWidget = document.getElementById("chat-widget-messages");
        chatWidget.scrollTop = chatWidget.scrollHeight;
    }
    function isUserAtBottom() {
        var chatWidget = document.getElementById("chat-widget-messages");
        return chatWidget.scrollHeight - chatWidget.clientHeight <= chatWidget.scrollTop + 1;
    }
    document.getElementById("chat-widget-messages").addEventListener("scroll", function () {
        if (isUserAtBottom()) {
            window.scrollTo(0, document.body.scrollHeight);
        }
    });
});