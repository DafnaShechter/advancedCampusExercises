def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    translated_sentence = ' '.join(words.get(word, word) for word in sentence.split())
    return translated_sentence


# Test the translate function
print(translate("el gato esta en la casa"))
