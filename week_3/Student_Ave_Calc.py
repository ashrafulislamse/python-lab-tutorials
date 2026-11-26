# Week 3 tutorial - Student Average Calculator
# reads three quiz marks, shows the average, decides pass or fail,
# and repeats for the next student until the user answers N

choice = "y"

# iteration: repeat the whole program while the user answers Y
while choice.lower() == "y":
    # input: read the three quiz marks
    quiz_1 = float(input("Enter Quiz 1 mark: "))
    quiz_2 = float(input("Enter Quiz 2 mark: "))
    quiz_3 = float(input("Enter Quiz 3 mark: "))

    # process: calculate the average of the three marks
    average = (quiz_1 + quiz_2 + quiz_3) / 3

    # output: show the average, then selection decides pass or fail
    print(f"Average mark: {average:.2f}")
    if average >= 50:
        print("Result: PASS")
    else:
        print("Result: FAIL")

    # ask whether another student's marks will be entered
    # .lower() so both Y and y continue the loop
    choice = input("Continue? Select Y/N: ")

print("Program Ended")
