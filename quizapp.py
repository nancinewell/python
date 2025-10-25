import tkinter as tk

# # # # # # # # # # # # # # # # MAIN FUNCTION # # # # # # # # # # # # # # # # 
def main():
    app = Application()
    app.mainloop()

# # # # # # # # # # # # # # # # APPLICATION # # # # # # # # # # # # # # # # 
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        #set app title
        self.title("Character Quiz")
        #set size of app
        self.geometry('400x400')

        #set frame configuration
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        #run the quiz in the frame
        frame1 = RunQuiz(self)
        frame1.grid(row = 0, column = 0, sticky="new", padx = 15, pady = 15)

        
# # # # # # # # # # # # # # # # RUN QUIZ # # # # # # # # # # # # # # # # 
#class to contain the quiz experience
class RunQuiz(tk.Frame):
    #init function is a setup quiz function
    def __init__(self, parent):
        super().__init__(parent)
        #configure rows/columns
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        #welcome question 
        self.welcomeLabel = tk.Label(self, text = "Let's figure out what kind of character would you like to be!", font= ("Times New Roman", 18), wraplength=350, pady = 15)
        self.welcomeLabel.grid(row = 0, column = 0, pady = 5)
 
        #Get started button
        self.entryBtn = tk.Button(self, text = "Let's Get Started!", font = ("Times New Roman", 14), command = self.startQuiz) 
        self.entryBtn.grid(row = 1, column = 0, pady = 10)

    #function to start the quiz
    def startQuiz(self):
        #destroy the welcome elements 
        self.welcomeLabel.destroy()
        self.entryBtn.destroy()
        #instantiate QandA
        self.quiz = QandA()
        #put the questions in a generator
        self.qa = self.listGenerator(self.quiz.questions)
        #start the frameQuestions function to continue
        self.frameQuestions()

    #function to display questions with radio buttons one at a time
    def frameQuestions(self):
        #put the next question with radio options and a submit button into a frame. 
        currentQ = next(self.qa)
        #frame to hold the contents
        frame = tk.Frame(self)
        frame.grid(row = 0, column = 0, pady = 15)
        #ask the question
        qLabel = tk.Label(frame, text = currentQ[0], font = ("Times New Roman", 14))
        qLabel.grid(row = 0, column = 0)

    #radio buttons with answer options.
        #var to store the answer.
        r =  tk.StringVar()
        #buttons
        a1 = tk.Radiobutton(frame, text = currentQ[1], variable = r, value = "1", font = ("Times New Roman", 12), anchor = "w", command = lambda: self.logAnswer(r.get(), frame),wraplength=350, justify="left") 
        a2 = tk.Radiobutton(frame, text = currentQ[2], variable = r, value = "2", font = ("Times New Roman", 12), anchor  = "w", command = lambda: self.logAnswer(r.get(), frame),wraplength=350, justify="left")
        a3 = tk.Radiobutton(frame, text = currentQ[3], variable = r, value = "3", font = ("Times New Roman", 12), anchor = "w", command = lambda: self.logAnswer(r.get(), frame),wraplength=350, justify="left")
        #display the pieces
        a1.grid(row = 1, column = 0, sticky="ew")
        a2.grid(row = 2, column = 0, sticky = "ew")
        a3.grid(row = 3, column = 0, sticky = "ew")

    #function to destroy things
    def destroyThing(self, thing):
        thing.destroy()
            
    #generator function to get just one question at a time.          
    def listGenerator(self, list):
        for i in list:
            yield i
    
    #function to log the answer and ask another question (if there is one)
    def logAnswer(self, answer, frame):
        try: 
            #if there is an answer, increment the appropriate charClass counter
            match answer:
                    case "1":
                        self.quiz.incHealer()
                    case "2":
                        self.quiz.incMage()
                    case '3':
                        self.quiz.incWarrior()
                    case _:
                        raise Exception
            #clear the screen
            self.destroyThing(frame)
            #get another question- if there aren't any, it will trigger an exception
            self.frameQuestions()
        #when there are no more questions, call displayAnswer()
        except Exception:
            self.displayAnswer()

    #function to display answer results
    def displayAnswer(self):
        #a frame to put stuff in
        frame = tk.Frame(self)
        frame.grid(row = 0, column = 0)
        #get the suggested class results
        self.quiz.suggestedClassResults()
        #display data
        resultsText = f"""Your results are: 
        Healer: {self.quiz.healerAnswers/9*100:.2f}%
        Mage: {self.quiz.mageAnswers/9*100:.2f}%
        Warrior: {self.quiz.warriorAnswers/9*100:.2f}%\n\n
        """
        #concat flavor text
        for i in self.quiz.suggestedClass:
            match i:
                case "None":
                    resultsText += "You're a well rounded person! You would do well in any role!"
                case "Healer":
                    resultsText +="You would make a great healer! You’re caring, gentle, and always looking out for others. You’re the heart of the team!\n\n"
                case "Mage":
                    resultsText += "You have the heart of a Mage. You’re curious, smart, and love using your brain and imagination. You’re the team’s magical powerhouse!\n\n"
                case "Warrior":
                    resultsText += "You are a warrior at heart. You’re brave, strong, and ready to charge into action. You’re the team’s fearless protector!"
                case _:
                    resultsText += " "
        #display the results!        
        resultsLabel = tk.Label(frame, text = resultsText, font = ("Times New Roman", 14),wraplength=350)
        resultsLabel.grid(row = 1, column = 0, sticky="new")
        #Button to continue
        continueBtn = tk.Button(frame, text = "Continue", font = ("Times New Roman", 14), command = lambda: self.gatherStudentInfo(frame))
        continueBtn.grid(row = 2, column = 0)

    #function to gather student info
    def gatherStudentInfo(self, toDestroy):
        #clear the screen
        self.destroyThing(toDestroy)
        #create new frame to put stuff in
        frame = tk.Frame(self)
        frame.grid(row = 0, column = 0)
        #Gather Student Info
        nameLabel = tk.Label(frame, text = "What is your name?", font = ("Times New Roman", 14))
        nameLabel.grid(row = 1, column = 0, sticky = "ew")

        nameEntry = tk.Entry(frame, font = ("Times New Roman", 14), bd = 5, relief="flat", borderwidth=10)
        nameEntry.grid(row = 2, column = 0, sticky = "ew")

        classLabel = tk.Label(frame, text = "What class would you like to play?", font = ("Times New Roman", 14))
        classLabel.grid(row = 4, column = 0, sticky = "ew")
        #radio buttons to select charClass
        r =  tk.StringVar()
        
        a1 = tk.Radiobutton(frame, text = "Healer", variable = r, value = "Healer", font = ("Times New Roman", 12), anchor = "w", command = lambda: self.createStudent(r.get(), nameEntry.get(), frame),wraplength=350) 
        a2 = tk.Radiobutton(frame, text = "Mage", variable = r, value = "Mage", font = ("Times New Roman", 12), anchor  = "w", command = lambda: self.createStudent(r.get(), nameEntry.get(),frame),wraplength=350)
        a3 = tk.Radiobutton(frame, text = "Warrior", variable = r, value = "Warrior", font = ("Times New Roman", 12), anchor = "w", command = lambda: self.createStudent(r.get(), nameEntry.get(),frame),wraplength=350)
        
        a1.grid(row = 5, column = 0, sticky="ew")
        a2.grid(row = 6, column = 0, sticky = "ew")
        a3.grid(row = 7, column = 0, sticky = "ew")
    
    #function to create the student based on gathered info
    def createStudent(self, charClass, name, toDestroy):
         #clear the screen
        self.destroyThing(toDestroy)
        #create new student based on gathered info
        student = Student(name, charClass)
        #frame to put stuff in
        frame = tk.Frame(self)
        frame.grid(row = 0, column = 0)    
        #Kudos message
        studentLabel = tk.Label(frame, text = f"Welcome {student.name}, the newest {student.charClass} to join the ranks!", font = ("Times New Roman", 14),wraplength=350)
        studentLabel.grid(row = 0, column = 1)

    
# # # # # # # # # # # # # # # # STUDENT CLASS # # # # # # # # # # # # # # # # 
class Student:
    def __init__(self, name, charClass):
         self.name = name
         self.charClass=  charClass


# # # # # # # # # # # # # # # # QANDA CLASS # # # # # # # # # # # # # # # # 
class QandA(tk.Tk): 
    def __init__(self):
        #counters to keep track of answers
        self.healerAnswers = 0
        self.mageAnswers = 0
        self.warriorAnswers = 0
        #list of suggested class(es)- possible to have more than one
        self.suggestedClass = []
    #questions to ask the user
    questions = [["What's your favorite way to help your team?", "Bind their wounds and keep them safe", "Blast the bad guys with cool powers", "Jump into battle and protect everyone"],
                ["If you had a superpower, what would it be?","Healing anyone with a touch", "Controlling the elements", "Super strength"],
                ["What's your favorite kind of story?","One where the hero saves others with kindness", "One where the hero learns magic to defeat evil", "One where the hero fights monsters"],
                ["Which animal do you feel most like?","A gentle deer who watches over the forest", "A clever fox who knows secret paths", "A strong lion who protects the pride"],
                ["What is your favorite thing to do in a game?","Help your friends when they're in trouble", "Discover secrets and solve puzzles", "Fight monsters and win battles"],
                ["What kind of place would you live in?","A peaceful garden with glowing flowers", "A tall tower filled with magical books", "A strong castle with armor and weapons"],
                ["What do you do when someone gets hurt?","Run to help and make sure they're okay", "Think of a clever way to fix the problem", "Stand guard and make sure it doesn't happen again"],
                ["What's your favorite school subject?","Science or health- learning how things work and how to help", "Reading or art- using your imagination", "Gym or history- action and adventure"],
                ["What kind of teammate are you?","The one who cheers everyoneon and helps when needed", "The one who comes up with smart plans", "The one who leads the charge and keeps everyone safe"]]
    #function to determine suggested class(es) based on answers to questions
    def suggestedClassResults(self):
        #if results are evenly spread answers, no suggested class
        if self.healerAnswers == self.mageAnswers == self.warriorAnswers:
            self.suggestedClass.append("None")
        else:
            #find the answer type with the most
            maxScore = max(self.mageAnswers, self.healerAnswers, self.warriorAnswers)
            #if healer is most, add healer to the suggested class results
            if maxScore == self.healerAnswers:
               self.suggestedClass.append("Healer")
            #if mage is most, add mage to the suggested class results
            if maxScore == self.mageAnswers:
                self.suggestedClass.append("Mage")
            #if warrior is most, add warrior to the suggested class results
            if maxScore == self.warriorAnswers:
                self.suggestedClass.append("Warrior")

    #function to increment healerAnswers
    def incHealer(self):
        self.healerAnswers += 1
        print("Healer inreased: ",self.healerAnswers, "\n")

    #function to increment mageAnswers
    def incMage(self):
        self.mageAnswers += 1
        print("Mage inreased: ",self.mageAnswers, "\n")
#function to increment warriorAnswers
    def incWarrior(self):
        self.warriorAnswers += 1
        print("Warrior inreased: ",self.warriorAnswers, "\n")


#run the program!
if __name__ == "__main__":
    main()
