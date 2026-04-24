from itertools import combinations,permutations
entrances=[0,0]
PowersOfEnemies=0
NumberOfWays=0
def sol(powers,index):
	if index==len(powers):
		global NumberOfWays
		NumberOfWays+=1
		return 
	for i in range(2):
		if i==0 and entrances[0]+powers[index]>entrances[1]:
			continue
		entrances[i]+=powers[index]
		sol(powers,index+1)
		entrances[i]-=powers[index]
N=int(input())
if N==0:
	print('%i %i'%(1,0))
	print('We will win!')
else:
	PowersOfEnemies=[int(x) for x in input().split()]
	TotalPowerOfEnemies=sum(s for s in PowersOfEnemies)
	arrangements=list(map(list,permutations(PowersOfEnemies)))
	for arrangement in arrangements:
		entrances=[0,0]
		sol(arrangement,0)
	print('%i %i'%(NumberOfWays,TotalPowerOfEnemies))
	print('We will win!' if NumberOfWays>TotalPowerOfEnemies else 'Got no way out!')
