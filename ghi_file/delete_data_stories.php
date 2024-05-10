<?php
function delete_story_block($intent, $filename) {
    // Đọc toàn bộ nội dung từ file
    $content = file_get_contents($filename);

    // Tìm vị trí bắt đầu và kết thúc của story block
    $start_index = strpos($content, "- story: " . $intent." path");
    if ($start_index !== false) {
        $end_index = strpos($content, "- story:", $start_index + 1);
        if ($end_index === false) {
            // If this is the last story, set the end index to the end of the content
            $end_index = strlen($content);
        }

        // Xóa khối dữ liệu của story
        $story_block = substr($content, $start_index, $end_index - $start_index);
        $content = str_replace($story_block, '', $content);

        // Ghi lại nội dung đã chỉnh sửa vào file
        file_put_contents($filename, $content);
        echo "Đã xóa story '$intent' khỏi file.<br>";
    } else {
        echo "Không tìm thấy story '$intent' trong file.<br>";
    }
}
// delete_story_block("phong_truyen_thong","./rasa_php/data/stories.yml");

?>