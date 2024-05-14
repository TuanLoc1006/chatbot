def ghi_log_file(user_input):
    try:
        # Đường dẫn đến thư mục bạn muốn lưu tệp
        directory_path = "C:\\xampp\htdocs\\chatbot\\rasa_php\\customs\\ghi_log_file_no_response\\"

        with open(directory_path + "log_file.txt", "a", encoding="utf-8") as file:
            file.write(user_input + '\n')
        print("Ghi file thành công!")
    except IOError:
        print("Lỗi: Không thể ghi file.")

# Gọi hàm với user_input bất kỳ
ghi_log_file("Nội dung muốn ghi vào tệp")

class write_file:
    def __init__(self):
        pass

    def get_ghi_log_file(self, user_input):
        return ghi_log_file(user_input)
