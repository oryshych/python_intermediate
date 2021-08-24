# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# with open("my_file.txt", mode="a") as file:
#     file.write("\nNext text")

# with open("/Users/A & A/Desktop/new_file.txt", mode="w") as file:
#     file.write("Next text new ")

with open("../../Desktop/new_file.txt") as file:
    contents = file.read()
    print(contents)