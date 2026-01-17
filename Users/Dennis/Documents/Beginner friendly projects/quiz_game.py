print("=" * 40)
print("    SIMPLE QUIZ GAME")
print("=" * 40)
print("\nAnswer the questions by typing a, b, c, or d\n")

score = 0


print("Question 1: What is the capital of Germany?")
print("a) Sofia")
print("b) Berlin")
print("c) Washington")
print("d) Paris")
answer1 = input("Your answer: ").lower()
if answer1 == "b":
    print("!!!Correct!!\n")
    score = score + 1
else:
    print(" EGH! Wrong! The answer is: b) Berlin\n" )
print("Question 2: When was Bulgaria created?")
print("a) 681 AD")
print("b) 1878 AD")
print("c) 1398 AD")
print("d) 1 BCE")
answer2 = input("Your answer: ").lower()
if answer2 == "a":
    print("!!!Correct!!\n")
    score = score + 1
else: 
    print(" EGH! Wrong! The answer is: a) 681 AD\n" )
print("Question 3: What is the biggest country in the world?")
print("a) France")
print("b) China")
print("c) USA")
print("d) Russia")
answer3 = input("Your answer: ").lower()
if answer3 == "d":
    print("!!!Correct!!\n")
    score = score + 1
else: 
    print(" EGH! Wrong! The answer is: d) Russia\n" )
print("Question 4: Which country has the biggest GDP in the world?")
print("a) China")
print("b) Russia")
print("c) USA")
print("d) United Kingdom")
answer4 = input("Your answer: ").lower()
if answer4 == "c":
    print("!!!Correct!!\n")
    score = score + 1
else: 
    print(" EGH! Wrong! The answer is: c) USA\n" )
print("Question 5: What is the most northern country in Europe?")
print("a) Norway")
print("b) Sweden")
print("c) Finland")
print("d) Denmark")
answer5 = input("Your answer: ").lower()
if answer5 == "a":
    print("!!!Correct!!\n")
    score = score + 1
else: 
    print(" EGH! Wrong! The answer is: d) Norway\n" )

print("=" * 40)
print(f"FINAL SCORE: {score} /5")
print("=" * 40)
if score == 5:
    print("🏆 PERFECT! You're a genius!")
elif score >= 4:
    print("⭐ Great job!")
elif score >= 3:
    print("👍 Not bad!")
elif score >= 2:
    print("📚 Keep studying!")
else:
    print("😅 Better luck next time!")



