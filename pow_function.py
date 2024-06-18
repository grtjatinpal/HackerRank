# Input
base = int(input())
expo = int(input())
mod = int(input())


# print(base**expo)
print(pow(base, expo))

# print(base**expo % mod)
print(pow(base, expo, mod))

result = pow(base, expo) + pow(base, expo)
print(result)