class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        return False

    def push(self, new_element):
        self.stack.insert(0, new_element)

    def pop(self):
        return self.stack.pop(0)

    def peek(self):
        return self.stack[0]

    def size(self):
        return len(self.stack)


def is_balanced(text):
    opening = ['(', '[', '{']
    closing = [')', ']', '}']
    my_stack = Stack()
    for symbol in str:
        if symbol in opening:
            my_stack.push(opening.index(symbol))
        elif symbol in closing:
            if my_stack.stack and my_stack.peek() == closing.index(symbol):
                my_stack.pop()
            else:
                return 'Несбалансированно'
    return 'Сбалансированно'


if __name__ == '__main__':
    str = input()
    print(is_balanced(str))
