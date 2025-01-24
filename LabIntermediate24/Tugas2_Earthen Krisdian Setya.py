def hangman():
    secret_word = "prasmul"
    guessed_letters = set()
    hidden_word = ["_"] * len(secret_word)
    attempts_left = 6

    while "_" in hidden_word and attempts_left > 0:
        print("\nSecret Word: ", "".join(hidden_word))
        print(f"Sisa nyawa: {attempts_left}")
        user_input = input("Masukkan huruf: ").lower()

        if not len(user_input) == 1 or not user_input.isalpha():
            print("Masukkan hanya satu huruf dan harus alfabet")
            continue

        if user_input in guessed_letters:
            print("Kamu sudah menebak huruf ini sebelumnya")
            continue

        guessed_letters.add(user_input)

        if user_input in secret_word:
            for i in range(len(secret_word)):
                if secret_word[i] == user_input:
                    hidden_word[i] = user_input
        else:
            print("Tebakanmu salah")
            attempts_left -= 1

    if "_" not in hidden_word:
        print(f"\nCongrats! Kamu sudah berhasil menebak: {secret_word}")
    else:
        print(f"\nGame over, secret wordnya adalah {secret_word}")

hangman()