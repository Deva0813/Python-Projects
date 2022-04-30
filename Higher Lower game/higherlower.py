import random
from game_data import data
from art import logo
from art import vs
from replit import clear

def pick1():
	a=random.choice(total)
	return a

def chk(f1,f2):
	if f1>f2:
		return 'A'
	elif f1<f2:
		return 'B'


cout=False
score=0

while cout!=True:
		clear()
		total=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]
		print(logo)
		print("\nYour Score : ",score,"\n")
	
		ind=pick1()
		total.remove(ind)
		compprt= f"{data[ind]['name']},{data[ind]['description']},{data[ind]['country']}"
		
		print("Compare A : ",compprt)
		print(vs)
		
		ind1=pick1()
		compprt= f"{data[ind1]['name']},{data[ind1]['description']},{data[ind1]['country']}"
		
		print("Compare B : ",compprt)
		
		follower1=data[ind]['follower_count']
		follower2=data[ind1]['follower_count']
		ans=chk(follower1,follower2)
		
		pick=input("\nWho as more followers 'A' or 'B' : ")
		pick=pick.upper()
	
		if pick!=ans:
				print("\nYour answer is Worng...")
				cout=True
			
		score+=1
