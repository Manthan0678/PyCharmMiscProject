# mock test total score and average score finder
enter_test_score = 0.000000000000000000000000000000000000000000000000000000000000000000000000000000000001
total_test = 0
total_score = 0
while enter_test_score != 0:
    enter_test_score = float(input("enter your test score(or type 0 to finish):"))
    if enter_test_score != 0:
        total_score = enter_test_score + total_score
        total_test = total_test + 1

print("total score is:" + str(total_score))
print("total test count is:" + str(total_test))
if total_test > 0:
    average = total_score / total_test
    print("average score is:" + str(average))
else:
    print("you did not appear in any test")