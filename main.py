try:
    def game():
        new=input("press 1 to start and 0 for quit the game:")
        if new=="0":
            print("Thanks for visiting us:")
            return
        elif new=="1":
            print("welcome to the quiz game:")
            print("Lets Start")
        else:
            print("Invalid Output")
            return
        questions=[["who is prime minister of India?", "Narendra Modi", "Rahul Gandhi", "Amit shah", "Manmohan Singh", 1],
            ["what is the capital of India?","Mumbai", "Kolkata","New Delhi","Chennai", 3],
            ["what is the national animal of India?", "Lion", "Tiger","Elephant", "Peacock", 2],
            ["what is the national bird of India?", "Sparrow", "Peacock", "Parrot", "Eagle", 2],
            ["what is the national flower of India?", "Rose", "Lily", "Marigold","Lotus", 4],
            ["How many colours present in our Flag", "2","3","4","7",3],
            ["Python language used for what purpose","Coding","Editing","Filming","Nothing",1],
            ["How many states in India","23","34","28","29",4],
            ["Who is the CM of Punjab","Amit Shah","Narendra Modi","Bhagwant Maan","Rahul Gandhi",3],
            ["What is the currency of India?", "Dollar", "Rupee", "Euro", "Yen", 2],
            ["Who wrote the Indian National Anthem?", "Rabindranath Tagore", "Bankim Chandra", "Mahatma Gandhi", "Subhash Chandra Bose", 1],
            ["What is the national sport of India?", "Cricket", "Hockey", "Football", "Kabaddi", 2],
            ["How many planets are there in our solar system?", "7", "8", "9", "10", 2],
            ["What is the full form of CPU?", "Central Processing Unit", "Computer Personal Unit", "Central Program Utility", "Control Processing Unit", 1],
            ["Which is the largest state in India by area?", "Maharashtra", "Rajasthan", "Madhya Pradesh", "Uttar Pradesh", 2],
            ["Who is known as the Father of the Nation in India?", "Jawaharlal Nehru", "Mahatma Gandhi", "Sardar Patel", "Bhagat Singh", 2],
            ["What does HTML stand for?", "Hyper Text Markup Language", "High Tech Modern Language", "Hyper Transfer Markup Language", "Home Tool Markup Language", 1],
            ["Which river is known as the Ganga of the South?", "Godavari", "Krishna", "Cauvery", "Narmada", 1],
            ["In which year did India get independence?", "1945", "1947", "1950", "1942", 2],
            ["What is the chemical symbol for water?", "H2O", "CO2", "O2", "NaCl", 1]]
        sum=0
        for question in questions:
            print(question[0])
            print(f"1.{question[1]}")
            print(f"2.{question[2]}")
            print(f"3.{question[3]}")
            print(f"4.{question[4]}")
            try:
                a=int(input("enter your choice: "))
                if a==question[5]:
                    print("Correct awnser:")
                else:
                    print(f"Wrong awnser,the awnser is {question[5]}")
                    print("Better luck next time.")
                    print("Thanks for playing this quiz game:")
                    break
                sum+=1000
                print("You won",sum)
            except ValueError as e:
                print("Please choose your awnser in integer not in string like press 1 for first: ")
    game()
except Exception as e1:
    print(f"Error found: {e1}")
