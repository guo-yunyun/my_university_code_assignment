names = ['小红', '小黑', '小白']
scores = [85.5, 92.0, 78.3]
print(f'{'姓名':<10}{'成绩':>6}')
for name, score in zip(names, scores):
    print(f'{name:<10}{score:>6.1f}')
