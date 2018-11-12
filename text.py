input_text = "Total capital assets (net)                        $      4,191,448   $   4,044,748   $     137,724     $   146,304     $   4,329,172   $   4,191,052"


def process(text):
    entries = [entry.strip() for entry in text.split('$')]
    for idx, entry in enumerate(entries[1:]):
        entries[idx + 1] = '${}'.format(entry)
    return entries


assert process(input_text) == ['Total capital assets (net)', '$4,191,448', '$4,044,748', '$137,724', '$146,304', '$4,329,172', '$4,191,052']
