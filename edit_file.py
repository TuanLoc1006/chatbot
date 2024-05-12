import re

# Đọc nội dung từ tệp đầu vào
with open('./rasa_php/customs/all_university_VN.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Sử dụng regex để tìm và thay thế tất cả các mẫu [[...]]
clean_text = re.sub(r'\[\[(.*?)\]\]', '', text)

# Ghi nội dung đã được chỉnh sửa vào tệp mới
with open('./rasa_php/customs/output.txt', 'w') as f:
    f.write(clean_text)
