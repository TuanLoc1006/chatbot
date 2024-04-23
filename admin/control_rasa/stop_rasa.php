<?php
if(isset($_POST['stop_rasa'])) {
    // Thực thi lệnh để huấn luyện Rasa từ thư mục chứa dự án Rasa
    // exec("cd .\\rasa_php\\ && ", $output);

    // Hiển thị kết quả
    echo "Rasa is being stop...<br>";
    
    foreach ($output as $line) {
        echo $line . "<br>";
    }
    echo "stop finished";
    // exec("rasa run", $output);
    // echo "rasa shell open terminal";
    // echo "rasa running";
}
?>



<!-- Stop-Process -Name "rasa" -->