input_text = "Total capital assets (net)                        $      4,191,448   $   4,044,748   $     137,724     $   146,304     $   4,329,172   $   4,191,052"


def process(text):
    n = 0
    capture = []
    for w in text.split('$'):
        if n == 0:
            capture.append(w.strip())
        else:
            capture.append("$" + w.strip())
        n += 1 
    return capture


assert process(input_text) == ['Total capital assets (net)', '$4,191,448', '$4,044,748', '$137,724', '$146,304', '$4,329,172', '$4,191,052']
