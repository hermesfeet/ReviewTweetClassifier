#Given a sorted array of positive integers with an empty spot (zero) at the end, insert an element in sorted order.


list = [1,3,5,9]

index = len(list) - 1

print(index)

num = 7

for item in range(0, index):
    if (num > list[item]) & (num < list[item+1]):
        list.insert(item+1, num)

print(list)


# 16.2 Reverse the order of elements in an array (without creating a new array).

listy = [1,3,5,9]

index = len(listy) - 1
iterate_half = int(index/2)

for item in range(0, iterate_half):
    a = listy[item]
    listy[item] = listy[index-item]
    listy[index-item] = a

print(listy)

#Given two lists (A and B) of unique strings, write a program to determine if A is a subset of B.
# That is, check if all the elements from A are contained in B.

A = ["dog", "cat", "man", "gruto"]
B = ["dog", "cat", "man", 'love', "fragg"]

dicter = {}

for item in B:
    dicter[item] = item

print(dicter)

for item in range(0,len(A)):
    word = A[item]
    if word == dicter[word]:
        print('yes ' + word)
    else:
        print("no")