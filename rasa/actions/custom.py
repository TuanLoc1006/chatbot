import pandas as pd 
stop_words = pd.read_csv('C:\\xampp\htdocs\\chatbot\\rasa\\actions\\vietnamese_stopwords.txt')
print(stop_words)

class Custom:

    def remove_stop_words(chuoi):
        results = []
        for text in chuoi:
            tmp = text.split(' ')
            # Loại bỏ các từ có trong stop_words
            filtered_words = [word for word in tmp if word not in stop_words]
            results.append(" ".join(filtered_words))
        return results

