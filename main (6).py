class Player:
 def play(self): 
  print("The player is playing cricket")
class Batsman (Player): 
 def play(self): 
  print("The batsman is batting")
player = Player() 
batsman = Batsman()
player.play()
batsman.play()