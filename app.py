#import questions
from qa import QandA

# class QandA: 
#     def __init__(self):
#         self.healerAnswers = 0
#         self.mageAnswers = 0
#         self.warriorAnswers = 0
#         self.suggestedClass = None
    
#     questions = [["What's your favorite way to help your team?", "Bind their wounds and keep them safe", "Blast the bad guys with cool powers", "Jump into battle and protect everyone"],
#                 ["If you had a superpower, what would it be?","Healing anyone with a touch", "Controlling the elements", "Super strength"],
#                 ["What's your favorite kind of story?","One where the hero saves others with kindness", "One where the hero learns magic to defeat evil", "One where the hero fights monsters"],
#                 ["Which animal do you feel most like?","A gentle deer who watches over the forest", "A clever fox who knows secret paths", "A strong lion who protects the pride"],
#                 ["What is your favorite thing to do in a game?","Help your friends when they're in trouble", "Discover secrets and solve puzzles", "Fight monsters and win battles"],
#                 ["What kind of place would you live in?","A peaceful garden with glowing flowers", "A tall tower filled with magical books", "A strong castle with armor and weapons"],
#                 ["What do you do when someone gets hurt?","Run to help and make sure they're okay", "Think of a clever way to fix the problem", "Stand guard and make sure it doesn't happen again"],
#                 ["What's your favorite school subject?","Science or health- learning how things work and how to help", "Reading or art- using your imagination", "Gym or history- action and adventure"],
#                 ["What kind of teammate are you?","The one who cheers everyoneon and helps when needed", "The one who comes up with smart plans", "The one who leads the charge and keeps everyone safe"]]
    
#     def suggestedClassResults(self):
#         print(f"""Your results are: 
#             Mage: {self.mageAnswers/9*100}%
#             Healer: {self.healerAnswers/9*100}%
#             Warrior: {self.warriorAnswers/9*100}%
#             """)

#         if self.healerAnswers >= self.mageAnswers:
#             if self.healerAnswers >= self.warriorAnswers:
#                 print("You would make a great healer! You’re caring, gentle, and always looking out for others. You’re the heart of the team!")
#             if self.warriorAnswers >= self.mageAnswers:
#                 print("You are a warrior at heart. You’re brave, strong, and ready to charge into action. You’re the team’s fearless protector!")
#         else: print("You have the heart of a Mage. You’re curious, smart, and love using your brain and imagination. You’re the team’s magical powerhouse!")
    
#     def incHealer(self):
#         try:
#             self.healerAnswers += 1
#             print("Healer inreased: ",self.healerAnswers)
#         except Exception as e:
#             print("Exception: ", e)
    
#     def incMage(self):
#         self.mageAnswers += 1
#         print("Mage inreased: ",self.mageAnswers)

#     def incWarrior(self):
#         self.warriorAnswers += 1
#         print("Warrior inreased: ",self.warriorAnswers)

class Student:
    def __init__(self, name, charClass):
         self.name = name
         self.charClass=  charClass
         print(f"New character created! {self.name}, the {self.charClass}")



def mainFunction():
    quiz = QandA()
    askQuestions(quiz)
    quiz.suggestedClassResults()
    createCharacter()


def askQuestions(quiz):
    qa = questionGenerator(quiz.questions)
    try:
        for i in range(len(quiz.questions)):
            currentQ = next(qa)
            print(currentQ[0])
            print("a: ", currentQ[1])
            print("b: ", currentQ[2])
            print("c: ", currentQ[3])
            
            goodAnswer = False

            while goodAnswer == False: 
                print("Type 'a', 'b' or 'c' to indicate your answer.")
                answer = input()
                try: 
                    match answer:
                        case "a":
                            goodAnswer = True
                            quiz.incHealer()
                            
                        case "b":
                            goodAnswer = True
                            quiz.incMage()
                            
                        case "c":
                            goodAnswer = True
                            quiz.incWarrior()
                        case _:
                            raise Exception
                except:
                    print("That is not one of the options.")
    except Exception as e:
        print("exception: ",e)


def questionGenerator(questions):
    for i in questions:
        yield i


def createCharacter():
    print("What is your name?")
    studentName = input()

    goodAnswer = False
    
    while goodAnswer == False: 
        print("""What class would you like to be?
          a. Healer
          b. Mage
          c. Warrior
          Type 'a', 'b', or 'c' to indicate your answer.
          """)
        charClass = input()
        try: 
            match charClass:
                case "a" | "b" | "c":
                    goodAnswer = True
                case _:
                    raise Exception
        except:
            print("That is not one of the options.")
        
    if charClass == "a":
        charClass = "Healer"
    elif charClass == "b":
        charClass = "Mage"
    elif charClass == "c":
        charClass = "Warrior"

    newStudent = Student(studentName, charClass)

mainFunction()