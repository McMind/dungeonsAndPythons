def clear():
	print(27 * "\n")

class player():
	def __init__(self):
		self.pos = [1,1]
		self.ico = 'P'
	def show_pos(self):
		return str(self.pos[0]) + ',' + str(self.pos[1])
	def check_pos(self,size):
		x = range(1,size[0] + 1)
		y = range(1,size[1] + 1)
		if(self.pos[0] in x and self.pos[1] in y):
			return True
		else:
			return False
	def move(self,direction,size):
		for i in range(len(direction)):
			if(self.check_pos(size)):
				match direction[i]:
					case 'w':
						self.pos = [self.pos[0],self.pos[1]-1] # go up
					case 'a':
						self.pos = [self.pos[0]-1,self.pos[1]] # go left
					case 's':
						self.pos = [self.pos[0],self.pos[1]+1] # go down
					case 'd':
						self.pos = [self.pos[0]+1,self.pos[1]] # go right
			else:
				return False
		else: 
			return self.check_pos(size) # check one more time if out of bounds

class stage():
	def __init__(self):
		self.size = (5,5) # all stages are rectangles
		self.exit = (5,5)
		self.ico = 'O'
	def draw(self,player_pos,player_ico):
		for y in range(1,self.size[0]+1):
			for x in range(1,self.size[1]+1):
				if(player_pos == [x,y]):
					print(player_ico,end='')
				elif(self.exit == (x,y)):
					print(self.ico,end='')
				else:
					print('.',end='')
			print()

# class init
player = player()
stage = stage()

# game itself
while(True):
	clear()
	stage.draw(player.pos,player.ico)
	#print(player.show_pos())
	direction = input('type w,a,s,d to move' + "\n")
	if (player.move(direction,stage.size) is False):
		clear()
		print('OUT OF BOUNDS')
		break
	if (tuple(player.pos) == stage.exit):
		clear()
		print('YOU WIN')
		break