score = float(input('请输入一个百分制的成绩：'))
if score >= 90:
    print('优秀')
elif 80 <= score <= 89:
    print('良好')
elif 70 <= score <= 79:
    print('中等')
elif 60 <= score <= 69:
    print('及格')
else:
    print('不及格')
