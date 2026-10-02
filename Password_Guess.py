import random #noqa

easy_words = ['apple' , 'banana', 'grape', 'orange', 'peach', 'pear',]
medium_words = ['planet', 'laptop', 'coconut', 'python', 'bottle', 'monkey']
hard_words = ['computer', 'programming', 'umbrella', 'function', 'variable', 'mountain']

print ("Welcome to the Password Guessing Game!")
print ("You have to guess the password based on the difficulty level you choose.")

difficulty = input("Choose difficulty level (easy, medium, hard): ").lower()

if difficulty == "easy":
    password = random.choice(easy_words)
elif difficulty == "medium":
    password = random.choice(medium_words)
elif difficulty == "hard":
    password = random.choice(hard_words)
else:
    print("Invalid choice. Setting the default difficulty level to easy.")
    password = random.choice(easy_words)

attempt = 0

while True:
    guess = input("Guess the password: ")
    attempt += 1
    if guess == password:
        print(f"Congratulations! You guessed the password correctly in {attempt} attempts.")
        break
    else:
        hint = ""
        for i in range(len(password)):
            if i < len(guess) and guess[i] == password[i]:
                hint += guess[i]
            else:
                hint += "_"
        print(f"Hint: {hint}")
print ("Game Over")