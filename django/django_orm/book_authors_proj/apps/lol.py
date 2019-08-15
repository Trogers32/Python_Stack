import random

switch_Dict = {
    1:"H",
    2:"e",
    3:"l",
    4:"l",
    5:"o",
    6:" ",
    7:"w",
    8:"o",
    9:"r",
    10:"l",
    11:"d",
    12:"!",
}
hell = ""
while hell != "Hello world!":
    hello = []
    wow = []
    while len(hello) != 12:
        lol = random.randint(1,12)
        counter = 0
        temp_letter = switch_Dict[lol]
        for numbers in wow:
            if numbers == lol:
                counter += 1
        if counter == 0:
            wow.append(lol)
            hello.insert(lol, temp_letter)
    hell = ""
    hell = hell.join(hello)
print(hell)

