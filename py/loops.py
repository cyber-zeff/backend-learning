# for
arr = [1,2,3,4,5]
for x in arr:
    print(x)

for x in range(10):
    # * a better approach: print(f"{x = }")
    print(x)

points = [(1,2), (3,4), (5,6)]
for x,y in points:
    print(f"{x = } and {y = }")