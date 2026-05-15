from users import (
    student_login,
    submit_assignment,
    view_grades
)


def main():
# student login first, function definced in file users.py
    student_login("Mohammad")

    submit_assignment(
        "Mohammad",
        "Python Decorator Project"
    )

    view_grades("Alex")


if __name__ == "__main__": # script starts here
    main() # call function main, defined in line 8
