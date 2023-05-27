password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"

# using lambda function and list comprehension
decrypted_password = ''.join([(lambda c: chr(ord(c) + 2) if c.isalpha() else c)(char) for char in password])
print(decrypted_password)

# using lambda function, list comprehension, and map
print(''.join(map(lambda c: chr(ord(c) + 2) if c.isalpha() else c, password)))
