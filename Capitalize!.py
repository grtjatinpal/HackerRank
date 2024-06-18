def solve(string):
    for word in string.split():
        string = string.replace(word, word.capitalize())
    return string


if __name__ == "__main__":
    string = input()
    # result = solve(string)
    result = solve(string)
    print(result)


# q w e r t y u i o p a string d f g h j  k l z word c v b n m Q W E R T Y U I O P A string D F G H J  K L Z word C V B N M
