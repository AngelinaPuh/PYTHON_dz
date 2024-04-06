import random
timeList =["Сегодня", "Завтра", "Очень скоро"]
eventList = ["вы встретите", "с вами случится", "вы найдёте"]
objectList = ["что-то волшебное", "необычный инцидент", "большой сюрприз"]
zodiac =["овен","телец","близнецы","рак", "лев", "дева", "весы", "скорпион","стрелец", "козерог", "водолей", "рыбы"]

while True:
   zodiac_sign = input("Введите ваш знак зодиака: ").lower()
   if zodiac_sign in zodiac:
      print("Знак зодиака введен правильно!")
      time = timeList[random.randint(0, len(timeList) - 1)]
      event = eventList[random.randint(0, len(eventList) - 1)]
      object = objectList[random.randint(0, len(objectList) - 1)]
      print(time + " " + event + " " + object)
      next = input("хотите попробовать ещё раз?")
      if next.lower() != "да" :
         break
   else:
      print("Вы ввели неправильный знак зодиака. Пожалуйста, попробуйте ещё раз.")
   
print("Приходите ещё за новыми предсказаниями!")