#mathematical

import math

assistant = None
student = None
tutor = None

class Assistant:
    def validate_input(self, prompt, allow_complex=True):
        while True:
            user_input = input(prompt).strip()

            # Handle potential leading signs for real and imaginary parts
            clean_input = user_input.replace('j', '')
            if '+' in clean_input:
                clean_input = clean_input.replace('+', '')
            if '-' in clean_input and clean_input.count('-') == 1 and not clean_input.startswith('-'):
                clean_input = clean_input.replace('-', '')

            # Remove decimal points for integer validation
            temp_clean_input = clean_input.replace('.', '', 1)

            if temp_clean_input.isdigit():
                return complex(user_input) if allow_complex else int(user_input)
            else:
                print("Illegal input. Please enter a valid number.")

class Student:
    def calculate(self, val1, val2, operator):
        if operator == "+": return val1 + val2
        elif operator == "-": return val1 - val2
        elif operator == "*": return val1 * val2
        elif operator == "/":
            return val1 / val2 if val2 != 0 else "Error: Division by zero"
        elif operator == "%":
            # Modulo operator is typically for real numbers.
            # If complex, we'll take the real part for modulo.
            return val1.real % val2.real
        else:
            return "Illegal Operator"

    def print_result(self, result):
        if isinstance(result, complex) and result.imag == 0:
            print(f"Result: {result.real:.0f}")
        else:
            print(f"Result: {result}")

class Tutor:
    def get_command(self):
        return input("Choose operation: ").lower().strip()

def init():
    global assistant, student, tutor
    assistant = Assistant()
    student = Student()
    tutor = Tutor()

def begin():
    print("--- Shawn xi MSE800 Project: Modular Calculator ---")
    print("Supports: +, -, *, /, %, factorial")

    command = tutor.get_command()
    if command == "factorial":
        num = assistant.validate_input("Enter a positive integer: ", allow_complex=False)
        result = f"Result: {math.factorial(num)}"
        student.print_result(result)
    else:
        val1 = assistant.validate_input("Enter first number: ")
        val2 = assistant.validate_input("Enter second number: ")
        result = student.calculate(val1, val2, command)
        student.print_result(result)

if __name__ == "__main__":
    init()
    begin()