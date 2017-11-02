list_ = [[[[1, 4, 5], [[6, 9], [[[8, 1], 7], 3], 2], 7], 5, 2], 9, [1, 2]]

def test_me(list_):
    sum_list = list()
    for i in list_:
        if isinstance(i, list):
           sum_list.append(test_me(i))
        else:
            sum_list.append(i)

    return sum(sum_list)


print(test_me(list_))


# Good idea but recursive means it
# is calling itself not creating new
# function and calling it (you created a closure by the way).
# So please remove inner function
# (just remove definition and usage - lines 3 and 10)
# and in line 6 try append result of test_me(i)
# to sumlist. Uncommitting so you could update.


#!/usr/bin/python3.6
# Write recursive function which will calculate sum of all digits in this
# list: [[[ [1, 4, 5], [[6, 9],[[[8, 1], 7], 3], 2], 7], 5, 2], 9, [1, 2]]
# def test_me(list_):
#     sumlist = list()
#     def test_me_(lst):
#         for i in lst:
#             if isinstance(i, list):
#                 test_me_(i)
#             else:
#                 sumlist.append(i)
#
#     test_me_(list_)
#
#     return sum(sumlist)