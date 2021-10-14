# /usr/bin/env python3

# Created by: Rodas Nega
# Created on: Oct 2021
# This program asks the user for their grade level and
# converts it into a middle percentage


def level_conversion(grade_level):
    # calculate percentage from level

    # process & output
    if grade_level == "4+":
        grade_percentage = 97.5

    elif grade_level == "4":
        grade_percentage = 90.5

    elif grade_level == "4-":
        grade_percentage = 83

    elif grade_level == "3+":
        grade_percentage = 78

    elif grade_level == "3":
        grade_percentage = 74.5

    elif grade_level == "3-":
        grade_percentage = 71

    elif grade_level == "2+":
        grade_percentage = 68

    elif grade_level == "2":
        grade_percentage = 64.5

    elif grade_level == "2-":
        grade_percentage = 61

    elif grade_level == "1+":
        grade_percentage = 58

    elif grade_level == "1":
        grade_percentage = 54.5

    elif grade_level == "1-":
        grade_percentage = 51

    elif grade_level == "R":
        grade_percentage = 24.5

    else:
        grade_percentage = -1

    return grade_percentage


def main():
    # this function calls the precedent function

    # input
    user_grade_level = input("Enter your level for percentage conversion: ")

    level_converted = level_conversion(user_grade_level)  # call function

    if level_converted == -1:  # error check
        print("Error")
    else:
        print(
            "Level {0} has a middle percentage of {1}%".format(
                user_grade_level, level_converted
            )
        )

    print("\nDone.")


if __name__ == "__main__":
    main()
