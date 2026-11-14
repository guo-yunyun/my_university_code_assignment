a = int(input("请输入第一个整数"))
b = int(input("请输入第二个整数"))
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
if b == 0:
    print("除数不能为0")
else:
    print(f"{a} / {b} = {a / b}")


