<?php
include "../../db_con.php";

include "../../ghi_file/delete_data_nlu.php";
include "../../ghi_file/delete_data_domain.php";
include "../../ghi_file/delete_data_stories.php";

$file_nlu = '../../rasa_php/data/nlu.yml';
$file_domain = '../../rasa_php/domain.yml';
$file_stories = '../../rasa_php/data/stories.yml';

if (isset($_POST['delete_intent'])) {
    $intent_id = $_POST['intent_id'];
    $intent_name = $_POST['intent_name'];
    
    delete_block_by_intent($intent_name, $file_nlu);
    delete_domain_intent_block($intent_name, $file_domain);
    delete_domain_responses_block($intent_name, $file_domain);
    delete_story_block($intent_name, $file_stories);
    
    // Chuẩn bị câu lệnh SQL DELETE cho từng bảng
    $sql_example_intent = "DELETE FROM example_intent WHERE intent_id = $intent_id";
    $sql_answer_intent = "DELETE FROM answer_intent WHERE intent_id = $intent_id";

    // Thực hiện câu lệnh xóa cho từng bảng
    if ($conn->query($sql_example_intent) === TRUE && $conn->query($sql_answer_intent) === TRUE) {
        // Tiếp tục xóa từ bảng intents
        $sql_intents = "DELETE FROM intents WHERE intent_id = $intent_id";
        if ($conn->query($sql_intents) === TRUE) {
            // Nếu xóa thành công, chuyển hướng đến trang chính
            header("Location: home.php");
            exit();
        } else {
            echo "Error deleting record from intents table: " . $conn->error;
        }
    } else {
        echo "Error deleting records from example_intent or answer_intent tables: " . $conn->error;
    }

    // Đóng kết nối
    $conn->close();
}
?>
