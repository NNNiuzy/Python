# 排序中的lamba
students = [
    {'name': 'john', 'score': 'B', 'age': 15},
    {'name': 'jane', 'score': 'A', 'age': 12},
    {'name': 'dave', 'score': 'B', 'age': 10},
    {'name': 'ethan', 'score': 'C', 'age': 20},
    {'name': 'peter', 'score': 'B', 'age': 20},
    {'name': 'mike', 'score': 'C', 'age': 16}
]

print(sorted(students, key=lambda stu: stu['score']))
