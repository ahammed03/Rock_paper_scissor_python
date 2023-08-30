class Game:
    def __init__(self):
        self.user_score=0
        self.computer_score=0
        self.options=["rock","paper","scissor"]
    def func(self):
        import random
        return random.choice(self.options)
    def output(self,user_choice):
        self.user_choice=user_choice
        if (self.user_choice=="rock" and self.func()=="scissor") or (self.user_choice=="scissor" and self.func()=="paper" ) or (self.user_choice=="paper" and self.func()=="rock"):
            self.user_score+=1 
            print('''
            your choice : {}
            computer choice : {}
            Computer Lose
            Your Score :- {}
            Computer Score :- {}'''.format(user_choice,self.func(),self.user_score,self.computer_score))
        elif (self.user_choice=="rock" and self.func()=="rock") or (self.user_choice=="scissor" and self.func()=="scissor") or (self.user_choice=="paper" and self.func()=="paper"):
            print('''
                  No one got any points''')
        elif (self.user_choice=="rock" and self.func()=="paper") or (self.user_choice=="scissor" and self.func()=="rock") or (self.user_choice=="paper" and self.func()=="scissor"):
            self.computer_score+=1 
            print('''
            your choice : {}
            computer choice : {}
            Computer won
            Your Score :- {}
            Computer Score :- {}'''.format(user_choice,self.func(),self.user_score,self.computer_score))
    def final_(self):
        if self.user_score==self.computer_score:
            print('''GAME DRAW 3
Both have Equal Scores''')
        elif self.user_score<self.computer_score:
            print('''COmputer Won the Game
You got {} less points than computer'''.format(self.computer_score-self.user_score)) 
        else:
            print('''You Won the Game
You got {} more points than computer'''.format(self.user_score-self.computer_score))
        return "Thank You for Playing"
obj=Game()
c=0
print("\nWelcome Rock Paper Scissor Game ")
while True:
    print('''   
          Choose your Option
          0- rock
          1- Paper
          2- Scissor
          5 for EXIT''')
    options=["rock","paper","scissor"]
    user_input=int(input())
    c+=1
    if c>5:
        print(obj.final_())
        break
    if user_input==5:
        print("Thank You")
        break 
    elif user_input>2:
       print("Sorry u choose wrong option")
       break
    else:
        obj.output(options[user_input])
    
    
    
    
                
            
    
        

        
        