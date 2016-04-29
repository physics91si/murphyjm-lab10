#!/usr/bin/python

import sets

a = sets.Set()

a.add('1')
a.add('1')
a.add('2')
a.remove('1')
a.remove('3')
a.add('1')
a.add(0)

print('passed test 1')

b = sets.Set()

b.add('2')
b.add('3')
b.add('4')
b.add(5)

c = a & b
print(c.elements)

d = a | b
print(d.elements)

e = d - c
print(e.elements)
