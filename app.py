from flask import Flask, render_template, request, jsonify
import requests


RASA_API_URL = 'http://localhost:5005/webhooks/rest/webhook'
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/webhook', methods=['POST'])
def webhooks():
    user_message = request.json['message']
    print('User Message:', user_message)

    try:
        rasa_response = requests.post(RASA_API_URL, json={'message': user_message})
        rasa_response.raise_for_status()
        rasa_response_json = rasa_response.json()
        print('Bot Response:', rasa_response_json[0]['text'])  # In ra phản hồi từ máy chủ RASA API
        bot_response = rasa_response_json[0]['text'] if rasa_response_json else 'Sorry, I didn\'t understand that.'
        # print(type(bot_response))
        return bot_response
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return "An error occurred while processing your request."


if __name__ == "__main__":
    print("Starting Flask server...")
    app.run()
