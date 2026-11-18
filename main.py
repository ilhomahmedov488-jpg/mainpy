
# 1.
# def min_of_three(a,b,c):
#     if a<b and a<c:
#         return a
#     elif b<a and b<c:
#         return b

#     elif c<a and c<b:
#         return c
# print(min_of_three(7, 2, 5))


# 2

# def power(a,b):
#     if b==1:
#         return a
#     return power(a,b-1)*a
# print(power(2, 5))


# 3
# def count_digits(b):
#     if b==0:
#         return 0
#     return count_digits(b//10)+1

# print(count_digits(75869))

# 4.
# def sum_of_cubes(a,b):
#     def cube(x):
#         return x**3
#     return cube(a)+cube(b)
# print(sum_of_cubes(2, 3))

# 5.
# def make_adder(a):
#     def inner(b):
#         return a+b
#     return inner

# add5 = make_adder(5)
# add10 = make_adder(10)
# print(add5(3))
# print(add10(3))

# 6. 
# def make_accumulator():
#     a=0
#     def inner(b):
#         nonlocal a
#         a=a+b
#         return a
#     return inner
# acc = make_accumulator()
# print(acc(10))
# print(acc(5))
# print(acc(20))

# 7. 
# def exclaim(func):
#     def inner():
#         res=func()
#         return res+"!"
#     return inner
# @exclaim
# def greet():
#     return "Salom"

# print(greet())



# 8.
# def log_result(func):
#     def inner(a,b):
#         res=func(a,b)
#         print(f"multiply returned {func(a,b)}")
#         print(func(a,b))
#     return inner
# @log_result
# def multiply(a, b):
#     return a * b

# (multiply(3, 4))


# 9.
# def count_vowels(ch):
#     cnt=0
#     a="aoiue"
#     for i in ch:
#         def is_lowel(i):
#             if i in a:
#                 return True
#             else:
#                 return False
#         if is_lowel(i):
#             cnt+=1
#     return cnt
        

# print(count_vowels("programming"))

# 10.
# def sort_by_grade(*s):
#     s=sorted(s,key=lambda x:x[1],reverse=True)
#     return s
# print(sort_by_grade(("Ali", 85), ("Vali", 92), ("Sara", 78)))