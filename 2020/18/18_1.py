def solve(eq):
    i = 0
    nested = 0
    if '(' in eq or ')' in eq:
        for i in range(len(eq)):
            if eq[i] == '(':
                nested += 1
                if nested == 1:
                    ind_left = i

            if eq[i] == ')':
                nested -= 1
                if nested == 0:
                    ind_right = i

                    if ind_left == 0 and ind_right == len(eq)-1:
                        new_eq = eq[ ind_left+1 : ind_right ]
                        # print("SOLVING 1: ", new_eq)
                        return solve(new_eq)
                    elif ind_left == 0 and ind_right < len(eq)-1:
                        new_eq = solve(eq[ ind_left+1 : ind_right ]) + eq[ind_right+1:]
                        # print("SOLVING 2: ", new_eq)
                        return solve(new_eq)
                    elif ind_left > 0 and ind_right == len(eq)-1:
                        new_eq =  eq[:ind_left] + solve(eq[ ind_left+1 : ind_right ])
                        # print("SOLVING 3: ", new_eq)
                        return solve(new_eq)
                    else:
                        new_eq =  eq[:ind_left] + solve(eq[ ind_left+1 : ind_right ]) + eq[ind_right+1:]
                        # print("SOLVING 4: ", new_eq)
                        return solve(new_eq)

    else:
        for i in range(len(eq)):
            if eq[i] == '*':
                left_int = int(eq.split(' * ')[0])
                if eq.count(' ') == 2:
                    right_int = int(eq.split(' * ')[1])
                    return str(left_int*right_int)
                else:
                    right_int = int(eq.split(' * ')[1].split(' ')[0])
                    new_eq = str(left_int*right_int) + eq[i+2+len(str(right_int)):]
                    return solve(new_eq)

            if eq[i] == '+':
                left_int = int(eq.split(' + ')[0])
                if eq.count(' ') == 2:
                    right_int = int(eq.split(' + ')[1])
                    return str(left_int+right_int)
                else:
                    right_int = int(eq.split(' + ')[1].split(' ')[0])
                    new_eq = str(left_int+right_int) + eq[i+2+len(str(right_int)):]
                    return solve(new_eq)


with open("day18.txt","r") as file:

    f = file.read().splitlines()
    ans = 0
    for eq in f:
        # print("Equation: ", eq, "Answer: ", solve(eq))
        int_ans = int(solve(eq))
        ans += int_ans

    print("FINAL ANSWER: ", ans)