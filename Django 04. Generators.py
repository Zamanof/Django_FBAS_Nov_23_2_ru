# Generators

# import datetime
#
# def infinite_days(start=None):
#     if start is None:
#         start = datetime.date.today()
#     while True:
#         yield start
#         start += datetime.timedelta(days=1)
#
#
# days = infinite_days()
# while True:
#     print(next(days))
#     input()

# using (var db = new SqlConnection())
# def read_file_lines(path):
#     with open(path, encoding="utf-8") as f:
#         for line in f:
#             yield line.strip()
#
# for line in read_file_lines("students.txt"):
#     print(">>", line)
#     input()