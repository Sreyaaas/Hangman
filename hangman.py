import random
list=["sourav","devaj","akil","bis","joel","ameen","jazeel","dean",'ojas',"tanya","shivani","nayana","praveen","sagar","sreyas"]
word=random.choice(list)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

number=len(word)
display=[]

for i in range(number):
  display+="_"

print('''_                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/   ''')
# print(word)
eog=False

lives=6

name=input("Enter your name: ")
print(" ")
while not eog:
  choice1=input("Guess a letter: ").lower()
  
  for i in range(number):
    letter=word[i]
    if letter==choice1:
      display[i]=letter
  # print(display)
  print(stages[lives])

  print(f"{' '.join(display)}")
  if choice1 not in word:
    lives-=1
    if lives==0:
      eog=True
      print('''
      __   __           __             __  __
      \ \ / /___ __ __  | |    ___  ___| |_| |
       \ V / _ \| | | | | |   / _ \/ __| __| |
        | | (_) | |_| | | |__| (_) \__ | |_|_|
        |_|\___/ \__,_| |_____\___/|___/\__(_)
   ''')
      print(f"You've Lost {name}!")
      print(f"The right answer was: {word}")
      

  if "_" not in display:
    eog=True
    print(f"You've Won {name}!")
    print('''
__  __               _       _             __ 
\ \/ /___  __  __   | |     / /___  ____  / /
 \  / __ \/ / / /   | | /| / / __ \/ __ \/ / 
 / / /_/ / /_/ /    | |/ |/ / /_/ / / / /_/  
/_/\____/\__,_/     |__/|__/\____/_/ /_(_)   
                                             
    ''')


  


