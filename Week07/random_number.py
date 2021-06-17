import random


def append_random_numbers(numbers_list, quantity=1):
    for i in range(quantity):
        random_number = round(random.uniform(1, 100), 1)
        # random_number = f"{random_number:.1f}"
        numbers_list.append(random_number)

    

def main():
    randnums = [16.2, 75.1, 52.3]
    print(randnums)

    append_random_numbers(randnums)
    print(randnums)
    
    append_random_numbers(randnums, 3)
    print(randnums)


# Call the main function
main()