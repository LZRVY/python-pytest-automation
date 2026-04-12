def parse_grades(grade):
    grade = grade.strip()

    parts = [p.strip() for p in grade.split(",")]

    if len(parts) != 2:
        raise ValueError("Invalid grades format")

    name, score = parts
    if name == ""  or score == "":
        raise ValueError("Name/Grade cannot be empty")

    try:
        score_int = int(score)
    except ValueError:
        raise ValueError("Score must be an integer")

    if score_int < 0 or score_int > 100:
        raise ValueError("Score out of range: Score must be between 0 and 100")

    return name, score_int

def process_grades(grades, pass_stu, fail_stu, invalid_grade):
    total = passed = failed = invalid = 0
    valid_scores = []
    topper = average = None
    with open(grades, "r") as fin, open(pass_stu, "w") as fp, open(fail_stu, "w") as ff, open(invalid_grade, "w") as fe:
        for grade in fin:
            if not grade.strip():
                continue

            total +=1
            try:
                name, score_int = parse_grades(grade)
            except ValueError as e:
                invalid += 1
                fe.write(f"{e} | raw = {grade}\n")
                continue

            valid_scores.append(score_int)

            if score_int >= 60:
                passed += 1
                fp.write(f"{name} - {score_int}\n")
            else:
                failed += 1
                ff.write(f"{name} - {score_int}\n")
        if valid_scores:
            topper = max(valid_scores)
            average = round((sum(valid_scores) / len(valid_scores)),2)



    return {
        "grades parsed": total,
        "pass_count": passed,
        "fail_count": failed,
        "invalid grades": invalid,
        "top-scorer": topper,
        "average score of valid entries": average,
    }
