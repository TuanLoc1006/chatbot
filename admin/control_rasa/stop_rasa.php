<?php
if(isset($_POST['stop_rasa'])) {
    echo "Rasa is being stop...<br>";
    // Thực thi lệnh để huấn luyện Rasa từ thư mục chứa dự án Rasa
    exec('cd ..\\..\\rasa_php\\ && Stop-Process -Name "rasa"');

    echo "stop finished";
}
?>

<!-- Stop-Process -Name "rasa" -->