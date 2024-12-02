# Write a program that accepts a string as input, capitalizes the first letter of each
# word in the string, and then returns the result string.

def capitalize_words(text):
    words = text.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)
def main():
    print("Capitalized Words:")
    print(capitalize_words("hi"))
    print(capitalize_words("i love programming"))
if __name__ == "__main__":
    main()