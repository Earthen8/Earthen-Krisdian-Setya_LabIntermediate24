def update_text(word, hidden, guess):
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                hidden[i] = guess
        print(f"Congrats! '{guess}' is in the secret word!")
    else:
        print(f"'{guess}' is not in secret word")

def hangman(word):
    hidden, guessed, attempt = ['_'] * len(word), set(), 6
    while '_' in hidden and attempt > 0:
        print("\nWord: " + " ".join(hidden))
        print(f"Sisa nyawa: {attempt}")
        guess = input("Tebak kata: ").lower()
        
        if guess in guessed or not guess.isalpha() or len(guess) != 1:
            print("Invalid input")
            continue
        
        guessed.add(guess)
        update_text(word, hidden, guess)
        
        if guess not in word:
            attempt -= 1
    
    print(f"\nCongrats! Jawabannya adalah '{word}'" 
          if '_' not in hidden else
            f"\nGame over! Jawabannya adalah '{word}'")

hangman("prasmul")