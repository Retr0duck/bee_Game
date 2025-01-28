WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 4, "GRAPHIC": 7}

def main():
    print("Welcome to Spelling bee!")
    print("Your letters are: A I P C R H G")
    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left!")
        guess = input("Guess a word: ")
        if guess == "GRAPHIC":
            WORDS.clear()
            print("You've won!")
        if guess in WORDS.keys():
            points = WORDS.pop(guess)
            print(f"Good job! You scored {points} points.")
        print("That's the game")

# A simple way to get the words and values is this.
"""
for words, values in WORDS.items():
    print(f"It's okay here is the {words} and {values}")
"""
    


main()