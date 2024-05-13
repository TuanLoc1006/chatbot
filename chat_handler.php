<?php
// Import PHP cURL library
function callRasaAPI($userMessage) {
    // RASA API URL
    $RASA_API_URL = 'http://localhost:5005/webhooks/rest/webhook';
    // Data to be sent in POST request
    $data = json_encode(array('message' => $userMessage));
    // Set up cURL
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $RASA_API_URL);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
    // Execute the cURL request
    $response = curl_exec($ch);
    // Check for errors
    if(curl_errno($ch)) {
        $error_msg = curl_error($ch);
        // Handle curl error
        echo "An error occurred: " . $error_msg;
    }
    // Close cURL session
    curl_close($ch);
    // Return the response
    return $response;
}

// Get user message from request JSON
$requestData = json_decode(file_get_contents('php://input'), true);
$userMessage = $requestData['message'];
// Call RASA API
$rasaResponse = callRasaAPI($userMessage);
// Decode RASA response JSON
$rasaResponseJson = json_decode($rasaResponse, true);
// Check if RASA response is not empty
if (!empty($rasaResponseJson)) {
    // Extract bot responses from RASA response
    $botResponses = array();
    foreach ($rasaResponseJson as $message) {
        $botResponses[] = $message['text'];
    }
    // Return bot responses as JSON
    echo json_encode($botResponses);
} else {
    // Return error message if RASA response is empty
    echo "Xin lỗi, tôi không hiểu !!!";
}
?>
