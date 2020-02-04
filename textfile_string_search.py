## This script splits each line into a list and searches for the substring


file = open('filename.txt', 'r')
lines = file.readlines()
file.close()

substring = 'is'

print(f'Search the text for the following string: {substring}')
print()
total = 0
linenum= 0
for line in lines:
    linenum += 1
    line = line.split()
    count = line.count(substring)
    total += count
    print(f'The count in line {linenum} is:', count)

print()
print(f'Total number of occurrences is:', total)
