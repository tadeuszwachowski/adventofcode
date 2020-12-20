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
                    # print(ind_left,ind_right)
                    if ind_left == 0 and ind_right == len(eq)-1:
                        # print("SOLVING 1: ", eq[ ind_left+1 : ind_right ])
                        # for x in eq[ ind_left+1 : ind_right ]:
                        #     print(x)
                        new_eq = eq[ ind_left+1 : ind_right ]
                        # print( "LEN: ", len(eq[ ind_left+1 : ind_right ]) )
                        return solve(new_eq)
                    elif ind_left == 0 and ind_right < len(eq)-1:
                        # print("SOLVING 2: ", eq[ ind_left+1 : ind_right ] + eq[ind_right+1:] )
                        new_eq = solve(eq[ ind_left+1 : ind_right ]) + eq[ind_right+1:]
                        # print( "LEN: ", len(new_eq) )
                        return solve(new_eq)
                    elif ind_left > 0 and ind_right == len(eq)-1:
                        new_eq =  eq[:ind_left] + solve(eq[ ind_left+1 : ind_right ])
                        # print("SOLVING 3: ", new_eq)
                        # print(list(new_eq))
                        # print(new_eq)
                        # print( "LEN: ", len(new_eq) )
                        return solve(new_eq)
                    else:
                        # print("SOLVING 4: ", eq[ ind_left+1 : ind_right ])
                        new_eq =  eq[:ind_left] + solve(eq[ ind_left+1 : ind_right ]) + eq[ind_right+1:]
                        return solve(new_eq)

    else:
        # print("INPUT EQUATION: ", eq)
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
                # print(left_int, eq[i], right_int)

            if eq[i] == '+':
                # print("DEBUG: ", eq)
                left_int = int(eq.split(' + ')[0])
                if eq.count(' ') == 2:
                    right_int = int(eq.split(' + ')[1])
                    return str(left_int+right_int)
                else:
                    right_int = int(eq.split(' + ')[1].split(' ')[0])
                    new_eq = str(left_int+right_int) + eq[i+2+len(str(right_int)):]
                    # print("OUTPUT EQUATION: ",new_eq)
                    return solve(new_eq)
                # print(left_int, eq[i], right_int)
        

with open("day18.txt","r") as file:

    f = file.read().splitlines()
    ans = 0
    for eq in f:
        # print(eq)
        # print("Equation: ", eq, "Answer: ", solve(eq))
        int_ans = int(solve(eq))
        ans += int_ans

    print("FINAL ANSWER: ", ans)