# Find the anonymous function in the given array and use the
# function to process the rest members of array (like map does)
#
# find_function([lambda a: a+2,9,3,1,0]) # [11,5,3,2]
# find_function([9,3,lambda a: a/2.0,1,0]) #[4.5,1.5,0.5,0.0]
#
# Итого: есть лист, в нём один из элементов (неизвестно какой именно) -
# lambda функция. Её надо найти и использовать
# на всех остальных элементах списка.
#                         def find_lambda(*args, **kwargs):
#     return []
#
# print(find_lambda([lambda a: a+2,9,3,1,0])) # [11, 5, 3, 2]
# print(find_lambda([9,2,3,lambda a: a/2.0,1,0])) #[4.5, 1, 1.5, 0.5, 0.0]



from inspect import isfunction

array1 = [lambda a: a+2,9,3,1,0]
array2 = [9,3,lambda a: a/2.0,1,0]

def find_lambda(*args, **kwargs):
    tmp_lst = list()
    func = []
    for i in list(*args):
        if isfunction(i):
          func = i
        else:
            tmp_lst.append(i)
    result = list(map(func, tmp_lst))
    return result


print(find_lambda(array1))

find_lambda(array1)