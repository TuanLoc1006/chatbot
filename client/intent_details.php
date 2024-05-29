<?php
include "../includes/db_con.php";

// Kiểm tra xem có tham số intent_id được truyền qua URL không
if (isset($_GET['intent_id'])) {
    $intent_id = $_GET['intent_id'];

    // Truy vấn cơ sở dữ liệu để lấy thông tin chi tiết về ý định
    $sql_intent_details = "SELECT `intent_id`, `intent_name`, `status_file` FROM `intents` WHERE `intent_id` = $intent_id";
    $result = $conn->query($sql_intent_details);

    if ($result && $result->num_rows > 0) {
        $row = $result->fetch_assoc();
        ?>
        <!DOCTYPE html>
        <html lang="en">

        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Intent Details</title>

            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css"
                integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

        </head>

        <body>
            <!-- <h3><a href="../admin/views/home.php">Trang admin</a></h3> -->
            <h3><a href="../index.php">Trang user</a></h3>
            <div class="container">
                <div class="row">
                    <div class="col-md-6">
                        <h2>Thông tin chi tiết chủ đề</h2>
                        <!-- <p><strong>Intent Name:</strong> <?php echo $row['intent_name']; ?> </p> -->

                        <div class="question-list">
                            <h2>Các mẫu câu hỏi về cùng 1 chủ đề:</h2>
                            <p>Ví dụ: xin chào, chào bạn, hello, hi, bonjour, nice to meet you</p>
                            <?php
                            $sql_ex_intents = "SELECT `id`, `intent_id`, `example_question`, `status_file` FROM `example_intent` WHERE `intent_id`='$intent_id' ";
                            $result_example_intent = $conn->query($sql_ex_intents);
                            while ($row = $result_example_intent->fetch_assoc()) {
                                $display = ($row['status_file'] == 1) ? 'style="display: none;"' : ''; // Kiểm tra giá trị của status_file
                                echo '<div class="item"><textarea rows="2" cols="70" class="example-question" data-id="' . $row['id'] . '">' . $row['example_question'] . '</textarea> <button class="btn-edit-example btn-primary btn" data-id="' . $row['id'] . '" ' . $display . '>Lưu thay đổi</button> <button class="btn-delete-example btn btn-danger" data-id="' . $row['id'] . '" ' . $display . '>Xóa</button></div>';
                            }
                            ?>
                        </div>

                        <div class="answer-list">
                            <h2>Các mẫu câu trả lời:</h2>
                            <?php
                            $sql_chat_answer = "SELECT `id`, `intent_id`, `chat_answer`, `status_file` FROM `answer_intent` WHERE `intent_id`='$intent_id'";
                            $result_chat_answer = $conn->query($sql_chat_answer);
                            while ($row = $result_chat_answer->fetch_assoc()) {
                                $display = ($row['status_file'] == 1) ? 'style="display: none;"' : ''; // Kiểm tra giá trị của status_file
                                echo '<div class="item"><textarea rows="2" cols="70" class="chat-answer" data-id="' . $row['id'] . '">' . $row['chat_answer'] . '</textarea> <button class="btn-edit-answer btn-primary btn" data-id="' . $row['id'] . '" ' . $display . '>Lưu thay đổi</button> <button class="btn-delete-answer btn btn-danger" data-id="' . $row['id'] . '" ' . $display . '>Xóa</button></div>';
                            }
                            ?>
                        </div>


                    </div>
                    <div class="col-md-6">
                        <h3>Tạo câu hỏi tương tự</h3>
                        <?php
                        $intent_id = $_GET['intent_id'];
                        $sql_intent_details = "SELECT * FROM `intents` WHERE `intent_id` = $intent_id";
                        $result = $conn->query($sql_intent_details);
                        if ($result && $result->num_rows > 0) {
                            $row = $result->fetch_assoc();
                            $intent_name = $row['intent_name'];
                        }
                        ?>
                        <form method="post" action="./save_data.php">
                            <div class="form-group">
                                <label for="intentName">Id chủ đề:</label>
                                <input class="form-control" name="intent_id" type="text"
                                    value="<?php echo $row['intent_id']; ?>" readonly><br>
                                <label for="intentName">Tên Intent (chủ đề cuộc trò chuyện)</label>
                                <input type="text" class="form-control" id="intentName" name="intentName"
                                    placeholder="Nhập chủ đề" value="<?php echo $row['intent_name']; ?>" readonly>


                            </div>
                            <div class="form-group">
                                <label for="description">Câu hỏi liên quan đến chủ đề này</label>
                                <textarea class="form-control" id="question" name="question" placeholder="Nhập câu hỏi"
                                    rows="3"></textarea>
                            </div>
                            <div class="form-group">
                                <label for="answer">Câu trả lời cho chủ đề này</label>
                                <textarea class="form-control" id="answer" name="answer" placeholder="Nhập câu trả lời"
                                    rows="3"></textarea>
                            </div>

                            <button type="submit" id="btn-submit" class="btn btn-primary">Thêm mới</button>

                        </form>
                    </div>
                </div>
            </div>
            <!-- Lắng nghe sự kiện submit của biểu mẫu -->
            <script>
                document.getElementById('btn-submit').addEventListener('submit', function (event) {
                    // Ngăn chặn hành động mặc định của biểu mẫu
                    event.preventDefault();

                    // Tải lại trang
                    location.reload();
                });
            </script>
            <!-- nut xoa cau hoi -->
            <script>
                document.addEventListener("DOMContentLoaded", function () {
                    const deleteExampleButtons = document.querySelectorAll(".btn-delete-example");

                    deleteExampleButtons.forEach(function (button) {
                        button.addEventListener("click", function () {
                            const id = this.getAttribute("data-id");
                            const isConfirmed = confirm("Bạn có chắc chắn muốn xóa câu hỏi?");
                            if (isConfirmed) {
                                $.ajax({
                                    type: "POST",
                                    url: "delete_example.php",
                                    data: { id: id },
                                    success: function (response) {
                                        console.log(response);
                                        window.location.reload();
                                    }
                                });
                            }
                        });
                    });
                });
            </script>
            <!-- nut xoa cau tra loi -->
            <script>
                document.addEventListener("DOMContentLoaded", function () {
                    const deleteAnswerButtons = document.querySelectorAll(".btn-delete-answer");

                    deleteAnswerButtons.forEach(function (button) {
                        button.addEventListener("click", function () {
                            const id = this.getAttribute("data-id");
                            const isConfirmed = confirm("Bạn có chắc chắn muốn xóa câu trả lời?");
                            if (isConfirmed) {
                                $.ajax({
                                    type: "POST",
                                    url: "delete_answer.php",
                                    data: { id: id },
                                    success: function (response) {
                                        console.log(response);
                                        window.location.reload();
                                    }
                                });
                            }
                        });
                    });
                });
            </script>
            <!-- sua cau hoi -->
            <script>
                document.addEventListener("DOMContentLoaded", function () {
                    const editButtons = document.querySelectorAll(".btn-edit-example");
                    editButtons.forEach(function (button) {
                        button.addEventListener("click", function () {
                            const id = this.getAttribute("data-id");

                            // Lấy giá trị hiện tại của textarea
                            const textarea = this.parentElement.querySelector("textarea");
                            const currentValue = textarea.value;

                            if (currentValue !== null) {
                                $.ajax({
                                    url: "edit_example.php",
                                    method: "POST",
                                    data: { id: id, value: currentValue },
                                    success: function (response) {
                                        // Xử lý phản hồi từ máy chủ nếu cần
                                        console.log(response);
                                    },
                                    error: function (xhr, status, error) {
                                        // Xử lý lỗi nếu có
                                        console.error("Có lỗi xảy ra: ", error);
                                    }
                                });
                            }
                        });
                    });
                });
            </script>
            <!-- sua cau tra loi -->
            <script>
                document.addEventListener("DOMContentLoaded", function () {
                    const editButtons = document.querySelectorAll(".btn-edit-answer");
                    editButtons.forEach(function (button) {
                        button.addEventListener("click", function () {
                            const id = this.getAttribute("data-id");

                            // Lấy giá trị hiện tại của textarea
                            const textarea = this.parentElement.querySelector("textarea");
                            const currentValue = textarea.value;

                            if (currentValue !== null) {
                                $.ajax({
                                    url: "edit_answer.php",
                                    method: "POST",
                                    data: { id: id, value: currentValue },
                                    success: function (response) {
                                        // Xử lý phản hồi từ máy chủ nếu cần
                                        console.log(response);
                                    },
                                    error: function (xhr, status, error) {
                                        // Xử lý lỗi nếu có
                                        console.error("Có lỗi xảy ra: ", error);
                                    }
                                });
                            }
                        });
                    });
                });
            </script>

        </body>
        

        </html>
        <?php
    } else {
        echo "Không tìm thấy thông tin chi tiết về ý định.";
    }
} else {
    echo "Tham số intent_id không được truyền.";
}
?>