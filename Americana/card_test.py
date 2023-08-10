def get_personality_type(answers):
    personality_type = ''

    for answer in answers:
        personality_type += 'E' if answer == '1' else 'I'
        personality_type += 'S' if answer == '2' else 'N'
        personality_type += 'T' if answer == '3' else 'F'
        personality_type += 'J' if answer == '4' else 'P'

    return personality_type


def main():
    print("Answer the following questions with 1 or 2:")
    answers = []

    questions = [
        "You prefer to spend time with others at social events. (1) or (2)",
        "You focus on the practical details and realities of life. (1) or (2)",
        "You base your decisions on logical analysis and objective criteria. (1) or (2)",
        "You prefer to plan and organize your activities in advance. (1) or (2)"
    ]

    for question in questions:
        answer = input(question)
        while answer not in ['1', '2']:
            print("Invalid input. Please enter 1 or 2.")
            answer = input(question)
        answers.append(answer)

    personality_type = get_personality_type(answers)
    print("Your personality type:", personality_type)


if __name__ == "__main__":
    main()
