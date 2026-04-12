import random


def gen_grades(names, scores):
    random.shuffle(names)
    random.shuffle(scores)
    stu_grades = zip(names, scores)

    for name, score in stu_grades:
        yield f"{name}, {score}"
