import pdb

pdb.set_trace()

def get_greater_numbers(list_of_lists):
    greater_numbers = [x for lst in list_of_lists for x in lst if x == max(lst)]
    return greater_numbers


def get_prime_number(number):
    for n in range(2, int(number ** 0.5) + 1):
        if number % n == 0:
            return False
    return True


if __name__ == '__main__':
    list_of_lists = [[2, 4, 1], [1, 2, 3, 4, 5, 6, 7, 8], [100, 250, 43]]
    greater_numbers = get_greater_numbers(list_of_lists)
    print(greater_numbers)

    list_of_number = [3, 4, 8, 5, 5, 22, 13]
    prime_numbers = filter(get_prime_number, list_of_number)
    print(list(prime_numbers))
