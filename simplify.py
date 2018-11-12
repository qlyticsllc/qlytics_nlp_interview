text = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way-in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only."


def is_valid(text, portion):
    sequence = ''
    for c in text:
        sequence += c
        if len(sequence) == len(portion):
            if sequence == portion:
                return True
            sequence = sequence[1:]
    return False


def capture_text():
    sequence = ''
    capture = False
    captured = []
    for c in text:
        sequence += c
        if (capture and
            sequence.endswith(', ')):
            capture = False
            captured.append(sequence[:-2])
            sequence = ''
        if is_valid(sequence.lower(), 'it was the '):
            sequence = ''
            capture = True
    filtered = []
    for entry in captured:
        sequence = ''
        capture = False
        for c in entry:
            if is_valid(sequence, ' of '):
                sequence = ''
                if c not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    capture = True
            sequence += c
        if (capture and
            sequence not in captured):
            filtered.append(sequence)
    return filtered

