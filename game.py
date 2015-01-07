import random, sys

class Game():
    def __init__(self, category, level, word):
        self.category=category
        self.level=level
        self.word=word
        self.guessed_list=[] #list with letters already guessed by user
        self.word_construction=''
        self.nr_attempts=0 #nr_attempts depend of level
    
    def set_nr_attempts(self):
        #Define nr_attempts according to the level
        
        if self.level=="1":
            self.nr_attempts=5
        elif self.level=="2":
            self.nr_attempts=2
    
    def get_index(self, letter):
        #Return the indexes of the letter introduced by user on the word  
      
        count=self.word.count(letter)
        
        if count>0:  
            return [i for i, ltr in enumerate(self.word) if ltr == letter]
     
    def print_word(self, indexes, letter):
        #Print the word generated randomly
        
        if self.word_construction =='':
            for i in range(0, len(self.word)):
                self.word_construction +='_'
        else:        
            #replace the '_' characters per letter introduced by user
            s=list(self.word_construction)
                
            for i in indexes:
                s[i]=letter
                 
            #list->string
            self.word_construction=''.join(s)
            
            #return word
        return self.word_construction           
                   
         
    def guess_word_verification(self, letter):
        #Check if the letter inserted by user exists in the word generated randomly

        if letter in self.word:
            return True
        else:
            return False
 
    def sub_nr_attempts(self):
        #Decrement nr of attempts
        
        self.nr_attempts -=1
        return self.nr_attempts
    
    def add_guessed_list(self, letter):
        #Add to guessed_List the letter inserted by the user
        
        if letter in self.guessed_list:
            return False
        else:
            self.guessed_list.append(letter)
            return True
    
    def get_status_game(self):
        #Verify the status of the game through the nr of attempts and if the variable word_construction still has '_' character
        
        if self.nr_attempts==0:
            return False
        elif self.nr_attempts>0:
            if (self.word_construction.find("_")<0 and len(self.word_construction)>0):
                return False
            else:
                return True
        else:
            return False
                
def get_word(category, level):
    #Generate randomly the word according to the category
    
    cars=['FIAT', 'OPEL', 'PEUGEOT', 'RENAULT', 'TOYOTA', 'HONDA', 'NISSAN', 'VOLKSWAGEN', 'CHEVROLET', 'BMW', 'MERCEDES', 'CITROEN']
    colours=['PINK', 'YELLOW', 'WHITE', 'GREY', 'BLACK', 'GREEN', 'RED', 'BROWN', 'ORANGE', 'VIOLET', 'BLUE']
    countries=['CANADA', 'NICARAGUA', 'PANAMA', 'AUSTRALIA', 'BELIZE', 'ERITREA', 'MICRONESIA', 'SOMALIA', 'SWEDEN', 'INDIA']
        
    if category=='3':
        return (cars[random.randint(0,len(cars)-1)])
    elif category=='2':
        return (colours[random.randint(0,len(colours)-1)])
    elif category=='1':
        return (countries[random.randint(0,len(countries)-1)])        

def main():
    
    category=input("Please choose a category:\n 1 - Countries \n 2 - Colours \n 3 - Car Brands \n\n 0-Exit ")
    
    
    while (category<"0" or category>"3"):
        category=input("Please choose a category:\n 1 - Countries \n 2 - Colours \n 3 - Car Brands \n\n 0-Exit ")
    
    if category=="0":
        print("Bye.")
        sys.exit()
    
    level=input("Please choose your level: \n 1 - Beginner \n 2 - Intermediate \n\n 0-Exit ")
    
    while (level<"0" or level>"2"):
        level=input("Please choose your level: \n 1 - Beginner \n 2 - Intermediate \n\n 0-Exit ")
    
    if level=="0":
        print("Bye.")
        sys.exit()
        
    if (category!="0" and level!="0"):
            turn=Game(category, level,get_word(category, level))
            turn.set_nr_attempts()
            #print(turn.word)
            print(turn.print_word([],''))
            
            while turn.get_status_game() and turn.nr_attempts>0: #number of attemps>0
                
                letter=input("You have %d attempts. \nPlease choose a letter: \n"%turn.nr_attempts)
                letter=letter.upper()
                
                #add to guessed_list
                if len(turn.guessed_list)==0:
                    turn.add_guessed_list(letter)
                else:
                    while(not turn.add_guessed_list(letter)):#to avoid user could insert the same letter
                        print("You have choosen a word already choosen before.")
                        letter=input("You have %d attempts. \nPlease choose a letter: \n"%turn.nr_attempts)
                        letter=letter.upper()
                    
                #verify if the letter is in the word generated
                if(turn.guess_word_verification(letter)):
                    print("Good choice!")
                    word=turn.print_word(turn.get_index(letter), letter)
                    print(word)
                    
                else:
                    print("Bad choice!")
                    turn.sub_nr_attempts()
                    word=turn.print_word([], letter)
                    print(word)
            

            if (turn.nr_attempts>=0 and turn.word_construction.find("_")<0):
                print("You have just won! Congratulations!")
            elif turn.nr_attempts==0 and turn.word_construction.find("_")>=0:
                print("You have just lost. Sorry!\nThe word was %s"%turn.word)
            
              
if __name__=="__main__":
    main()