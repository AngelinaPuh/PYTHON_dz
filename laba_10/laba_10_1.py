rightCounter = 0
questionsCounter = 0 
questions = ["сколько цветов у радуги? ", "какой язык мы изучаем? ", "какой сейчас год? ", "в какой группе мы учимся? ", "какой сегодня день недели? "]
rightAnswers = ["7", "python", "2024", "п21", "суббота"]
while questionsCounter < len(questions):
 answer = input(questions[questionsCounter])
 if answer.lower() == rightAnswers[questionsCounter]:
    rightCounter += 1
 questionsCounter += 1
print(f"вы набрали баллов: {rightCounter}")