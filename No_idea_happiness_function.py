# user input list
def user_input(number_of_elements):
    user_list = []
    for i in range(number_of_elements):
        user_list.append(int(input(f"Element {i+1}: ")))

    return user_list


def create_set():
    _set = set(map(int, input("Enter set all elements: ").split()))
    return _set


def calculate_happiness(happiness: set, sadness: set, user_list):
    happiness = 0
    for num in user_list:
        if num in setA:
            happiness += 1
        if num in setB:
            happiness -= 1

    print(f"Happiness: {happiness}")


if __name__ == "__main__":

    # n is user input list size and m is number of set
    # number_of_elements, number_of_set = map(int, input().split())
    no_of_elements_main_set = int(input("Enter the Main elements Size: "))
    nnumber_of_set = int(input("Enter the number of set: "))

    # user input list
    # user_list = list(map(int, input().split()))
    user_list = user_input(no_of_elements_main_set)

    # set A is happiness
    setA = create_set()

    # set B is sadness
    setB = create_set()

    calculate_happiness(setA, setB, user_list)
