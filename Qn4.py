# Write a program that takes an integer as input and returns an integer with
# reversed digit ordering.

def reverse_number(number):
    num_str = str(number)
    if num_str[0] == '-':
        return -int(num_str[1:][::-1])
    else:
        return int(num_str[::-1])
def main():
    print("Reversed Number:")
    print(reverse_number(500))
    print(reverse_number(-56))
    print(reverse_number(-90))
    print(reverse_number(91))
if __name__ == "__main__":
    main()