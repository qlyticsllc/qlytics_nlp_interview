input_text = "Total capital assets (net)                        $      4,191,448   $   4,044,748   $     137,724     $   146,304     $   4,329,172   $   4,191,052"


def process(text):
    words = [
        word.strip() if i == 0 else '$' + word.strip()
        for i, word in enumerate(text.split('$'))
    ]
    return words


assert process(input_text) == [
    'Total capital assets (net)', '$4,191,448', '$4,044,748', '$137,724',
    '$146,304', '$4,329,172', '$4,191,052'
]
