def median_score(students: int, max_score: int, min_max_score: list[tuple]):
    if students == max_score:
        return 1
    max_score_per_student = 0
    max_sum = 0

    total_students = students

    for score in min_max_score:
        minimal, maximum = (score[0]), score[1]
        if minimal == maximum:
            total_students -= 1
            continue
        max_sum += maximum
        if maximum > max_score_per_student:
            max_score_per_student = maximum
    return int(max_sum / total_students)


n, s = map(int, input().split())
students_scores = []
for i in range(n):
    students_scores.append(tuple(map(int, input().split())))
print(median_score(n, s, students_scores))

if __name__ == '__main__':
    # def res(students, score):
    #     return round(((score / students + score) / students))
    # 26 - equals; 42-26=[16]
    # (3,5) (7,9) (6,7) (3,8)
    # min = 3+7+6+3=[19]
    # max = 5+9+7+8=[29]
    array = [(5, 5),
             (3, 5),
             (7, 9),
             (6, 7),
             (3, 8),
             (10, 10),
             (1, 1),
             ]
    array2 = [(11, 14),
              (2, 10),
              (11, 14)
              ]
    print(median_score(7, 42, array))
    print(median_score(3, 27, array2))

