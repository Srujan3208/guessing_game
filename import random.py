import random
import time
def game():
    attempt=0
    score=100
    num=random.randint(1,10)
    start=time.time()
    while score>0:        
        choice=int(input("Guess a number b/w (0 to 10):"))
        if(choice==num):
            print("Correct guess")
            break
        elif(choice<num):
            print("guess is to less")
            score-=10
            attempt+=1
        else:
            print("guess is to big")
            score-=10
            attempt+=1
    end=time.time()
    dur=end-start
    if score==0:
        print("Game is over!the number was",num)
    return score,attempt,dur

n=int(input("How many times you want to play:"))
total=0
best=0
attempts=1000
duration=10000
for i in range(1,n+1):
    score_,attempt_,dur_=game()
    print(f"game {i} score{score_}")
    print(f"number of atempts:{attempt_}")
    print(f"time taken:{dur_}")
    total+=score_
    if score_>best:
        best=score_
    if attempt_<attempts:
        attempts=attempt_
    if dur_<duration:
        duration=dur_
    print()
print("\n -----final result------")
print(f"total score:{total}")
print(f"average:{total/3}")
print(f"best score{best}")
print(f"best attempt:{attempts}")
print(f"time taken:{duration}")
