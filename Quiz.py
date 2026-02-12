print("JAI SHREE RAM!!\nWelcome to the Quiz")
score = 0
name = input("Please enter your name") 
print(f"Hello {name}!, lets get started")
print("1)Ramayana was written by?")
answer = input("your answer:")
if answer.lower() == "valmiki":
    print("Correct — well done!")
    score += 1
else :
    print("the correct answer is valmiki")
print("2)Who is the mother of Karna?")
answer = input("your answer:")
if answer.lower() == "kunti devi":
    print("That's right!")
    score += 1
else :
    print("the correct answer is Kunti devi")
print("3)What is the real name of Bhishma pitamah?")
answer = input("your answer:")
if answer.lower()== "devavrata":
    print("Great going!")
    score += 1
else :
    print("the correct answer is Devavrata")
print("4)Who is the prime minister of india?")
answer = input("your answer:")
if answer.lower()=="narendra modi":
    print("Bullseye!")
    score += 1
else :
    print("The answer is Narendra modi")
print("5)What is the name of your country?")
answer = input("your answer:")
if answer.lower()=="bharath":
    print("Awesome — you got it!")
    score += 1
else :
    print("The answer is bharath")
print(f"Your final score is {score} out of 5.")
print("\nQuiz Completed!")
