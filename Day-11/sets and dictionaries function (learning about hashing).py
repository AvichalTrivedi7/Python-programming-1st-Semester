'''

myset.union()   ---- |

myset.intersection()  ----- &

myset.difference()  ----- -

myset.symmetric_difference() ------- ^

myset.add()

myset.update({*multiple elements*})
myset.remove()


myset.difference_update({*multiple elements*})
myset.discard()
myset.clear(*removes all elements*)
myset.issubset()
myset.issuperset()
	

mydict=dict('name'='avichal','roll'=6)

mydict={'name':'avichal','roll':6}

print(mydict.pop('name'))

mydict.clear()

del mydict['name']

print(mydict.get('name','Unknown'))


'''

my_dict = {frozenset([1, 2, 3]): "value1", frozenset([4, 5]): "value2"}

print(my_dict)

print(my_dict[frozenset({1,2,3})]) #for hashing, will learn later