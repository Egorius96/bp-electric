n = int(input("enter a num: "))
binary_8 = format(n, "b").zfill(8)
print("in binary form:", binary_8)
print("task result in binary:", binary_8[-4:] + binary_8[:4])
print("task result in int:", int(binary_8[-4:] + binary_8[:4], 2))
