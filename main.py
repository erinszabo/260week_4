"""
chap 4 exercises: 1,2,3,5,and 10 or 11
"""
import evaluators as e

if __name__ == '__main__':
    print()
    print("1) Modify the infix-to-postfix algorithm so that it can handle errors.")
    print(f"testing with bad input ('3 j +') returns: {e.infixToPostfix('3 j +')}")
    print(f"testing again with valid ('3 + 5') input returns: {e.infixToPostfix('3 + 5')}")


    print()
    print("2) Modify the postfix evaluation algorithm so that it can handle errors.")
    print(f"testing with bad input ('5 + 3') returns: {e.postfixEval('5 + 3')}")
    print(f"testing again with valid ('5 3 +') input returns: {e.postfixEval('5 3 +')}")

    print()
    print("3) Implement a direct infix evaluator that combines the functionality of infix-to-postfix "
          "conversion and the postfix evaluation algorithm. Your evaluator should process infix tokens "
          "from left to right and use two stacks, one for operators and one for operands, to perform the evaluation.")

    print()
    print("5) Implement the Queue ADT, using a list such that the rear of the queue is at the end of the list.")

    print()
    print("...10 or 11 here...")
    print()
    print()
