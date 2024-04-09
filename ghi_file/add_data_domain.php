<?php
function add_data_to_file_domain($intent, $answer, $filename) {
    // Đọc toàn bộ nội dung từ file
    $lines = file($filename);

    $insert_index_intent = null;
    foreach ($lines as $i => $line) {
        if (trim($line) == "intents:") {
            $insert_index_intent = $i + 1;  // Bắt đầu thêm từ dòng tiếp theo sau intent
            break;
        }
    }

    if ($insert_index_intent !== null) {
        // Kiểm tra xem intent đã tồn tại chưa
        $intent_exists = false;
        foreach (array_slice($lines, $insert_index_intent) as $line) {
            if (trim($line) == "- $intent") {
                $intent_exists = true;
                break;
            }
        }

        if (!$intent_exists) {
            $new_content = "  - $intent\n";
            array_splice($lines, $insert_index_intent, 0, $new_content);
            echo 'Đã thêm intent<br>';
        } else {
            echo 'Đã có intent trong file domain.<br>';
        }
    }

    $insert_index_intent1 = null;
    foreach ($lines as $i1 => $line) {
        if (trim($line) == "responses:") {
            $insert_index_intent1 = $i1 + 1;  // Bắt đầu thêm từ dòng tiếp theo sau responses
            break;
        }
    }

    if ($insert_index_intent1 !== null) {
        $new_utter = "  utter_$intent:";
        $new_text = "  - text: \"$answer\"\n";

        // Lặp qua các dòng từ vị trí $insert_index_intent1 để kiểm tra xem utter đã tồn tại hay không
        $found_utter = false;
        foreach ($lines as $i => $line) {
            // Nếu tìm thấy block utter tương ứng với intent
            if (trim($line) == "utter_$intent:") {
                $found_utter = true;
                // Tìm vị trí cuối cùng của block utter bằng cách đếm số lượng dòng chứa text trong block
                $utter_end_index = $i + 1;
                while ($utter_end_index < count($lines) && substr(trim($lines[$utter_end_index]), 0, 9) == "- text: \"") {
                    // Kiểm tra xem text đã tồn tại trong block utter hay chưa
                    $text_nlu = trim($lines[$utter_end_index]);
                    $text_answer = "- text: \"$answer\"";
                    if ($text_nlu == $text_answer) {
                        echo 'Text đã tồn tại trong block utter.<br>';
                        return;  // Nếu text đã tồn tại, không thêm và kết thúc hàm
                    }
                    $utter_end_index++;
                }

                // Chèn text vào cuối block utter nếu chưa tồn tại
                array_splice($lines, $utter_end_index, 0, "  - text: \"$answer\"\n");
                echo 'Đã thêm text vào cuối block utter.<br>';
                break;  // Thoát khỏi vòng lặp sau khi thêm text
            }
        }

        if (!$found_utter) {
            // Thêm utter mới và text
            $new_content = "$new_utter\n$new_text";
            array_splice($lines, $insert_index_intent1, 0, $new_content);
            echo 'Đã thêm utter mới và text.<br>';
        }
    }

    // Ghi lại toàn bộ nội dung đã chỉnh sửa vào file
    file_put_contents($filename, implode("", $lines));
}




// function add_data_to_file_domain($intent, $answer, $filename) {
//     // Đọc toàn bộ nội dung từ file
//     $lines = file($filename);

//     // Tạo biến để kiểm tra xem đã tìm thấy block utter tương ứng chưa
//     $found_utter = false;

//     foreach ($lines as $i => $line) {
//         // Nếu tìm thấy block utter tương ứng với intent
//         if (trim($line) == "utter_" . $intent . ":") {
//             $found_utter = true;
//             // Tìm vị trí cuối cùng của block utter bằng cách đếm số lượng dòng chứa text trong block
//             $utter_end_index = $i + 1;
//             while ($utter_end_index < count($lines) && strpos(trim($lines[$utter_end_index]), "- text:") === 0) {
//                 // Kiểm tra xem text đã tồn tại trong block utter hay chưa
//                 if (trim($lines[$utter_end_index]) == "- text: \"$answer\"") {
//                     echo "Text đã tồn tại trong block utter.";
//                     return;  // Nếu text đã tồn tại, không thêm và kết thúc hàm
//                 }
//                 $utter_end_index++;
//             }

//             // Chèn text vào cuối block utter nếu chưa tồn tại
//             array_splice($lines, $utter_end_index, 0, "  - text: \"$answer\"\n");
//             echo 'Đã thêm text vào cuối block utter.';
//             break;  // Thoát khỏi vòng lặp sau khi thêm text
//         }
//     }

//     // Ghi lại toàn bộ nội dung đã chỉnh sửa vào file
//     file_put_contents($filename, implode("", $lines));
// }

// Sử dụng hàm
// add_data_to_file_domain('deny', 'khong chiu nha ban oi', './domain.yml');
?>
