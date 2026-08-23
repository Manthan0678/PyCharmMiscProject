#Percentage Calculator
physics_score = float(input("Enter physics score: "))
chemistry_score = float(input("Enter chemistry score: "))
mathematics_score = float(input("Enter mathematics score: "))
sum = physics_score + chemistry_score + mathematics_score
percentage = (sum/300)*100
print("you total score out of 300 marks is:" + str(sum))
print("your overall percentage is:" + str(percentage) + "%")