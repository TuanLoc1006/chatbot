<?php
include "db_con.php";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $intentName = $_POST['intentName'];
    $question = $_POST['question'];
    $answer = $_POST['answer'];

    $sql_intents = "SELECT `intent_id`, `intent_name` FROM `intents` WHERE `intent_name` = '$intentName'";
    $result = $conn->query($sql_intents);
    if ($result->num_rows > 0) {
        $row = $result->fetch_assoc();
        $intent_ID = $row['intent_id'];
        $intent_Name = $row['intent_name'];

        //neu co intent_name roi thi them cau hoi vao example_intent
        if ($intent_ID != "") {
            //kiem tra example_question co trong example_intent chua
            $sql_example_question = "SELECT  `example_question` FROM `example_intent` WHERE `example_question` = '$question'";
            $result = $conn->query($sql_example_question);
            if ($result->num_rows > 0) {
                echo "da co question nay<br>";
                $sql_answer_intent = "SELECT  `chat_answer` FROM `answer_intent` WHERE `chat_answer` = '$answer'";
                $result = $conn->query($sql_answer_intent);
                if ($result->num_rows > 0) {
                    echo "da co answer nay<br>";
                } else {
                    $sql = "INSERT INTO `answer_intent`(`id`, `intent_id`, `chat_answer`, `status_file`) VALUES ('','$intent_ID','$answer', '0')";
                    if ($conn->query($sql) === TRUE) {
                        echo "Thêm dữ liệu answer_intent thành công<br>";
                    } else {
                        echo "Thêm dữ liệu answer_intent thất bại:<br>" . $conn->error;
                    }
                }
            } else {

                $sql = "INSERT INTO `example_intent`(`id`, `intent_id`, `example_question`, `status_file`) VALUES ('','$intent_ID','$question', '0')";
                if ($conn->query($sql) === TRUE) {
                    echo "Thêm dữ liệu example_intent thành công<br>";
                } else {
                    echo "Thêm dữ liệu example_intent thất bại:<br>" . $conn->error;
                }
                $sql_answer_intent = "SELECT  `chat_answer` FROM `answer_intent` WHERE `chat_answer` = '$answer'";
                $result = $conn->query($sql_answer_intent);
                if ($result->num_rows > 0) {
                    echo "da co answer nay<br>";
                } else {
                    $sql = "INSERT INTO `answer_intent`(`id`, `intent_id`, `chat_answer`, `status_file`) VALUES ('','$intent_ID','$answer', '0')";
                    if ($conn->query($sql) === TRUE) {
                        echo "Thêm dữ liệu answer_intent thành công<br>";
                    } else {
                        echo "Thêm dữ liệu answer_intent thất bại:<br>" . $conn->error;
                    }
                }
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
                    $sql = "INSERT INTO `example_intent`(`id`, `intent_id`, `example_question`, `status_file`) VALUES ('','$intent_ID','$question', '0')";
                    if ($conn->query($sql) === TRUE) {
                        echo "Thêm dữ liệu example_intent thành công<br>";
                    } else {
                        echo "Thêm dữ liệu example_intent thất bại:<br>" . $conn->error;
                    }

                    $sql = "INSERT INTO `answer_intent`(`id`, `intent_id`, `chat_answer`, `status_file`) VALUES ('','$intent_ID','$answer', '0')";
                    if ($conn->query($sql) === TRUE) {
                        echo "Thêm dữ liệu answer_intent thành công<br>";
                    } else {
                        echo "Thêm dữ liệu answer_intent thất bại:<br>" . $conn->error;
                    }
                }
            }
        } else {
            echo "Thêm dữ liệu intents thất bại:<br>" . $conn->error;
        }
    }

    // $sql_intents = "SELECT i.intent_name, e.example_question, a.chat_answer 
    //             FROM `intents` i 
    //             JOIN example_intent e ON e.intent_id = i.intent_id 
    //             JOIN answer_intent a ON a.intent_id = i.intent_id 
    //             WHERE i.intent_id = 37
    //             GROUP BY i.intent_id, i.intent_name, e.example_question, a.chat_answer";
    // $result = $conn->query($sql_intents);

    // if ($result->num_rows > 0) {
    //     while ($row = $result->fetch_assoc()) {
    //         $intent_Name = $row['intent_name'];
    //         $example_question = $row['example_question'];
    //         $chat_answer = $row['chat_answer'];
    //         echo "$intent_Name--$example_question--$chat_answer <br>";
    //     }
    // } else {
    //     echo "Không có dữ liệu<br>";
    // }

    // $sql = "INSERT INTO `intents`(`intent_id`, `intent_name`) VALUES ('','$intentName')";  
    // if ($conn->query($sql) === TRUE) {
    //     echo "Thêm dữ liệu intent thành công";
    // } else {
    //     echo "Thêm dữ liệu thất bại: " . $conn->error;
    // }

    // $answer = $_POST['answer'];
    // $sql_answer = "INSERT INTO `response`(`ResponseID`, `IntentID`, `ResponseText`) VALUES ('','$IntentID','$answer')";
    // if ($conn->query($sql_answer) === TRUE) {
    //     echo "Thêm dữ liệu response thành công";
    // } else {
    //     echo "Thêm dữ liệu thất bại: " . $conn->error;
    // }
}


?>