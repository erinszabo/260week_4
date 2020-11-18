class Stack:  # a stack of blocks
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):  # place a new block on the stack O(1)
        self.items.append(item)

    def pop(self):  # look at and remove the top block O(1), bottom block O(n)
        return self.items.pop()

    def peek(self):  # just look at the top block O(1), bottom block O(n)
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


""" 
need to fix, right now it is only checking for edges of tag. 
needs to check for open vs close tags
VVVVVVVVVVVVVVVVVVVVVVVVVVVVV
"""

def tag_checker(symbolString):
    """
    checks if balanced
    :param symbolString:
    :return: Boolean
    """
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "<":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False

        index = index + 1

    if balanced and s.is_empty():
        return True
    else:
        return False


def matches(open, close):
    opener = "<"
    closer = ">"  # maybe use "</" here instead? Didn't work but might just need tweaking
    return opener.index(open) == closer.index(close)


def tag_check(codeString):
    """
    :param codeString: the code that you want to check if the tags are balanced
    :return: Boolean, True if Balanced, False if not Balanced
    """
    balanced = True
    symbol_string = ""
    close = ""
    for i in codeString:
        if i in "<":
            symbol_string += i
        if i in "/":
            close += i
    # print(symbol_string)
    # print(close)
    if len(symbol_string) % 2 != 0 or len(close) != len(symbol_string) // 2:
        balanced = False
    return balanced


