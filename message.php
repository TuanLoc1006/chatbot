<!-- Created By CodingNepal -->
<?php
$getMesg = $_POST['text']; // Fetching user message from POST data
// echo $getMesg;
// Sending user message to Flask server
$data = array('message' => $getMesg);
$flask_url = 'http://localhost:5005/webhooks/rest/webhook';
$options = array(
    'http' => array(
        'method'  => 'POST',
        'content' => json_encode($data),
        'header'=>  "Content-Type: application/json\r\n" .
                    "Accept: application/json\r\n"
    )
);
$context  = stream_context_create($options);
$result = file_get_contents($flask_url, false, $context);

// Outputting the response from Flask server
if ($result !== FALSE) {
    $rasa_response = json_decode($result, true);
    foreach ($rasa_response as $response) {
        echo $response['text'] . "<br>"; // Assuming the response contains 'text' field
    }
} else {
    echo "Sorry, can't connect to the chatbot server.";
}
?>
