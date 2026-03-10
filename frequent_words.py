import pandas

max = 0
file_words = [pandas.read_csv("file_path")]

read_words = {}
top_words = {}

for item in file_words:
    if item in read_words:
        read_words.count =+ 1
    else:
        read_words.word = item
        read_words.count = 1
    
for i in range(0, 10):
    if item in read_words:
        if item.count > (item-1).count:
            max = item.count
            top_word = item.word
        else:
            max = (item-1).count
            top_word = (item-1).word
        top_words.word = top_word.word
        top_words.count = max
        read_words.pop(top_words.word)


print(top_words)