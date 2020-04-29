# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

phonbook = {}
for num in range(0, n, 1):
    try:
        x, y = [str(x) for x in input().split()]
        phonbook[x] = y
    except:
        break

query = list(input.split())

for num in range(0, len(query), 1):
    x = query[num]
    try:
        print(x+"="+phonbook[x])
    except:
        print("Not found")
