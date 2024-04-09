<?php
include 'db_con.php';
include './ghi_file/add_data_nlu.php';
include './ghi_file/add_data_domain.php';
include './ghi_file/add_data_stories.php';

$file_nlu = './rasa_php/data/nlu.yml';
$file_domain = './rasa_php/domain.yml';
$file_stories = './rasa_php/data/stories.yml';

$sql_id_intents = "SELECT `intent_id` FROM `intents` WHERE 1";
$result = $conn->query($sql_id_intents);
if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        $intent_id = $row['intent_id'];
        echo "====> $intent_id\n";

        $sql = "SELECT i.intent_name, e.example_question, a.chat_answer 
        FROM `intents` i 
        JOIN example_intent e ON e.intent_id = i.intent_id 
        JOIN answer_intent a ON a.intent_id = i.intent_id 
        WHERE i.intent_id = '$intent_id' and e.status_file = '0' and a.status_file = '0'";
        $resultsql = $conn->query($sql);
        if ($resultsql->num_rows > 0) {
            while ($rowIntent = $resultsql->fetch_assoc()) {
                $intent_Name = $rowIntent['intent_name'];
                $example_question = $rowIntent['example_question'];
                $chat_answer = $rowIntent['chat_answer'];
                echo "$intent_Name--$example_question--$chat_answer <br>";
                add_data_to_file_nlu($intent_Name, $example_question, $file_nlu);
                $sql_example_question = "UPDATE `example_intent` SET `status_file`='1' WHERE example_question='$example_question'";
                if ($conn->query($sql_example_question) === TRUE) {
                    echo "Da update status_file cua example_intent = 1";
                } else {
                    echo "loi update status_file example_intent" . $conn->error;
                }
                add_data_to_file_domain($intent_Name, $chat_answer,$file_domain);
                $sql_chat_answer = "UPDATE `answer_intent` SET `status_file`='1' WHERE chat_answer = '$chat_answer'";
                if ($conn->query($sql_chat_answer) === TRUE) {
                    echo "Da update status_file cua answer_intent = 1";
                } else {
                    echo "loi update status_file answer_intent" . $conn->error;
                }
                $story_intent = $intent_Name . " path";
                echo "===>";
                $utter_intent = "utter_" . $intent_Name; 
                echo $utter_intent;
                add_data_to_file_story($story_intent,$intent_Name,$utter_intent,$file_stories);
            }
        }else{
            echo 0;
        }
    }
}


// $sql_intents = "SELECT i.intent_name, e.example_question, a.chat_answer 
// FROM `intents` i 
// JOIN example_intent e ON e.intent_id = i.intent_id 
// JOIN answer_intent a ON a.intent_id = i.intent_id 
// WHERE i.intent_id = 18
// ";

// $result = $conn->query($sql_intents);
// if ($result->num_rows > 0) {
//     while ($row = $result->fetch_assoc()) {
//         add_data_to_file_domain($row['intent_name'], $row['chat_answer'],$file_domain);
//         add_data_to_file_nlu($row['intent_name'], $row['example_question'], $file_nlu);
//     }
// } else {
//     echo "Không có dữ liệu";
// }

// Đóng kết nối đến CSDL
$conn->close();
?>