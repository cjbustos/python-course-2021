import statistics

score_1 = float(input("Please, write the first score:"))
score_2 = float(input("Write the second score:"))

# int, float, bool, str
# dict, tuple, list

average = statistics.mean([score_1, score_2])
print("The average is:", average)

if average >= 4:
    print("Congrats, you pass!")
else:
    print("Good luck for next try!")