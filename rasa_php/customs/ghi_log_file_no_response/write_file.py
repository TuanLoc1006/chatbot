def get_ghi_log_file(user_input):
    try:
        # Đường dẫn đến thư mục bạn muốn lưu tệp
        directory_path = "C:\\xampp\htdocs\\chatbot\\rasa_php\\customs\\ghi_log_file_no_response\\"

        with open(directory_path + "log_file.txt", "w", encoding="utf-8") as file:
            file.write(user_input)
        print("Ghi file thành công!")
    except IOError:
        print("Lỗi: Không thể ghi file.")

# Gọi hàm với user_input bất kỳ
get_ghi_log_file("Nội dung muốn ghi vào tệp")

class write_file:
    def __init__(self):
        pass
    
    def get_log_file(self, user_input):
        return get_ghi_log_file(user_input)
