#python project quiz

questions =["Who invented cruise wheel? 1)Nikola Tesla 2)Radeph Tennon 3)Adolf Hitler" ,"Who was the founder of the company Apple? 1)Albert Einstein 2)Dalai Lama 3) Steve Jobs" , "Who was the Favorite actor of Neerja Bhanot? 1)Akshay Kumar 2)Rajesh Khanna 3)Amitabh Bachaan" ]


questionstot = len(questions)

answers = ["2", "3", "3"]

ansindex = -1

cor = 0

print("Quiz Started! Choose the number as the answer:")
for question in questions:
    ansindex = ansindex +1
    print(question)
    ans = input("Choose your answer: ")
    if ans in answers[ansindex]:
        cor = cor +1

print("Quiz Finished! you got "+str(cor)+ " out of" + str(questionstot)+ "questions right")
