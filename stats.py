def count_words(text):
    return len(text.split())
 
def count_characters(text):
    char_counts = {}
    for ch in text.lower():
        if ch in char_counts:
            char_counts [ch] += 1
        else:
            char_counts[ch]=1
    return char_counts

def structure (char_counts):
    filter = {ch: count for ch, count in char_counts.items() if ch!= ' '}
    return sorted(filter.items(), key=lambda item: item[1], reverse=True)      







