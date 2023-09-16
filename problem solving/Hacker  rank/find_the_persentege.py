if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    values = student_marks.get(query_name, [])
    number=float(sum(values))/ 3.00
    formatted_number = "{:.2f}".format(number)
    print(formatted_number)
