<?php
include '../includes/db_con.php';


if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['id'])) {
    $id = $_POST['id'];
    $newValue = $_POST['value'];

    // Thực hiện cập nhật dữ liệu
    $sql = "UPDATE example_intent SET example_question='$newValue' WHERE id='$id'";
    
    if ($conn->query($sql) === TRUE) {
        echo "Dữ liệu đã được cập nhật thành công";
    } else {
        echo "Lỗi: " . $sql . "<br>" . $conn->error;
    }
}

$conn->close();
?>
