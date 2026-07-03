from prompt import prompt

# data = {
#     "topic": "FastAPI",
#     "language": "Python",
#     "level": "Beginner"
# }

# result = prompt.format(**data)

# print(result)



result = prompt.format(
    name="Praveen",
    age=30,
    city="Chennai"
)

print(result)