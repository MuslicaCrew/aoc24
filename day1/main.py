input = list()

# Open the file in read mode
try:
    with open("input.txt", "r") as file:
        for line in file:
            #pass
            input.append(line.rstrip())# Use .strip() to remove leading/trailing whitespace
except FileNotFoundError:
    print("The file does not exist.")
except IOError:
    print("An error occurred while reading the file.")
# print(input)

# TESTING ONLY

#example = """3   4
#4   3
#2   5
#1   3
#3   9
#3   3""".splitlines()

# PART 1
print("Answer for part 1:")
left = list()
right = list()
for line in input:
    left.append(line.split(" ")[0])
    right.append(line.split(" ")[3])
left.sort()
right.sort()

ans = 0

for i, _ in enumerate(left):
    ans += abs(int(left[i]) - int(right[i]))

print(ans)


# PART 2
print("Answer for part 2:")
left = list()
right = list()
for line in input:
    left.append(line.split(" ")[0])
    right.append(line.split(" ")[3])
left.sort()
right.sort()

ans = 0

count = {x: right.count(x) for x in left}

for n in left:
    ans += count[n] * int(n)

print(ans)
