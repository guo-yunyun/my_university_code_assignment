import re
text='你好，我的手机号是12345678000，备用号是10087654321'
text=text+'我的邮箱是test23@qq.com'
text=text+'这人是个笨蛋，也是个傻瓜。'
print('原始文本',text)
phone_list=re.findall(r'1\d{10}',text)
print('提取手机号：',phone_list)
email_list=re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',text)
print('提取邮箱：',email_list)
new_text=re.sub('笨蛋','***',text)
new_text=re.sub('傻瓜','***',new_text)
print('替换敏感词后的文本：',new_text)
