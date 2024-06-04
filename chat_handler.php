<?php
// Hàm gọi API của Rasa
function callRasaAPI($userMessage) {
    $RASA_API_URL = 'http://localhost:5005/webhooks/rest/webhook';
    $data = json_encode(array('message' => $userMessage, 'sender' => 'user'));
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $RASA_API_URL);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
    $response = curl_exec($ch);
    if (curl_errno($ch)) {
        $error_msg = curl_error($ch);
        echo json_encode(["Đã xảy ra lỗi kết nối server: " . $error_msg], JSON_UNESCAPED_UNICODE);
    }
    curl_close($ch);
    return $response;
}

$requestData = file_get_contents('php://input');
if ($requestData) {
    $requestData = json_decode($requestData, true);
    if (json_last_error() === JSON_ERROR_NONE) {
        $userMessage = $requestData['message'] ?? '';
        $rasaResponse = callRasaAPI($userMessage);
        $rasaResponseJson = json_decode($rasaResponse, true);
        if (!empty($rasaResponseJson)) {
            $botResponses = array();
            foreach ($rasaResponseJson as $message) {
                if (isset($message['text']) && !empty($message['text'])) {
                    $botResponses[] = $message['text'];
                }
            }
            if (empty($botResponses)) {
                echo json_encode(["Xin lỗi, tôi không hiểu !!!"], JSON_UNESCAPED_UNICODE);
            } else {
                echo json_encode($botResponses, JSON_UNESCAPED_UNICODE);
            }
        } else {
            echo json_encode(["Xin lỗi, tôi không hiểu !!!"], JSON_UNESCAPED_UNICODE);
        }
    } else {
        echo json_encode(["Yêu cầu không hợp lệ, không thể giải mã JSON"], JSON_UNESCAPED_UNICODE);
    }
} else {
    echo json_encode(["Yêu cầu không có dữ liệu đầu vào"], JSON_UNESCAPED_UNICODE);
}
?>