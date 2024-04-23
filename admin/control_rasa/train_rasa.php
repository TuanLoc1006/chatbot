<?php
if(isset($_POST['train_rasa'])) {
    // Thực thi lệnh để huấn luyện Rasa từ thư mục chứa dự án Rasa
    exec("cd .\\rasa_php\\ && rasa train", $output);

    // Hiển thị kết quả
    echo "Rasa is being trained...<br>";
    echo "Training output:<br>";
    foreach ($output as $line) {
        echo $line . "<br>";
    }
    echo "training finished";
    // exec("rasa run", $output);
    // echo "rasa shell open terminal";
    // echo "rasa running";
}
?>
