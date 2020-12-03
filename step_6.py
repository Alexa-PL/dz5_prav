result = {}
with open("text_66.txt", encoding="utf-8") as f_obj:
    for line in f_obj:
        lesson_time = []
        lessons = ([el for el in line.split(" ")])
        for el in lessons:
            lesson_time.append(''.join(i for i in list(el) if i.isdigit()))
        result[line.split(':')[0]] = sum([int(i) for i in lesson_time if i.isdigit()])

print(result)