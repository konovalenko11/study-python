def strip_punctuation(text):
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

    for char in punctuation_chars:
        text = text.replace(char, '')

    return text


print(strip_punctuation('!@Amaz,on#'))

