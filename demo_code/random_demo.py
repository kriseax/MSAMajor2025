import random

def main():
    
    #create a random number generator
    random_generator = random.Random()
    print(random_generator.randint(0, 100))


    #generate 20 random numbers
    print("Generate 20 random numbers")
    for _ in range(20):
        print(random_generator.randint(10, 99))


main()