text = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way-in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only."


def capture_text():
    startswith = 'it was the '
    captured = [entry[len(startswith):] for entry in text.split(', ') if entry.lower().startswith(startswith)]
    filtered = []
    for entry in captured:
        s = entry.split(' of ')[1]
        if s[0] not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' and s not in captured:
            filtered.append(s)
    return filtered

