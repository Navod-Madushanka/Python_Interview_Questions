# try:
#     file = open("a_text.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["seoifjrwo"])
# except FileNotFoundError:
#     file = open("a_text.txt", "w")
#     file.write("Something")
# except KeyError as error:
#     print(f"The key call {error} is not found")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("file was closed")


fruits = ["Apple", "Pear", "Orange"]


# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    fruit = fruits[index]
    print(fruit + " pie")


try:
    make_pie(4)
except IndexError:
    print("Fruit pie")
