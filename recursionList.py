#!/usr/bin/python3.6
# Write recursive function which will calculate sum of all digits in this
# list: [[[ [1, 4, 5], [[6, 9],[[[8, 1], 7], 3], 2], 7], 5, 2], 9, [1, 2]]


list_ = [[[[1, 4, 5], [[6, 9], [[[8, 1], 7], 3], 2], 7], 5, 2], 9, [1, 2]]

def test_me(list_):
    sum_list = list()

    def test_me_(lst):
        for i in lst:
            if isinstance(i, list):
                test_me_(i)
            else:
                sum_list.append(i)

    test_me_(list_)

    return sum(sum_list)
