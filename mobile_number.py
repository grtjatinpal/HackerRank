def wrapper(f):
    def fun(l):
        print(f"+91 {f[-10:-5]} {f[-1:-5]}")
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

