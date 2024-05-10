<?php
if(isset($_POST['run_rasa'])) {
    // Thực thi lệnh để huấn luyện Rasa từ thư mục chứa dự án Rasa
  
    exec("cd ..\\..\\rasa_php\\ && rasa run");

    // Hiển thị kết quả
    
}
    
?>