<?php
include "../../includes/db_con.php";

if (isset($_POST['intent_id']) && isset($_POST['selected'])) {
    $intent_id = $_POST['intent_id'];
    $selected = $_POST['selected'];

    $sql_update = "UPDATE intents SET selected = ? WHERE intent_id = ?";
    $stmt = $conn->prepare($sql_update);
    $stmt->bind_param('ii', $selected, $intent_id);
    
    if ($stmt->execute()) {
        echo "Cập nhật thành công";
    } else {
        echo "Cập nhật thất bại";
    }

    $stmt->close();
}
?>
