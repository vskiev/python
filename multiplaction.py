#!/usr/bin/env python3.6
#v1
# for i in range(1,11):
#     for j in range(1,11):
#         print("%4d" % (i*j), end='')
#     print()
#v2
for i in range(1,11):
    for j in range(1,11):
        print('{:>4}'.format((i*j)), end='')
    print()