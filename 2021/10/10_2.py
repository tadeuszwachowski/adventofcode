illegals = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

sums = []
incomplete = []
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        size = len(line)
        stack = []
        for i,bracket in enumerate(line):
            # if we find closed bracket check if there was an opening one
            if bracket in [')',']','}','>']:
                last_bracket = stack.pop()
                if bracket != last_bracket:
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
            # if we got to the end of the line it means we
            # encountered an incomplete one
            if i == size-1:
                s = 0
                for b in reversed(stack):
                    s *= 5
                    s += illegals[b]
                sums.append(s)

sums = sorted(sums)
middle_sum = sums[len(sums)//2]
print(middle_sum)


            