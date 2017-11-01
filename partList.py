#!/usr/bin/python3.6
# Write a function that gives all the ways to
# divide a list of at least two elements in two non-empty parts.
#
# Each two non empty parts will be in a tuple
# Each part will be in a string
# Elements of a pair must be in the same order as in the original array.
# Example:
#
# >>> a = ["az", "toto", "picaro", "zone", "kiwi"]
# >>> partlist(a)
#
# [('az', 'toto picaro zone kiwi'), ('az toto', 'picaro zone kiwi'), ('az toto picaro', 'zone kiwi'), ('az toto picaro zone', 'kiwi')]


list_ = ["az", "toto", "picaro", "zone", "kiwi"]
def partlist(list_):
 b = list()
 c = list()

 for i in range(1, len(list_)):
      s = ' '.join(list_[:i])
      s1 = ' '.join(list_[i:])

      b.append(s)
      b.append(s1)

 for j in zip(*[iter(b)]*2):
  c.append(j)

 return c

'''zip(*iterables)
Make an iterator that aggregates elements from each of the iterables.

Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. The iterator stops when the shortest input iterable is exhausted. With a single iterable argument, it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator. Equivalent to:

def zip(*iterables):
    # zip('ABCD', 'xy') --> Ax By
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)
The left-to-right evaluation order of the iterables is guaranteed. This makes possible an idiom for clustering a data series into n-length groups using zip(*[iter(s)]*n).

zip() should only be used with unequal length inputs when you don’t care about trailing, unmatched values from the longer iterables. If those values are important, use itertools.zip_longest() instead.'''