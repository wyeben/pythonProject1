def get_personality_type(answers):
    E = answers.count('a')
    I = answers.count('b')
    S = answers.count('a')
    N = answers.count('b')
    T = answers.count('a')
    F = answers.count('b')
    J = answers.count('a')
    P = answers.count('b')

    extroverted = 'a' if E > I else 'b'
    observant = 'a' if S > N else 'b'
    thinking = 'a' if T > F else 'b'
    judging = 'a' if J > P else 'b'

    return f"{extroverted}{observant}{thinking}{judging}"


def main():
    questions = [
        "Do you prefer spending time with others (a)"," or being alone (b)? ",
        "Do you focus on the details (a)"," or see the big picture (b)? ",
        "Are you more logical and analytical (a)"," or empathetic and compassionate (b)? ",
        "Do you like to plan and organize (a) ","or prefer to go with the flow (b)? ",
    ]

    answers = []

    for question in questions:
        answer = input(question).lower()
        while answer not in ['a', 'b']:
            print("Invalid response. Please enter 'a' or 'b'.")
            answer = input(question).lower()
        answers.append(answer)

    personality_type = get_personality_type(answers)
    print(f"Your Myers-Briggs Personality Type is: {personality_type}")


main()
