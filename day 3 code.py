import random

# simple probability dictionary (fake trained knowledge)
language_model = {
    "i": ["am", "like", "want"],
    "am": ["learning", "hungry", "happy"],
    "learning": ["ai", "python", "machine"],
    "machine": ["learning"],
    "learning": ["is"],
    "is": ["fun", "powerful", "useful"]
}

def generate_text(start_word, length=10):
    word = start_word.lower()
    sentence = [word]

    for _ in range(length):
        if word in language_model:
            next_word = random.choice(language_model[word])
            sentence.append(next_word)
            word = next_word
        else:
            break

    return " ".join(sentence)

# run demo
print(generate_text("I"))
