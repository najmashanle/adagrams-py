from random import randint

LETTER_POOL = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3,
    'H': 2, 'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6,
    'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4,
    'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1
}

LETTER_SCORES = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10
}

def draw_letters():
    tile_bag = []
    for letter in LETTER_POOL:
        count = LETTER_POOL[letter]
        for i in range(count):
            tile_bag.append(letter)

    hand = []
    while len(hand) < 10:
        random_index = randint(0, len(tile_bag) - 1)
        tile = tile_bag.pop(random_index)
        hand.append(tile)

    return hand

def uses_available_letters(word, letter_bank):
    letters_left = letter_bank.copy()

    for letter in word.upper():
        if letter in letters_left:
            letters_left.remove(letter)
        else:
            return False

    return True

def score_word(word):
    score = 0

    for letter in word.upper():
        score += LETTER_SCORES[letter]

    if len(word) >= 7:
        score += 8

    return score

def get_highest_word_score(word_list):
    best_word = word_list[0]
    best_score = score_word(best_word)

    for word in word_list[1:]:
        score = score_word(word)

        if score > best_score:
            best_word = word
            best_score = score

        elif score == best_score:
            if len(best_word) == 10:
                continue
            elif len(word) == 10:
                best_word = word
            elif len(word) < len(best_word):
                best_word = word

    return (best_word, best_score)