# list comprehension example
list1=[x for x in range(0,5)]


# dictionary comprehension
items=['apple','banana','orange','apple','banana']
dict1={item:items.count(item) for item in items}