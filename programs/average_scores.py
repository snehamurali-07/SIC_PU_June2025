''' Accept the average score of the student and give her the results as follow:
0 to 69 - Fail
70 to 84 - 2nd class
85 to 95 - 1st class
96 to 100 - Excellent
'''
avg_score = int(input("Enter the average score: "))
if 0 <= avg_score <= 69:
    print("Fail")
elif 70 <= avg_score <= 84:
    print("2nd class")
elif 85 <= avg_score <= 95:
    print("1st class")
elif 96 <= avg_score <=100:
    print("Excellent")
else:
    print("Invalid input")