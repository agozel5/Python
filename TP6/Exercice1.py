L1 = [0]*3

print(L1)
print(type(L1))
print(id(L1))

for i in range(len(L1)):
    print(f"Type of element at index {i}: {type(L1[i])}")
    print(f"Id of element at index {i}: {id(L1[i])}")

L1[1] += 1

print(L1)
print(type(L1))
print(id(L1))

for i in range(len(L1)):
    print(f"Type of element at index {i}: {type(L1[i])}")
    print(f"Id of element at index {i}: {id(L1[i])}")
