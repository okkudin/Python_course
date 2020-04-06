# create function input file name output array top3
# read file mandatory_tasks_session_4_lorem_ipsum.txt
# search for all words in file
# count frequency all words
# sort and top3

def top3(file_name):
    file = open(file_name, "r")
    text = file.read()
    text = text.replace(".", "").replace(",", "").replace("\n", " ").lower()
    words = text.split(" ")
    #print(words)

    result = {}
    for word in words:
        w = result.get(word)
        if w is None:
            result[word] = 1
        else:
            result[word] += 1
    #print(result.items())

    result = sorted(result.items(), key=lambda item: item[1], reverse=True)
    final_result = result[:3]
    final = map(lambda item: item[0], final_result)
    print(list(final))

top3("mandatory_tasks_session_4_lorem_ipsum.txt")