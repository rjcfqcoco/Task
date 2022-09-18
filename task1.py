# # def cube(n):
# #     return n**3
# # number = int(input("Please enter number: "))
# #
# # kup = cube(number)
# #
# # print("CUbe of number is {0} = {1}".format(number,kup))
#
# list1 = [10,20,30,40,50]
# length = len(list1) - 1
# for i in range(length, -1, -1):
#     print(list1[i])
#
# def fact(n):
#     return 1 if (n == 1 or n == 0) else n * fact(n-1)
# num = int (input("Number: "))
# print ("factorial off {0} = {1}". format(num, fact(num)))

# sum = 0
# n = int(input("Your Nmber PLease: "))
#
# for i in range (1, n+1, 1):
#     sum += i
# print("Sum is: ", sum)

# def checkPalin(self, x: int) -> bool:
#     s = str(x)
#
#     if len(s) == 1:
#         palin = True
#
#     i = int(len(s)/2)
#
#     for p in range(i):
#         if s[p] != s[-(p+1)]:
#             return False
#         else:
#             palin = True
#
#     return palin

# n = int(input("1num: "))
# k = int(input("2num: "))
#
# for i in range(0,n+1):
#     for j in range(k-i,0,-1):
#         print(j,end=' ')
#     print()

# n = int(input("row count:"))
# for i in range (1, n+1, 1):
#     for j in range(1, i + 1):
#         print (j, end = ' ')
#     print()

# def sum(n):
#     if n <= 1:
#         return n
#     return n + sum(n-1)
# n = int(input("Number: " ))
#
# print(sum(n))

