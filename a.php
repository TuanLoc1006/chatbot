<?php
// Hàm gọi API của Rasa
function callRasaAPI($userMessage) {
    // Địa chỉ API của Rasa
    $RASA_API_URL = 'http://localhost:5005/webhooks/rest/webhook';
    // Dữ liệu sẽ gửi trong yêu cầu POST
    $data = json_encode(array('message' => $userMessage, 'sender' => 'user'));
    // Thiết lập cURL
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $RASA_API_URL);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
    // Thực thi yêu cầu cURL
    $response = curl_exec($ch);
    // Kiểm tra lỗi
    if (curl_errno($ch)) {
        $error_msg = curl_error($ch);
        // Xử lý lỗi cURL
        echo "Đã xảy ra lỗi: " . $error_msg;
    }
    // Đóng phiên cURL
    curl_close($ch);
    // Trả về phản hồi
    return $response;
}

// Nhận tin nhắn người dùng từ JSON yêu cầu
$requestData = json_decode(file_get_contents('php://input'), true);
$userMessage = $requestData['message'] ?? '';

// Gọi API Rasa
$rasaResponse = callRasaAPI($userMessage);

// Giải mã phản hồi JSON từ Rasa
$rasaResponseJson = json_decode($rasaResponse, true);

// Kiểm tra nếu phản hồi từ Rasa không rỗng
if (!empty($rasaResponseJson)) {
    // Trích xuất các phản hồi của bot từ phản hồi của Rasa
    $botResponses = array();
    foreach ($rasaResponseJson as $message) {
        if (isset($message['text'])) {
            $botResponses[] = $message['text'];
        }
    }
    // Trả về các phản hồi của bot dưới dạng JSON
    echo json_encode($botResponses, JSON_UNESCAPED_UNICODE);
} else {
    // Trả về thông báo lỗi nếu phản hồi của Rasa rỗng
    echo json_encode(["Xin lỗi, tôi không hiểu !!!"], JSON_UNESCAPED_UNICODE);
}
?>
