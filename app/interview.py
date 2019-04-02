
class Stek:

    def __init__(self):
        self.items = []

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            result = self.items[-1]
            del self.items[len(self.items) - 1]
            return result
        else:
            return None

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            return None


x = Stek()

x.push(1)
x.push(2)
x.push(3)

print(x.is_empty())

print('peek:', x.peek())
print(x.pop())
print('peek:', x.peek())
print(x.pop())
print(x.pop())

print(x.is_empty())


class Queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            result = self.items[0]
            del self.items[0]
            return result
        else:
            return None

    def peek(self):
        if self.items:
            return self.items[0]
        else:
            return None


def check_brackets(your_brackets):
    """
    >>> check_brackets('()')
    True

    >>> check_brackets('{{')
    False

    >>> check_brackets('{{(())')
    False

    >>> check_brackets('{{]')
    False

    >>> check_brackets('{{}}[]')
    True

    >>> check_brackets('((([(])))')
    False
    """
    copy_brackets = your_brackets[:]
    search_for = ['()', '[]', '{}']

    for x in range(len(copy_brackets)):
        for pair in search_for:
            if pair in copy_brackets:
                index = copy_brackets.index(pair)

                copy_brackets_list = list(copy_brackets)
                del copy_brackets_list[index]
                del copy_brackets_list[index]

                copy_brackets = "".join(copy_brackets_list)

    return not copy_brackets
