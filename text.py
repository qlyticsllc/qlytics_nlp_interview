import nltk

nltk.download('punkt')

input_text = "Total capital assets (net)                        $      4,191,448   $   4,044,748   $     137,724     $   146,304     $   4,329,172   $   4,191,052"

def split(arr, size):
    arrs = []
    while len(arr) > size:
        pice = arr[:size]
        arrs.append(pice)
        arr = arr[size:]
    arrs.append(arr)
    return arrs

def process(text):
    result = []
    split_sentences = text.split("                        ")
    if len(split_sentences) > 0:
        result.append(split_sentences[0])
    if len(split_sentences) > 1:
        words = nltk.word_tokenize(split_sentences[1])

        values = split(words, 2)
        for value in values:
            result.append("".join(value))

    return result


assert process(input_text) == ['Total capital assets (net)', '$4,191,448', '$4,044,748', '$137,724', '$146,304', '$4,329,172', '$4,191,052']
