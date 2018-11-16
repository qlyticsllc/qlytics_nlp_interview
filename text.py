input_text = "Total capital assets (net)                        $      4,191,448   $   4,044,748   $     137,724     $   146,304     $   4,329,172   $   4,191,052"


def process(text):
    splits = text.split('$')
    result = []
    for i, s in enumerate(splits):
        s = s.strip()
        if i == 0:
            result.append(s)
        else:
            result.append('$'+s)
    return result


assert process(input_text) == ['Total capital assets (net)', '$4,191,448', '$4,044,748', '$137,724', '$146,304', '$4,329,172', '$4,191,052']
