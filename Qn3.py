# Write a Python function that checks whether a word or phrase is palindrome or
# not.

def is_pangram(text):
    text = text.lower()
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return all(letter in text for letter in alphabet)
def main():
    print("Pangram:")
    print(is_pangram("The quick brown fox jumps over the lazy dog"))
    print(is_pangram("hello world"))
if __name__ == "__main__":
    main()