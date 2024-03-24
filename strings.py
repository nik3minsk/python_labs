



val = int(input("Enter qt val: "))
ranges = []

for i in range(val):
    range = int(input("Enter range: "))
    ranges.append(range)
print(len(ranges))
k = int(len(ranges))

# if hasattr(len(ranges), '__iter__'):
#     print("Этот объект итерируемый")
# else:
#     print("Этот объект не итерируемый")

j=1
for element in ranges:
    print("Значение", j, ":", element)
    j += 1

# for i in range(len(ranges)):
#     print("Значение", i + 1, ":", ranges[i])