secret_word = "prasmul"

print(f"Tebak huruf dari kata yang memiliki {len(secret_word)} huruf")

for i in range(len(secret_word)):
    while True:
        answer = input(f"Masukkan huruf ke-{i+1}: ").lower()
        
        if len(answer) == 1 and answer.isalpha():
            break
        else:
            print("Masukkan hanya satu huruf")
    if answer == secret_word[i]:
        print("Correct")
    else:
        print("False")