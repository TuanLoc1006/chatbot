<?php
include '../includes/db_con.php';


if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $intentName = $_POST['intentName'];
    $sql_intents = "SELECT `intent_id`, `intent_name` FROM `intents` WHERE `intent_name` = '$intentName'";
    $result = $conn->query($sql_intents);

    if ($result->num_rows > 0) {
        $row = $result->fetch_assoc();
        $intent_ID = $row['intent_id'];
        $intent_Name = $row['intent_name'];
        echo $intent_Name;
    }else{
        $sql = "INSERT INTO `intents`(`intent_id`, `intent_name`) VALUES ('','$intentName')";
        if ($conn->query($sql) === TRUE) {
            echo 1;
        }
    }

    header('Location: ../index.php');
}


?>