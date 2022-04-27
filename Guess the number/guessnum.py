import random
logo="""
_____                       _____ _            _   _                 _               
|  __ \                     |_   _| |          | \ | |               | |              
| |  \/_   _  ___  ___ ___    | | | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
| | __| | | |/ _ \/ __/ __|   | | | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
| |_\ \ |_| |  __/\__ \__ \   | | | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
 \____/\__,_|\___||___/___/   \_/ |_| |_|\___| \_| \_/\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                      
"""
print(logo)

def guess():
	nums=random.randint(1,100)
	return nums

def check(chknum):
	if chknum==gus:
		return f"You got the answer the correct answer is :{gus}, You Win..."
	elif chknum>gus:
		return "Too High..."
	elif chknum<gus:
		return "Too Low..."

print("Welcome to my guessing game...\nI'm thinking a number between 1 to 100.\nGuess the number...")
mode=input("\nChoose your Difficulty level (easy / hard) : ")
count=False
atpmt=0
gus=guess()

if mode=="easy":
	atpmt=10
elif mode=="hard":
	atpmt=5
else:
	print("Invalid Input..")

while count!=True:
	player_num=int(input())
	print(check(player_num))
	if player_num==gus:
		count=True
		
	atpmt-=1
	print(f"\nYou have {atpmt} attempts...\nGuess Again : ")
	if atpmt==0:
		count=True
