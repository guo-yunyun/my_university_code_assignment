text = input('请输入一个字符串：')
reversed_text = text[::-1]
print('反转结果是：', reversed_text)
if text == reversed_text:
    print('判断结果：这是一个回文！')
else:
    print('判断结果：这不是一个回文！')
