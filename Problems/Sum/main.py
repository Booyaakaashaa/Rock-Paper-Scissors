# read sums.txt
# read sums.txt
s = open('sums.txt', 'r')
for line in s:
    a, b = line.strip().split()
    print(int(a) + int(b))
s.close()
