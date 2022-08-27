import random

print("\nPassword Generator")

# Ask user for number of letters, symbols and numbers
nr_letters = int(input("\nHow many letters would you like in your password?\n"))
nr_symbols = int(input("\nHow many symbols would you like?\n"))
nr_numbers = int(input("\nHow many numbers would you like?\n"))

# Create empty list
password = []

# Create list of letters, symbols and numbers
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

# Add letters, symbols and numbers to password list
for letter in range(1, nr_letters + 1):
    password.append(random.choice(letters))

for symbol in range(1, nr_symbols + 1):
    password.append(random.choice(symbols))

for number in range(1, nr_numbers + 1):
    password.append(random.choice(numbers))

# Shuffle password list
random.shuffle(password)

# Convert list to string
password = "".join(password)

# Print password string
print(f"\nYour password is: {password}\n")
