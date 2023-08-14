from tabulate import tabulate


def main():
    # print("Loading ", end="")
    # rotating_circle_animation()

    num_students = read_valid_input("\nHow many students do you have?", 0, 100)
    num_subjects = read_valid_input("How many subjects do they offer?", 0, 100)

    print("Saving ", end="")
    iteration = 10
    for _ in range(iteration):
        print(">", end="")
        time.sleep(0.3)
    print("\nsaved successfully\n")

    scores = []
    for student in range(num_students):
        print(f"Entering score for student {student + 1}:")
        student_scores = []
        for subject in range(num_subjects):
            print(f"Enter score for subject {subject + 1}:")
            score = read_valid_input(None, 0, 100)
            student_scores.append(score)

            print("Saving ", end="")
            for _ in range(iteration):
                print(">", end="")
                time.sleep(0.2)
            print("\nSaved successfully\n")

        scores.append(student_scores)

    student_positions = calculate_student_positions(scores)

    subject_totals = [sum(scores[student][subject] for student in range(num_students)) for subject in
                      range(num_subjects)]
    student_totals = [sum(scores[student]) for student in range(num_students)]

    highest_scores_per_subject = [max(scores[student][subject] for student in range(num_students)) for subject in
                                  range(num_subjects)]
    lowest_scores_per_subject = [min(scores[student][subject] for student in range(num_students)) for subject in
                                 range(num_subjects)]

    class_total_score = sum(student_totals)
    class_average_score = class_total_score / (num_students * num_subjects)

    pass_threshold = 50
    num_passes_per_subject = [sum(1 for student in range(num_students) if scores[student][subject] >= pass_threshold)
                              for subject in range(num_subjects)]
    num_fails_per_subject = [num_students - num_passes for num_passes in num_passes_per_subject]

    hardest_subject_index = subject_totals.index(min(subject_totals))
    easiest_subject_index = subject_totals.index(max(subject_totals))

    overall_highest_score = max(student_totals)
    overall_lowest_score = min(student_totals)

    best_graduating_student_index = student_totals.index(max(student_totals))
    worst_graduating_student_index = student_totals.index(min(student_totals))

    student_data = []
    for student in range(num_students):
        student_data.append([f"Student {student + 1}"] + scores[student] + [student_totals[student],
                                                                            student_totals[student] / num_subjects,
                                                                            student_positions[student]])

    headers = ["Student"] + [f"SUB {subject + 1}" for subject in range(num_subjects)] + ["TOT", "AVE",
                                                                                             "POS"]

    print(tabulate(student_data, headers=headers, tablefmt="grid"))

    print("\nSUBJECT SUMMARY:")
    for subject in range(num_subjects):
        print(f"Highest Scoring subject is: {subject + 1}: scoring: {highest_scores_per_subject[subject]}")
        print(f"Lowest Scoring subject is: {lowest_scores_per_subject[subject]}")
    for subject in range(num_subjects):
        print(
            f"Subject {subject + 1} Passes: {num_passes_per_subject[subject]} Fails: {num_fails_per_subject[subject]}")

    print(
        f"Hardest Subject: Subject {hardest_subject_index + 1} with Average Score: {subject_totals[hardest_subject_index] / num_students}")
    print(
        f"Easiest Subject: Subject {easiest_subject_index + 1} with Average Score: {subject_totals[easiest_subject_index] / num_students}")

    print(f"Overall Highest Score: {overall_highest_score}")
    print(f"Overall Lowest Score: {overall_lowest_score}")
    print("===============================================================")
    print()
    print("CLASS SUMMARY")
    print("===============================================================")
    print(
        f"Best Graduating Student: Student {best_graduating_student_index + 1} with Total Score: {student_totals[best_graduating_student_index]}")
    print("===============================================================")
    print()
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(
        f"Worst Graduating Student: Student {worst_graduating_student_index + 1} with Total Score: {student_totals[worst_graduating_student_index]}")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print()
    print("===============================================================")
    print(f"Class total Score is: {class_total_score}")
    print(f"Class Average score is: {class_average_score}")
    print("===============================================================")


def read_valid_input(prompt, min_val, max_val):
    if prompt is not None:
        print(f"{prompt}\n")

    while True:
        try:
            number = int(input())
            if min_val <= number <= max_val:
                return number
            else:
                print(f"Invalid input. Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# def rotating_circle_animation():
#     animation_frames = ["🇬🇪", "🇺🇲", "🇬🇧", "🇳🇬", "🇦🇱", "🇧🇷", "🇨🇦", "🇩🇰", "🇳🇬"]
#     iterations = 25
#
#     for _ in range(iterations):
#         print(f"\r{animation_frames[_ % len(animation_frames)]}", end="")
#         time.sleep(0.5)


def calculate_student_positions(scores):
    total_scores = [sum(student_scores) for student_scores in scores]
    sorted_indices = sorted(range(len(total_scores)), key=lambda k: total_scores[k], reverse=True)
    positions = [sorted_indices.index(i) + 1 for i in range(len(sorted_indices))]
    return positions

if __name__ == "__main__":
    import time

    main()