from sys import exit
from random import *

def gold_room(): 
  print("This room is full of gold. How much do you take?") 
  choice = input("> ")
  #if "0" in choice or "1" in choice:               Não faz sentido com a pergunta.
  how_much = int(choice)
  #else: 
    #dead("Man, learn to type a number.") 
  if how_much < 50:
    print("Nice, you're not greedy, you win!") 
    exit(0)
  elif how_much > 50: 
    dead("You greedy bastard!")
  else: 
    dead("Man, learn to type a number.") 

def bear_room():
  print("There is a bear here.")
  print("The bear has a bunch of honey.")
  print("The fat bear is in front of another door.")   
  print("How are you going to move the bear?") 
  bear_moved = False
  while True: 
    choice = input("> ")
    if choice == "take honey":
     dead("The bear looks at you then slaps your face off.")
    elif choice == "taunt bear" and not bear_moved: 
      print("The bear has moved from the door.")
      print("You can go through it now.") 
      bear_moved = True
    elif choice == "taunt bear" and bear_moved:
      dead("The bear gets pissed off and chews your leg off.") 
    elif choice == "open door" and bear_moved: 
      gold_room()
    else: 
      print("I got no idea what that means.")

def cthulhu_room(): 
  print("Here you see the great evil Cthulhu.")
  print("He, it, whatever stares at you and you go insane.") 
  print("Do you flee for your life or eat your head?")
  choice = input("> ")
  if "flee" in choice: 
    start()
  elif "head" in choice: 
    dead("Well that was tasty!")
  else:
    cthulhu_room()

def bridge_room():
  print("You see a long wooden bridge")
  print("Before the bridge there is a sword")
  print("What do you do?")
  sword = False
  while True:
    choice = input("> ")
    guardHP = 10
    playedHP = 10
    if "grab sword" in choice:
      sword = True
      print("What do you do?")
    #START COMBAT
    elif "cross the bridge" in choice:
      print("As you cross the brige you see a guard in the middle of the bridge")
      print("He stops you and is read to fight")
      print(" O |")
      print("/|\T ")
      print("/ \.")
      while True:
        print(f"Vida atual: {playedHP}")
        print(f"Vida atua do guarda: {guardHP}")
        print("What do you do?")
        choice2 = input("> ")
        if "attack" in choice2:
          
          playedHit = randint(0,1)
          guardHit = randint(0,1)
          guardDef = randint(0,1)
          
          if sword == True:
            if guardDef == 1:
              print("Guard defended")
              guardHP -= 0
              playedHP -= 0
            elif playedHit == 1:
              print("You hit the guard")
              guardHP -= 2
              if guardHit == 1:
                print("The guard hit you")
                playedHP -= 2
            elif guardHit == 1:
                print("The guard hit you")
                playedHP -= 2
            else:
                print("Both you and the guard missed")
                
          else:
            if guardDef == 1:
              print("Guard defended")
              guardHP -= 0
              playedHP -= 0
            elif playedHit == 1:
              print("You hit the guard")
              guardHP -= 1
              if guardHit == 1:
                print("The guard hit you")
                playedHP -= 2
            elif guardHit == 1:
                print("The guard hit you")
                playedHP -= 2
            else:
                print("Both you and the guard missed")
              
        elif "defend" in choice2:
          playedHP -= 0
          
        elif "heal" in choice2:
          guardHit = randint(0,1)
          
          if guardHit == 1:
            playedHP -= 1
          else:
            playedHP += 2
            
        else:
          print("I got no idea what that means.")
        #END COMBAT  
        
        if playedHP == 0:
          dead("The guard kills you")
        if guardHP == 0:
          print("You killed the guard and crossed the bridge.")
          gold_room()
          
    else:
      print("I got no idea what that means.")
      
def dead(why):
  print(why, "Good job!") 
  exit(0)

def start(): 
  print("You are in a dark room.")
  print("There is a door to your right, left and foward.") 
  print("Which one do you take?")
  choice = input("> ")
  if choice == "left": 
    bear_room()
  elif choice == "right": 
    cthulhu_room()
  elif choice == "foward": 
    bridge_room()
  else: 
    dead("You stumble around the room until you starve.")

#start()
bridge_room()