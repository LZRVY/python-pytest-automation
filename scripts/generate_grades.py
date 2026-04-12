import src.grades_generator
from src.grades_process import parse_grades, process_grades

if __name__ == "__main__":
    names = [
        "Saige Fuentes", "Bowen Higgins", "Leighton Kramer", "Kylan Gentry",
        "Amelie Griffith", "Franklin Sierra", "Marceline Avila", "Jaylen Blackwell",
        "Saoirse Conrad", "Dilan Wolf", "Esme Vance", "Ronan Boyer",
        "Kiera Hodge", "Zion Mccarthy", "Maeve Stout", "Alaric Pineda",
        "Lyra Best", "Cillian Rocha", "Elara Gamble", "Soren Petty"
    ]

    scores = [
        91, 65, 82, 74, 99, 88, 70, 95, 61, 77,  # Original 10
        15, 37, 50, 58,  # 40% Failing (< 60)
        "N/A", -15,  # 20% Invalid
        74, 64, 85, 89  # 40% Passing
    ]

    with open("../data/grades.txt", "w") as grades_file:
        for grade in src.grades_generator.gen_grades(names, scores):
            print(grade)
            grades_file.write(grade + "\n")


    summary = process_grades("../data/grades.txt", "../data/passed.txt", "../data/failed.txt", "../data/gd_err.txt")
    print(summary)

