
int_list = tuple([int(i) for i in input().split()]) # convert to int and tuple
# int_tuple = tuple(int_list)
print(hash(int_list))

if __name__ == '__main__':
    n = int(input())
    value = list(range(1, n + 1))
    t_tuple = tuple(value)
    t = hash(t_tuple)
    print(t)
