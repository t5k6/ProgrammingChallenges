from hashlib import md5

# Range value ( limit ) is arbitrary, increase it if the answer returns as None
# zeroes is the leading zeroes

def secret(secret_key, limit, zeroes):
    for num in range(limit):
        digest = md5((secret_key + str(num)).encode())
        result = digest.hexdigest()
        if result.startswith(str(zeroes)):
            # print(result)
            return str(num)

print("Problem 1:\t {}".format(secret("bgvyzdsv", 1000000, "00000")))
print("Problem 2:\t {}".format(secret("bgvyzdsv", 10000000, "000000")))
