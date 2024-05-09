if __name__ == '__main__':
    student_marks = {}

    for _ in range(int(input())):
        # Save the first value in name, the others will save in the list call "line"
        name, *scores = input().split()
        # Change int values by float
        scores = list(map(float, scores))
        # Create a dict with the following format -> {"name": [float_scores],....}
        student_marks[name] = scores

    query_name = input()

    if query_name in student_marks.keys():
        print(f"{sum(student_marks[query_name]) / len(student_marks[query_name]):.2f}")