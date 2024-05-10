<?php

function add_data_to_file_story($story, $intent, $action, $filename) {
    // Đọc toàn bộ nội dung từ file
    $lines = file($filename);

    $insert_index = null;
    $story_found = false;
    foreach ($lines as $i => $line) {
        if (trim($line) == "- story: " . $story) {
            $story_found = true;
            // Tìm vị trí cuối cùng của story
            if (in_array("\n", array_slice($lines, $i))) {
                $end_of_story_index = array_search("\n", array_slice($lines, $i)) + $i;
            } else {
                $end_of_story_index = count($lines);
            }
            $insert_index = $end_of_story_index;   // Số dòng để chèn intent và action
            break;
        }
    }

    if (!$story_found) {
        // Tạo mới story nếu không tìm thấy
        $lines[] = "\n- story: $story\n";
        $lines[] = "  steps:\n";
        $insert_index = count($lines);   // Số dòng để chèn intent và action
    }

    // Kiểm tra xem intent và action đã tồn tại trong story hay chưa
    $intent_exists = false;
    $action_exists = false;
    foreach ($lines as $line) {
        if (strpos($line, "  - intent: $intent") !== false) {
            $intent_exists = true;
        }
        if (strpos($line, "  - action: $action") !== false) {
            $action_exists = true;
        }
    }

    // Chèn intent và action vào story tương ứng nếu chưa tồn tại
    // if ($insert_index !== null && !$intent_exists) {
    //     array_splice($lines, $insert_index, 0, "  - intent: $intent\n");
    // }
    // if ($insert_index !== null && !$action_exists) {
    //     array_splice($lines, $insert_index + 1, 0, "  - action: $action\n");
    // }
    // Chèn intent và action vào story tương ứng nếu chưa tồn tại
    if ($insert_index !== null && !$intent_exists) {
        array_splice($lines, $insert_index, 0, "  - intent: $intent\n");
        $insert_index++; // Cập nhật chỉ số
    }
    if ($insert_index !== null && !$action_exists) {
        array_splice($lines, $insert_index + 1, 0, "  - action: $action\n");
        $insert_index++; // Cập nhật chỉ số
    }

    // Ghi lại toàn bộ nội dung đã chỉnh sửa vào file
    file_put_contents($filename, implode("", $lines));
}

// add_data_to_file_story("deny2", "new", "new", "../data/stories.yml");

?>
