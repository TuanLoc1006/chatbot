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
        
        if rasa_response_json:  # Kiểm tra nếu danh sách rasa_response_json không rỗng
            bot_response = rasa_response_json[0]['text']  # Truy cập phần tử đầu tiên của danh sách
            print('Bot Response:', bot_response)
            return bot_response
        else:
            return "Xin lỗi, tôi không hiểu"
    
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return "An error occurred while processing your request."

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run()
