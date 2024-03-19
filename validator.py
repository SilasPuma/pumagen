import aiohttp
import asyncio

async def check_app_store_code(session, code):
    url = f"https://buy.itunes.apple.com/verifyReceipt?receipt={code.strip()}"
    async with session.post(url) as response:
        if response.status == 200:
            return code.strip()

async def check_app_store_codes(codes):
    valid_codes = []

    async with aiohttp.ClientSession() as session:
        tasks = [check_app_store_code(session, code) for code in codes]
        for result in asyncio.as_completed(tasks):
            valid_code = await result
            if valid_code:
                valid_codes.append(valid_code)
                print(f"Valid code: {valid_code}")

    return valid_codes

# Read codes from apple.txt
with open("apple.txt", "r") as file:
    codes_to_check = file.readlines()

# Check the validity of codes
valid_codes = asyncio.run(check_app_store_codes(codes_to_check))

# Write valid codes to apple-valid.txt
with open("apple-valid.txt", "w") as file:
    file.write("\n".join(valid_codes))

print("Valid codes have been saved to apple-valid.txt")
