test_case = int(input())

for ind in range(test_case):
    days = int(input())

    q_five = int(days / 5)

    marks = ((days*(days+1))/2) - (((5*q_five+5)*q_five)/2)
    
    print("Case {}: {}".format(ind+1, int(marks)))
