import random
import tools

while(True):    
    tools.play_game()
    play_again:str = input("您還要繼續嗎(y,n)?")
    if play_again == "n":
        break
    
    

print("猜數字遊戲結束")
    