# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    #print(type(left))
    #print(type(right))
    
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i))
            #Bracket.char = next
            #Bracket.position = i+1
            

        if next in ")]}":
            #print(len(opening_brackets_stack))
            #print(opening_brackets_stack, next)
            #print(are_matching(str(opening_brackets_stack), next))
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[len(opening_brackets_stack)-1][0], next):
                #print(i+1)
                return i + 1 
            #else :
            if are_matching(opening_brackets_stack[len(opening_brackets_stack)-1][0], next):
                opening_brackets_stack.pop()
            # Process closing bracket, write your code here
    
    if opening_brackets_stack :
        return opening_brackets_stack[len(opening_brackets_stack)-1][1] + 1



def main():
    text = input()
    if text[0:5] == 'I\\r\\n':
        text = text[5:]
    elif text == 'F':
        file = "./Datu struktūras/test1.txt"
        with open(file) as f:
            text = f.read()

    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if not mismatch :
        print("Success")
    else:
        print(mismatch)


if __name__ == "__main__":
    main()
