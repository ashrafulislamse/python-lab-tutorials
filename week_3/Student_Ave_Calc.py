# Week 3 tutorial - Student Average Calculator
# Reads three quiz marks, shows the average and pass/fail (50 to pass),
# and repeats for the next student until the user answers N.

choice = "y"
while choice.lower() == "y":
    quiz_1 = float(input("Enter Quiz 1 mark: "))
    quiz_2 = float(input("Enter Quiz 2 mark: "))
    quiz_3 = float(input("Enter Quiz 3 mark: "))
    average = (quiz_1 + quiz_2 + quiz_3) / 3
    print(f"Average mark: {average:.2f}")
    if average >= 50:
        print("Result: PASS")
    else:
        print("Result: FAIL")
    # .lower() so both Y and y continue the loop
    choice = input("Continue? Select Y/N: ")
print("Program Ended")
