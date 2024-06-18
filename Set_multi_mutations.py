def perform_operations(set_a, operation, new_set):
    if operation == 'intersection_update':
        set_a.intersection_update(new_set)
    elif operation == 'update':
        set_a.update(new_set)
    elif operation == 'symmetric_difference_update':
        set_a.symmetric_difference_update(new_set)
    elif operation == 'difference_update':
        set_a.difference_update(new_set)
    
    return set_a

Number_of_elements = int(input("Number of elements in Set A"))
SET_A = set(map(int, input().split()))
num_of_New_sets = int(input())

for _ in range(num_of_New_sets):
    operation, length = input("Enter operation and length separated by space: ").split()
    new_set = set(map(int, input().split()))
    SET_A = perform_operations(SET_A, operation, new_set)
    # perform_operations(SET_A, operation[0], new_set)
    # eval('SET_A.{}({})'.format(operation[0], new_set))

print(sum(SET_A))
# intersection_update 10