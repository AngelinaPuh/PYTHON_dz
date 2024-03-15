import random
const = random.randint(1, 20)
print("Я загадал число, попробуйте угадасть ")
user = int(input("ведите число \n"))
while const != user:
    if const+2 > user and user > const or  const-2 < user and user < const:
        print("Горячо! \n")
    elif const+4 > user and user > const or  const-4 < user and user < const:
        print("Тепло~ \n")
    else:
        print("Холодно...")
    user = int(input("попробуй еще раз \n"))
print(f"Ты угадал! моё число: {const}") 