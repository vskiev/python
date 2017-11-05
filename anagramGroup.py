from collections import defaultdict
test_list = ["tSAr", "rat", "tar", "star", "tars", "cheese"]

def groupAnagrams(lst):
 d=defaultdict(list)
 for w in lst:
    d[''.join(sorted(w))].append(w)
 print(list(d.values()))
 return list(d.values())


groupAnagrams(test_list)



# test_list = ["tsar", "rat", "tar", "star", "tars", "cheese"]
#
#
# def groupAnagrams(input_list):
#     return []



#
# def groupAnagrams(input_list):
#
#     test = list()
#     for i in range(len(input_list)):
#         test.append(sorted(input_list[i].lower()))
#
#     for i in test:
#
#     print(test)
# # return []
#
#
#
# groupAnagrams(test_list)





# def groupAnagrams(lst):
    # list of dict
    # d = {}
    # lst_Of_Dict = list()
    # for word in lst:
    #     lst_Of_Dict.append(dict ( (key, []) for key in word ))
    #
    # for i in range(len(lst_Of_Dict)):
    #     # print(lst_Of_Dict[i])
    #     d = dict(lst_Of_Dict[i])
    #
    # for word in lst:
    #     for char in word:
    #         if char in d.keys():
    #             d
    # def Dic_List(list1):
    #     for  word in list1:
    #      list1.append(dict.fromkeys(word, 0))
    #     return list1

        #
        # for i in range(len(lst_Of_Dict)):
        #     d = dict(lst_Of_Dict[i])
        # for word in lst:
        #     for c in word:
        #         if c in d.keys():
        #            d[c] +=1
        #         else:
        #              d[c] =1


    # for i in range(len(lst_Of_Dict)):
    #     d = dict(lst_Of_Dict[i])
    #
    #     if word in d:
    #         d[word] += 1
    #     else:
    #         d[word] = 1

        # print(d)

# groupAnagrams(test_list)

