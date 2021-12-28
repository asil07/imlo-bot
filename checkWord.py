from uzwords import words
from difflib import get_close_matches


def checkWord(word, words=words):

    word = word.lower()
    matches = set(get_close_matches(word, words))
    mavjud = False

    if word in matches:
        mavjud = True
        matches = word
    elif "ҳ" in word:
        word = word.replace("ҳ", "х")
        matches.update(get_close_matches(word, words))
    elif "х" in word:
        word = word.replace("х", "ҳ")
        matches.update(get_close_matches(word, words))

    return {"mavjud": mavjud, "so'zlar": matches}

if __name__ == "__main__":
    print(checkWord("хатот"))





