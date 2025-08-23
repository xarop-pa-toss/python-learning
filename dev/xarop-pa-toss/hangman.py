 print("Welcome to Guessing Game 2.0\n")
name = input("What's your name: ")

print(f"Hello {name}, good luck for you! ")

words = ["Apple", "Banana", "Chair", "Window", "Ocean", "Cloud", "Tiger", "Guitar", "Castle", "Robot",
    "Candle", "Bridge", "Pizza", "Moon", "Elephant", "Rainbow", "Mountain", "Camera", "Dragon", "Spider",
    "Balloon", "Treasure", "Laptop", "Airplane", "Clock", "Chocolate", "Mirror", "Diamond", "Jellyfish", "Volcano",
    "Forest", "Book", "Pencil", "Train", "Circus", "Pirate", "Snowman", "Rocket", "Turtle", "Starfish",
    "Iceberg", "Blanket", "Unicorn", "Sandwich", "Desert", "Castle", "Bottle", "Magic", "Planet", "Butterfly",
    "Crown", "Ghost", "Hammer", "Radio", "Witch", "Soap", "Flower", "Cloud", "Ring", "Cookie",
    "Shark", "Doctor", "Monster", "Lion", "Key", "Garden", "Treasure", "Phone", "Backpack", "Candle",
    "Pizza", "Camera", "Banana", "Balloon", "Ice cream", "Ladder", "Hospital", "Jelly", "Shadow", "King",
    "Queen", "Chess", "Circus", "Wizard", "Cave", "Clock", "Bread", "Tower", "Cave", "Tent",
    "Sword", "Candy", "Storm", "Whale", "Bridge", "Piano", "Mountain", "River", "Treasure", "Castle"]

word = random.choice(words)

guessed_letters = []
guess_limit = 12

while guess_limit > 0:
    guess = input("Guess the characters: ")

    if guess in word:
        guessed_letters.append(guess)
    
    for char in word:
        if char in guessed_letters:
            print(char)
        else:
            print("_")
