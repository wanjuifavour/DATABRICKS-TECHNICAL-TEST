# Write a Python function that checks whether a word or phrase is palindrome or
# not.

def is_palindrome(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]
def main():
    print("Palindrome:")
    print(is_palindrome("madam"))
    print(is_palindrome("nurses run"))
    print(is_palindrome("hello"))
if __name__ == "__main__":
    main()