import random

chance = 4
anser = random.randint(1,20)
count = 1

while chance != 0 :
    num = int (input(f"기회가 {chance}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요 :"))
    if anser < num :
        print("Down")
    elif anser > num :
        print("Up")
    elif anser == num :
        print(f"축하합니다. {count}번만에 숫자를 맞히셨습니다")
        break
    chance -= 1
    count += 1
if chance == 0 :
    print(f"아쉽습니다. 정답은 {anser}였습니다.")