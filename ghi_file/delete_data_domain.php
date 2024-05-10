<?php

function delete_domain_intent_block($intent, $filename) {
    // Đọc toàn bộ nội dung từ file
    $lines = file($filename);
    $block_found = false;
    $start_index = -1;
    $end_index = 0;
    foreach ($lines as $i => $line) {
        // Tìm intent và lấy vị trí bắt đầu của khối dữ liệu
        if (trim($line) == "- " . $intent) {
            $block_found = true;
            $start_index = $i;

            // Tìm vị trí kết thúc của khối dữ liệu
            $end_index = $start_index;
            while ($end_index < count($lines) && substr(trim($lines[$end_index]), 0, 1) != '-') {
                $end_index++;
            }

            break; // Found the block, no need to continue
        }
    }

    if ($block_found) {
        // Xóa khối dữ liệu
        array_splice($lines, $start_index, $end_index - $start_index + 1);

        // Ghi lại nội dung đã chỉnh sửa vào file
        file_put_contents($filename, implode("", $lines));
        echo "Đã xóa khối dữ liệu của intent '$intent' khỏi file.<br>";
    } else {
        echo "Không tìm thấy intent '$intent' trong file.<br>";
    }
}

function delete_domain_responses_block($response_name, $filename) {
    // Đọc toàn bộ nội dung từ file
    $lines = file($filename);
    $block_found = false;
    $start_index = -1;
    $end_index = 0;
    foreach ($lines as $i => $line) {
        // Tìm tên response và lấy vị trí bắt đầu của khối dữ liệu
        if (trim($line) == "utter_" . $response_name . ":") {
            $block_found = true;
            $start_index = $i;

            // Tìm vị trí kết thúc của khối dữ liệu
            $end_index = $start_index + 1; // Bắt đầu từ vị trí sau khi tìm thấy response
            while ($end_index < count($lines) && trim($lines[$end_index]) != "" && strpos(trim($lines[$end_index]), "utter_") === false) {
                $end_index++;
            }

            break; // Found the block, no need to continue
        }
    }

    if ($block_found) {
        // Xóa khối dữ liệu
        array_splice($lines, $start_index, $end_index - $start_index);

        // Ghi lại nội dung đã chỉnh sửa vào file
        file_put_contents($filename, implode("", $lines));
        echo "Đã xóa khối dữ liệu của response '$response_name' khỏi file.<br>";
    } else {
        echo "Không tìm thấy response '$response_name' trong file.<br>";
    }
}



// function delete_domain_responses_block($response_name, $filename) {
//     // Đọc toàn bộ nội dung từ file
//     $lines = file($filename);
//     $block_found = false;
//     $start_index = -1;
//     $end_index = 0;
//     foreach ($lines as $i => $line) {
//         // Tìm tên response và lấy vị trí bắt đầu của khối dữ liệu
//         if (trim($line) == "utter_" . $response_name . ":") {
//             $block_found = true;
//             $start_index = $i;

//             // Tìm vị trí kết thúc của khối dữ liệu
//             $end_index = $start_index;
//             while ($end_index < count($lines) && trim($lines[$end_index]) != "") {
//                 $end_index++;
//             }

//             break; // Found the block, no need to continue
//         }
//     }

//     if ($block_found) {
//         // Xóa khối dữ liệu
//         array_splice($lines, $start_index, $end_index - $start_index + 1);

//         // Ghi lại nội dung đã chỉnh sửa vào file
//         file_put_contents($filename, implode("", $lines));
//         echo "Đã xóa khối dữ liệu của response '$response_name' khỏi file.<br>";
//     } else {
//         echo "Không tìm thấy response '$response_name' trong file.<br>";
//     }
// }

// delete_domain_intent_block("phong_truyen_thong", "./rasa_php/domain.yml");
// delete_domain_responses_block("phong_truyen_thong", "./rasa_php/domain.yml");

?>
