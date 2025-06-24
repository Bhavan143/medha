#1.What do you need?
#score
#2.What do you want from whom?
#questions-myself
#need each answer from user
#3.order the needs with priority
#same
#4.flow/pseudo code
### 1.define questions ds
### 2.iterate and show each question
### 3.itearte and collect each question response form user
### 4.iterate and for every correct answer we need to increment the score
### 5.print score


#5.Implementation

questions=[
    {
    "question": "What is the capital of France?",
    "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
    "answer": "C"  
    },
    {
    "question": "What is the capital of INDIA?",
    "options": ["A. Delhi", "B. Madrid", "C. Paris", "D. Rome"],
    "answer": "A"
    },
    {
    "question": "What is the capital of USA?",
    "options": ["A. Berlin", "B. Washington D.C", "C. Paris", "D. Rome"],
    "answer": "B"
    }
]
count=0
for i,q in enumerate(questions):
    print(f"""
    Question {i+1}:{q["question"]}
    {q["options"][0]}
    {q["options"][1]}
    {q["options"][2]}
    {q["options"][3]}
    """)
    your_answer=input("enter your answer:")
    if your_answer == q["answer"]:
        print("Correct!")
        count+=1
    else:
        print("Incorrect!")
print(f"your score is :{count}")