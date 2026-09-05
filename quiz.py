questions = ("What is the capital of France?",
             "What is 2 + 2?",
             "what is the largest oceamn in world?",
             "what is 3+4"
            )
option = ("A. Paris B. London C. Berlin D. Madrid",
          "A. 3 B. 4 C. 5 D. 6",
            "A. Atlantic Ocean B. Indian Ocean C. Pacific Ocean D. Arctic Ocean",
            "A. 5 B. 6 C. 7 D. 8"
         )
answers = ("Paris",
            "4",
              "Pacific Ocean",
                "7"
          )
print("----------------")
#print(questions)
for que in questions:
    print(que)
    for opt in option:
        print(opt,end="\n")  
answer = input("Enter your answer: ")    