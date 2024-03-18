import requests

def check_app_store_codes(codes):
    valid_codes = []
    invalid_codes = []

    for code in codes:
        url = f"https://buy.itunes.apple.com/verifyReceipt?receipt={code.strip()}"
        response = requests.post(url)
        if response.status_code == 200:
            valid_codes.append(code)
        else:
            invalid_codes.append(code)

    return valid_codes

# Read codes from apple.txt
with open("apple.txt", "r") as file:
    codes_to_check = file.readlines()

# Check the validity of codes
valid_codes = check_app_store_codes(codes_to_check)

# Write valid codes to apple-valid.txt
with open("apple-valid.txt", "w") as file:
    file.write("\n".join(valid_codes))

print("Valid codes have been saved to apple-valid.txt")
