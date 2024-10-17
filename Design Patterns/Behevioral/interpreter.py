# Interpreter Pattern

from abc import ABC, abstractmethod

class Context:

    def __init__(self) -> None:
        self.stack = []


class Expression(ABC):
    @abstractmethod
    def interpret(self, context: Context) -> None:
        pass

class NumberExpression(Expression):

    def __init__(self, number: float) -> None:
        self.number = number

    def interpret(self, context: Context) -> None:
        context.stack.append(self.number)


class PlusExpression(Expression):

    def __init__(self, left: Expression, right: Expression) -> None:
        self.left = left
        self.right = right

    def interpret(self, context: Context) -> None:
        self.left.interpret(context)
        self.right.interpret(context)
        right_value = context.stack.pop()
        left_value = context.stack.pop()
        context.stack.append(left_value + right_value)


class MinusExpression(Expression):

    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self, context: Context):
        self.left.interpret(context)
        self.right.interpret(context)
        right_value = context.stack.pop()
        left_value = context.stack.pop()
        context.stack.append(left_value - right_value)


def parse_expression(expression: str) -> Expression:
    tokens = expression.split()
    stack = []

    for token in tokens:
        if token.isdigit():  # Si es un número
            stack.append(NumberExpression(float(token)))
        elif token == '+':  # Si es una suma
            right = stack.pop()
            left = stack.pop()
            stack.append(PlusExpression(left, right))
        elif token == '-':  # Si es una resta
            right = stack.pop()
            left = stack.pop()
            stack.append(MinusExpression(left, right))

    return stack.pop()


if __name__ == "__main__":
    context = Context()
    
    expression = "3 4 + 2 -"  # Esto significa (3 + 4) - 2
    parsed_expression = parse_expression(expression)
    
    parsed_expression.interpret(context)  # Interpretar la expresión
    
    print("Resultado:", context.stack.pop())  # Salida: Resultado: 5.0