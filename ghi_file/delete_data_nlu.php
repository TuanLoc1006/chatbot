
<?php

function delete_block_by_intent($intent, $filename) {
    // Đọc toàn bộ nội dung từ file
    $lines = file($filename);
    $block_found = false;
    $start_index = -1;
    $end_index = -1;
    foreach ($lines as $i => $line) {
        // Tìm intent và lấy vị trí bắt đầu của khối dữ liệu
        if (trim($line) == "- intent: " . $intent) {
            $block_found = true;
            $start_index = $i;
            // Tìm vị trí kết thúc của khối dữ liệu
            $end_index = $start_index + 1;
            while ($end_index < count($lines) && substr($lines[$end_index], 0, 10) != "- intent: ") {
                    $end_index++;
            }
            break;
        }
    }

    if ($block_found) {
        // Xóa khối dữ liệu
        array_splice($lines, $start_index, $end_index - $start_index);
        print($start_index.' ');
        print($end_index - $start_index + 1);
        // Ghi lại nội dung đã chỉnh sửa vào file
        file_put_contents($filename, implode("", $lines));
        echo "Đã xóa khối dữ liệu của intent '$intent' khỏi file.<br>";
    } else {
        echo "Không tìm thấy intent '$intent' trong file.<br>";
    }
}

// delete_block_by_intent("phong_truyen_thong","./rasa_php/data/nlu.yml");
?>
