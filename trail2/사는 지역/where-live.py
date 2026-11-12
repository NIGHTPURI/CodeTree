n = int(input())
name = []
address = []
region = []

p = []

for _ in range(n):
    name_value, address_value, region_value = input().split()
    name.append(name_value)
    address.append(address_value)
    region.append(region_value)

for i in range(n):
    p.append((name[i],address[i],region[i]))

p.sort()
print(f"name {p[-1][0]}")
print(f"addr {p[-1][1]}")
print(f"city {p[-1][2]}")


# Please write your code here.
