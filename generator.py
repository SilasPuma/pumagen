import random
import string

def generate_code():
    while True:
        code = "X" + ''.join(random.choices(string.ascii_uppercase, k=15))
        if sum(c.isalpha() for c in code) > sum(c.isdigit() for c in code):
            return code

def main():
    num_codes = int(input("How many Apple codes would you like to generate? "))

    codes = [generate_code() for _ in range(num_codes)]

    with open("generated_codes.txt", "w") as file:
        for code in codes:
            file.write(code + "\n")

    print("Codes have been generated and saved to apple.txt.")
    print("Run validator.py to check your codes!")

if __name__ == "__main__":
    main()
