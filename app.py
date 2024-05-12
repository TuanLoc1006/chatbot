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
            bot_responses = [message['text'] for message in rasa_response_json]  # Lấy nội dung tin nhắn từ mỗi phần tử của danh sách
            print('Bot Response:', bot_responses)
            return jsonify(bot_responses)  # Trả về danh sách các phản hồi của bot dưới dạng JSON
        else:
            return "Xin lỗi, tôi không hiểu !!!"
    
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return "Đã xảy ra lỗi trong khi xử lý yêu cầu của bạn"

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run()