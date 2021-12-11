illegals = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

full_sum = 0
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        stack = []
        for bracket in line:
            # if we find closed bracket check if there was an opening one
            if bracket in [')',']','}','>']:
                last_bracket = stack.pop()
                # if the closing bracket differs
                if bracket != last_bracket:
                    full_sum += illegals[bracket]
                    break
            # if we find opening bracket just add it to the stack
            else:
                if bracket == '(':
                    stack.append(')')
                if bracket == '[':
                    stack.append(']')
                if bracket == '{':
                    stack.append('}')
                if bracket == '<':
                    stack.append('>')

print(full_sum)
            