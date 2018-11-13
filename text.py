input_text = "Total capital assets (net)                        $      4,191,448   $   4,044,748   $     137,724     $   146,304     $   4,329,172   $   4,191,052"

def process(text):
    result = []
    phrases = text.split('$')
    for i in range(0,len(phrases)):
        if i == 0:
            result.append(phrases[i].strip(' '))
        else:
            result.append("$"+phrases[i].strip(' '))
    return result

assert process(input_text) == ['Total capital assets (net)', '$4,191,448', '$4,044,748', '$137,724', '$146,304', '$4,329,172', '$4,191,052']
