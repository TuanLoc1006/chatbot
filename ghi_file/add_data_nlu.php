<?php


function add_data_to_file_nlu($intent, $examples, $filename) {
    // Đọc toàn bộ nội dung từ file
    $lines = file($filename);

    $intent_found = false;
    foreach ($lines as $i => $line) {
        if (trim($line) == "- intent: " . $intent) {
            $intent_found = true;
            // Tìm vị trí bắt đầu của khối examples
            $start_index = $i + 1;
            $end_index = $start_index;
            while ($end_index < count($lines) && substr($lines[$end_index], 0, 2) == "  ") {
                if (trim($lines[$end_index]) == "    - " . $examples) {
                    // echo "Nội dung intent đã tồn tại, không thêm example question mới.<br>";
                    return;
                }
                $end_index++;
            }
            // Thêm nội dung mới vào cuối khối examples
            array_splice($lines, $end_index, 0, "    - $examples\n");
            break;
        }
    }

    if (!$intent_found) {
        // Tạo mới intent nếu không tìm thấy
        $lines[] = "- intent: $intent\n";
        $lines[] = "  examples: |\n";
        $lines[] = "    - $examples\n";
    }

    // Ghi lại toàn bộ nội dung đã chỉnh sửa vào file
    file_put_contents($filename, implode("", $lines));
}


?>
