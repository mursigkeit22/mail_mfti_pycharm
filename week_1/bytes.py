# example_bytes = b"hello"
# print(type(example_bytes))
# print(example_bytes)
# for letter in example_bytes:
#     print(letter)
#     print(type(letter))

# num = 9
# print(f'Binary: {num:#b}')


##example2_bytes = b"привет" # ошибка. чтобы её избежать, преобразуем строку в ютф8
example2_bytes = "привет"
encoded_string = example2_bytes.encode(encoding='utf-8') # закодировали строку
print(encoded_string)
print(type(encoded_string))
for letter in encoded_string:
    print(letter, end=' ')
print()
decoded_string = encoded_string.decode() # раскодировали строку
print(decoded_string)

