class QandA: 
    def __init__(self):
        self.healerAnswers = 0
        self.mageAnswers = 0
        self.warriorAnswers = 0
        self.suggestedClass = None
    
    questions = [["What's your favorite way to help your team?", "Bind their wounds and keep them safe", "Blast the bad guys with cool powers", "Jump into battle and protect everyone"],
                ["If you had a superpower, what would it be?","Healing anyone with a touch", "Controlling the elements", "Super strength"],
                ["What's your favorite kind of story?","One where the hero saves others with kindness", "One where the hero learns magic to defeat evil", "One where the hero fights monsters"],
                ["Which animal do you feel most like?","A gentle deer who watches over the forest", "A clever fox who knows secret paths", "A strong lion who protects the pride"],
                ["What is your favorite thing to do in a game?","Help your friends when they're in trouble", "Discover secrets and solve puzzles", "Fight monsters and win battles"],
                ["What kind of place would you live in?","A peaceful garden with glowing flowers", "A tall tower filled with magical books", "A strong castle with armor and weapons"],
                ["What do you do when someone gets hurt?","Run to help and make sure they're okay", "Think of a clever way to fix the problem", "Stand guard and make sure it doesn't happen again"],
                ["What's your favorite school subject?","Science or health- learning how things work and how to help", "Reading or art- using your imagination", "Gym or history- action and adventure"],
                ["What kind of teammate are you?","The one who cheers everyoneon and helps when needed", "The one who comes up with smart plans", "The one who leads the charge and keeps everyone safe"]]
    
    def suggestedClassResults(self):
        print(f"""Your results are: 
            Mage: {self.mageAnswers/9*100:.2f}%
            Healer: {self.healerAnswers/9*100:.2f}%
            Warrior: {self.warriorAnswers/9*100:.2f}%
            """)
        if self.healerAnswers == self.mageAnswers == self.warriorAnswers:
            print("You're a well rounded person! You would do well in any role!")
        else:
            maxScore = max(self.mageAnswers, self.healerAnswers, self.warriorAnswers)

            if maxScore == self.healerAnswers:
                print("You would make a great healer! You’re caring, gentle, and always looking out for others. You’re the heart of the team!")

            if maxScore == self.mageAnswers:
                print("You have the heart of a Mage. You’re curious, smart, and love using your brain and imagination. You’re the team’s magical powerhouse!")

            if maxScore == self.warriorAnswers:
                print("You are a warrior at heart. You’re brave, strong, and ready to charge into action. You’re the team’s fearless protector!")    
        # elif self.healerAnswers >= self.mageAnswers:
        #     if self.healerAnswers >= self.warriorAnswers:
        #         print("You would make a great healer! You’re caring, gentle, and always looking out for others. You’re the heart of the team!")
        #     if self.warriorAnswers >= self.mageAnswers:
        #         print("You are a warrior at heart. You’re brave, strong, and ready to charge into action. You’re the team’s fearless protector!")
        # else: print("You have the heart of a Mage. You’re curious, smart, and love using your brain and imagination. You’re the team’s magical powerhouse!")
    
    def incHealer(self):
        self.healerAnswers += 1
        print("Healer inreased: ",self.healerAnswers, "\n")
    
    def incMage(self):
        self.mageAnswers += 1
        print("Mage inreased: ",self.mageAnswers, "\n")

    def incWarrior(self):
        self.warriorAnswers += 1
        print("Warrior inreased: ",self.warriorAnswers, "\n")
