from itertools import groupby

output = dict()
for key, group in groupby(input("Enter list: ")):
    # print(f"group: {list(group)} and key: {key}")
    # print(f"group: {len(list(group))} and key: {key}")
    print(f"({len(list(group))}, {key})")
