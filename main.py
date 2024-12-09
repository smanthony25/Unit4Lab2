# Sean A
# Simple Reverse
# Use ArrayStack to easily reverse a string!!

from StackClass import ArrayStack


def main():
    original = "Sphinx of black quartz, judge my vow"
    new = ""

    stack = ArrayStack()

    for i in range(len(original)):
        stack.push(original[i])

    for i in range(len(stack)):
        new += stack.pop()

    print(f"Original: {original}")
    print(f"New: {new}")


if __name__ == "__main__":
    main()
