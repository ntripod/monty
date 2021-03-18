
user_input = input("enter a word: ")
user_input = user_input.upper()
for letter in user_input:
    if letter in "AEIOU":
        continue
    print (letter)
