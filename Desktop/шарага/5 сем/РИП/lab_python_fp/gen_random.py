import random

def gen_random(num_count, begin, end):
    rand = []
    for i in range(0, num_count):
        rand.append(random.randint(begin, end))
        # print(*rand)
    return(rand)

def main():
    print(gen_random(10, 1, 3))
    print('')
    print(gen_random(4, 5, 20))

if __name__ == "__main__":
    main()