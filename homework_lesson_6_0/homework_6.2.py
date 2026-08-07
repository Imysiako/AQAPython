word = input("Please enter the word with 'h':")
while 'h' not in word.lower():
    print("The word doesn't contain 'h'.")
    word = input("Please enter the word with 'h':")
print("Thank you. That's correct.")
