<?php
include "../../includes/db_con.php";

// Kiểm tra xem có tham số intent_id được truyền qua URL không
if (isset($_GET['intent_id'])) {
    $intent_id = $_GET['intent_id'];

    // Truy vấn cơ sở dữ liệu để lấy thông tin chi tiết về ý định
    $sql_intent_details = "SELECT * FROM `intents` WHERE `intent_id` = $intent_id";
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
            <h3><a href="./home.php">Trang admin</a></h3>
            <div class="container">
                <div class="row">
                    <div class="col-md-6">
                        <h2>Intent Details</h2>
                        <!-- <p><strong>Intent Name:</strong> <?php echo $row['intent_name']; ?> </p> -->

                        <div class="question-list">
                            <h2>Mẫu câu hỏi:</h2>
                            <?php
                            $sql_ex_intents = "SELECT `id`, `intent_id`, `example_question`, `status_file` FROM `example_intent` WHERE `intent_id`='$intent_id' ";
                            $result_example_intent = $conn->query($sql_ex_intents);
                            while ($row = $result_example_intent->fetch_assoc()) {
                                echo '<div class="item"><textarea rows="2" cols="70" class="example-question" data-id="' . $row['id'] . '">' . $row['example_question'] . '</textarea></div>';
                            }
                            ?>
                        </div>

                        <div class="answer-lis  t">
                            <h2>Mãu câu trả lời:</h2>
                            <?php
                            $sql_chat_answer = "SELECT `id`, `intent_id`, `chat_answer`, `status_file` FROM `answer_intent` WHERE `intent_id`='$intent_id'";
                            $result_chat_answer = $conn->query($sql_chat_answer);
                            while ($row = $result_chat_answer->fetch_assoc()) {
                                echo '<div class="item"><textarea rows="2" cols="70" class="chat-answer" data-id="' . $row['id'] . '">' . $row['chat_answer'] . '</textarea> </div>';
                            }
                            ?>
                        </div>

                    </div>
                    
                </div>
            </div>
            

           


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