# You are given with a list with strings. You need to return list with modified strings:
#
# • first character is removed
#
# • next character is removed if it is vowel("a", "e", "o", "i", "u", "y")
#
# • added "shwa" to the beginning
#
# • added " " (space) to the end
#
# • added length of original string to the end
#
#
#
# Example:
#
# apple -> shwapple 5
#
# banana ->  shwanana 6
#
# tractor ->  shwaractor 7
#
# ["garik", "balkon"] ->  ["shwarik 5", "shwalkon 6"]


#!/usr/bin/env python3
test_strings = ["kawabunga", "metro2013", "moon", "orange"]
tmp = test_strings[:]

def shwalengthimter(test_strings):

    def removefirstchar(lst):
        templist = list()
        for i in lst:
            templist.append(i[1:])
        return templist



    # def removeWithCondition(lst):
    #     templist = list()
    #     for w in lst:
    #         if w[0] == "a" or w[0] == "e" or w[0] == "o" or w[0] == "i" or w[0] == "u" or w[0] == "y":
    #             templist.append(w[1:])
    #         else:
    #             templist.append(w)
    #     return templist
    #
    def removeWithCondition(lst):
        templist = list()
        string = "aeoiuy"



    def addingShwa(lst):
        templist = list()
        for w in lst:
            # length = len(w)
            s = 'shwa' + w + " " + str()
            templist.append(s)
        return templist

    test_strings = removefirstchar(test_strings)
    print(test_strings)

    test_strings = removeWithCondition(test_strings)
    print(test_strings)

    test_strings = addingShwa(test_strings)
    print(test_strings)

shwalengthimter(test_strings)