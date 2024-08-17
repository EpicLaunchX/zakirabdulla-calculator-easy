from pytemplate.domain.models import operands_factory
from pytemplate.service.calculator import Calculator


def main():
    user_input = input("Enter two numbers and action separated by a comma: ")
    first_operand, second_operand, action = user_input.split(",")
    operands = operands_factory(int(first_operand), int(second_operand))
    calculator = Calculator()
    action = action.strip().lower()
    if action == "add":
        result = calculator.add(operands)
    elif action == "subtract":
        result = calculator.subtract(operands)
    elif action == "multiply":
        result = calculator.multiply(operands)
    elif action == "divide":
        result = calculator.divide(operands)
    else:
        raise ValueError("Invalid action")
    return result


if __name__ == "__main__":
    main()
