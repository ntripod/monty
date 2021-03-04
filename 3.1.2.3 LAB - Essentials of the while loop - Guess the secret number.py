secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
guess_number = int(input("Enter your guess: "))
while guess_number != secret_number:
    print("No it's not this one. Find it to escape the loop")
    guess_number = int(input("Enter your guess: "))
print("You found it! I am amazed")
