from collections import namedtuple

students_count, student_record = (int(input()),namedtuple("student_record", input().rstrip().split()))

print(sum([int(student_record(*input().rstrip().split()).MARKS) for _ in iter(range(students_count))])/students_count)
