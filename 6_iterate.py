names = ['小明', '小红', '小白', '小黑']
sores = [85, 92, 78, 88]
print('1.')
for i in range(len(names)):
    print(f'{names[i]},{sores[i]}')
print('\n2.')
for i, name in enumerate(names):
    print(f'{name},{sores[i]}')
print('\n3.')
for name, source in zip(names, sores):
    print(f'{name},{sores}')
