import operator

text = 'apple,banana,apple,banana,pear,apple'
fruits = text.split(',')
count_dict = {}
for fruit in fruits:
    count_dict[fruit] = count_dict.get(fruit, 0) + 1
sorted_counts = sorted(count_dict.items(), key=operator.itemgetter(1), reverse=True)
print()
for fruit in sorted_counts:
    print(fruit)
