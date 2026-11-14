course_a = ['小明', '小红', '小李', '小张', '小明']
course_b = ['小李', '小黑', '小张', '小白']
set_a = set(course_a)
set_b = set(course_b)
print(set_a)
print(set_b)
both = set_a & (set_b)
print(both)
only_one = set_a ^ (set_b)
print(only_one)
