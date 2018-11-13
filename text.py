import re

input_text = "Total capital assets (net)                        $      4,191,448   $   4,044,748   $     137,724     $   146,304     $   4,329,172   $   4,191,052"


def process(text):
    temp_list = list(reversed(re.split(r'\s+(\$)', text)))
    new_list = []
    while len(temp_list) > 0:
        el = temp_list.pop()
        new_el = el.strip()
        if new_el == '$':
            el = temp_list.pop()
            next_el = el.strip()
            new_el += next_el
        new_list.append(new_el)
    return new_list


assert process(input_text) == ['Total capital assets (net)', '$4,191,448', '$4,044,748', '$137,724', '$146,304', '$4,329,172', '$4,191,052']
