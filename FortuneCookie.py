import random

fortunes = ["You will have a great day!", "Pursue your dreams with vigour.", "It may be difficult, but it will be worth it in the end.", 
            "Work with what you have.", "Fame and fortune lie ahead.", "Take care of yourself first. Then help others.", 
            "If you have an idea, make it into a reality.", "Work with your destiny. Stop trying to outrun it.", "An exciting adventure awaits you!"]

RandomFortune = random.choice(fortunes)

LuckyNumber = (random.randint(1,100))

print(f"{RandomFortune} Your lucky number is: {LuckyNumber}")