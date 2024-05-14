<?php
include "../../includes/db_con.php";
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (isset($_POST["id"])) {
        $id = $_POST["id"];

        // Xóa dòng từ CSDL dựa vào ID
        $sql_delete_example = "DELETE FROM answer_intent WHERE id = $id";
        if ($conn->query($sql_delete_example) === TRUE) {
            // Đóng kết nối đến CSDL
            $conn->close();

            // Chuyển hướng người dùng về trang intent_details.php
            header('Location: intent_detail.php'); // Điều chỉnh URL tùy theo tên trang của bạn
            exit; // Đảm bảo không có mã PHP nào thực thi sau khi chuyển hướng
        } else {
            echo "Lỗi: " . $conn->error;
        }
    } else {
        echo "Lỗi: Không tìm thấy ID answer";
    }
} else {
    echo "Lỗi: Yêu cầu không hợp lệ";
}
?>
