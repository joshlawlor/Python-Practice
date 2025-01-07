import random

def random_value():
    return random.randint(1, 3)

if __name__ == '__main__':
    x = random_value()
    y = random_value()
    z = random_value()
    n = random_value()
    
    print(x, y, z, n)