from random import randint

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

def draw_letters(): 
    # Create expanded list of letters based on frequency
    letter_bank = []
    for letter, frequency in LETTER_POOL.items():
        for _ in range(frequency):
            letter_bank.append(letter)
    
    # Draw 10 random letters
    letters = [] # changed variable from drawn_letters to letters
    for _ in range(10):
        index = randint(0, len(letter_bank) - 1) # get a random index
        letters.append(letter_bank.pop(index)) # append the letter
    
    print(f"Drawn letters: {letters}") # check output
    return letters        

def uses_available_letters(word, letters):
    for letter in word: 
        if word.count(letter) > letters.count(letter):
            return False
    return True 
        

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass