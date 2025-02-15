import random

words = ["prasmul", "samsung", "iphone", "hangman"]
wins, loss = 0, 0

def update_text(word, hidden, guess):
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                hidden[i] = guess
        print(f"Congrats! '{guess}' is in the secret word!")
    else:
        print(f"'{guess}' is not in secret word")

def hangman():
    global wins, loss
    while words:
        word = random.choice(words)
        words.remove(word)
        hidden, guessed, attempts = ["_"] * len(word), set(), 6

        while "_" in hidden and attempts > 0:
            print("\nWord: " + " ".join(hidden))
            print(f"Sisa nyawa: {attempts}")
            guess = input("Tebak kata: ").lower()

            if guess in guessed or not guess.isalpha() or len(guess) != 1:
                print("Invalid input")
                continue

            guessed.add(guess)
            update_text(word, hidden, guess)

            if guess not in word:
                attempts -= 1

        if "_" not in hidden:
            wins += 1
            print(f"\nCongrats! Jawabannya adalah '{word}'")
        else:
            loss += 1
            print(f"\nGame over! Jawabannya adalah '{word}'")

        print(f"Score: {wins} Menang, {loss} Kalah")
        if input("Main lagi? (yes/no): ").lower() != "yes":
            print(f"Final Score: {wins} Menang, {loss} Kalah")
            break

hangman()