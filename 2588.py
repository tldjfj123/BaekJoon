a = input()
b = input()


new1 = int(a)
new2 = list(b)

l3 = new1 * int(new2[-1])
l4 = new1 * int(new2[-2])
l5 = new1 * int(new2[-3])


sum = l5 * 100 + l4 * 10 + l3

print(l3)
print(l4)
print(l5)
print(sum)