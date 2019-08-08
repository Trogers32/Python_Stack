import random
def randint(min = 0, max = 100):
    if min > max:
        temp = min
        min = max
        max = temp
    max -= min
    num = random.random()
    num *= max
    num += min
    return round(num)

print(randint(20,-20))