# #a = [1, 2, 3, 4, 5, 6, 7, 7, 5, 4, 8, 4]
# a = set(i for i in input().split())
# print(len(a))

a = [int(a) for a in input().split()]
k = int(input())
for i in range(k):
    a.insert(0, a.pop())
print(a)
