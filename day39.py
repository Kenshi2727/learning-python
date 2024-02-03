questions = [["Which language was used to create Facebook?", "Python", "Japanese", "JavaScript", "php", "None", 4],
             ["What is the capital of France?", "Paris", "Berlin", "Rome", "Madrid", "London", 1],
             ["Who wrote 'Romeo and Juliet'?", "William Shakespeare", "Jane Austen", "Charles Dickens", "Mark Twain",
              "Leo Tolstoy", 3],
             ["What is the currency of India?", "Indian Rupee", "Yen", "Euro", "Dollar", "Pound Sterling", 1],
             ["Which planet is known as the 'Red Planet'?", "Mars", "Venus", "Jupiter", "Saturn", "Neptune", 2],
             ["What is the largest mammal on Earth?", "Blue Whale", "Elephant", "Giraffe", "Hippopotamus", "Lion", 3],
             ["In which year did World War II end?", "1945", "1939", "1941", "1943", "1947", 4],
             ["Who is the current President of the United States?", "Joe Biden", "Donald Trump", "Barack Obama",
              "George W. Bush", "Bill Clinton", 2],
             ["What is the capital of Japan?", "Tokyo", "Beijing", "Seoul", "Bangkok", "Hanoi", 5],
             ["Which ocean is the largest?", "Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean",
              "Southern Ocean", 1],
             ["What is the currency of Brazil?", "Brazilian Real", "Euro", "Pound Sterling", "Yen", "US Dollar", 4],
             ["Who painted the Mona Lisa?", "Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Claude Monet",
              "Michelangelo", 5],
             ["What is the speed of light?", "299,792 kilometers per second", "150,000 kilometers per second",
              "400,000 kilometers per second", "200,000 kilometers per second", "500,000 kilometers per second", 4],
             ["In which year did the Titanic sink?", "1912", "1905", "1915", "1920", "1902", 1]
             ]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
i = 0
print("=========================Welcome to the Quiz Competition=============================")
for i in range(0, len(questions)):
    question= questions[i]
    print(f"\n\nQuestion for ₹{levels[i]}")
    print(question[0])
    # print(f"a. {questions[i][1]}               b. {questions[i][2]} ")
    # print(f"c. {questions[i][3]}               d. {questions[i][4]} ")
    print(f"a. {question[1]}               b. {question[2]} ")
    print(f"c. {question[3]}               d. {question[4]} ")
    reply = int(input("Enter your answer(1-4):"))
    if reply == question[-1]:
        print(f"Correct answer, you have won ₹{levels[i]}")
        if i == 4:
            money = 10000  # guranteed money after solving 5 questions correctly
        elif i == 9:
            money = 320000
        elif i == 14:
            money = 10000000
    else:
        print("Wrong answer!!!Now get out of here!!!!")
        break
print(f"Your take home money is ₹{money},Now get out!!")
