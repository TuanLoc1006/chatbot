<?php
include "db_con.php";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $intentName = $_POST['intentName'];
    $question = $_POST['question'];
    $answer = $_POST['answer'];
    $intent_id_detail = $_POST['intent_id'];
    echo $intent_id_detail;

    $sql_intents = "SELECT `intent_id`, `intent_name` FROM `intents` WHERE `intent_name` = '$intentName'";
    $result = $conn->query($sql_intents);
    if ($result->num_rows > 0) {
        $row = $result->fetch_assoc();
        $intent_ID = $row['intent_id'];
        $intent_Name = $row['intent_name'];

        // Check if $question is empty
        if (!empty($question)) {
            // Insert $question into example_intent table
            $sql = "INSERT INTO `example_intent`(`id`, `intent_id`, `example_question`, `status_file`) VALUES ('','$intent_ID','$question', '0')";
            if ($conn->query($sql) === TRUE) {
                // echo "Thêm dữ liệu example_intent thành công<br>";
            } else {
                // echo "Thêm dữ liệu example_intent thất bại:<br>" . $conn->error;
            }
        }

        // Check if $answer is empty
        if (!empty($answer)) {
            // Insert $answer into answer_intent table
            $sql = "INSERT INTO `answer_intent`(`id`, `intent_id`, `chat_answer`, `status_file`) VALUES ('','$intent_ID','$answer', '0')";
            if ($conn->query($sql) === TRUE) {
                // echo "Thêm dữ liệu answer_intent thành công<br>";
            } else {
                // echo "Thêm dữ liệu answer_intent thất bại:<br>" . $conn->error;
            }
        }
    } else {// neu chua co intent_name thi them moi vao bang intents va bang example_intent
        $sql = "INSERT INTO `intents`(`intent_id`, `intent_name`) VALUES ('','$intentName')";
        if ($conn->query($sql) === TRUE) {
            $sql_intents = "SELECT `intent_id`, `intent_name` FROM `intents` WHERE `intent_name` = '$intentName'";
            $result = $conn->query($sql_intents);
            if ($result->num_rows > 0) {
                $row = $result->fetch_assoc();
                $intent_ID = $row['intent_id'];
                $intent_Name = $row['intent_name'];

                if ($intent_ID != "") {
                    // Check if $question is empty
                    if (!empty($question)) {
                        // Insert $question into example_intent table
                        $sql = "INSERT INTO `example_intent`(`id`, `intent_id`, `example_question`, `status_file`) VALUES ('','$intent_ID','$question', '0')";
                        if ($conn->query($sql) === TRUE) {
                            // echo "Thêm dữ liệu example_intent thành công<br>";
                        } else {
                            // echo "Thêm dữ liệu example_intent thất bại:<br>" . $conn->error;
                        }
                    }

                    // Check if $answer is empty
                    if (!empty($answer)) {
                        // Insert $answer into answer_intent table
                        $sql = "INSERT INTO `answer_intent`(`id`, `intent_id`, `chat_answer`, `status_file`) VALUES ('','$intent_ID','$answer', '0')";
                        if ($conn->query($sql) === TRUE) {
                            // echo "Thêm dữ liệu answer_intent thành công<br>";
                        } else {
                            // echo "Thêm dữ liệu answer_intent thất bại:<br>" . $conn->error;
                        }
                    }
                }
            }
        } else {
            // echo "Thêm dữ liệu intents thất bại:<br>" . $conn->error;
        }
    }
    
    header("Location: intent_details.php?intent_id=$intent_id_detail");
}

?>
