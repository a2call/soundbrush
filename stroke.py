
class Mood:
	Joyful = 0
	Happy = 1
	Sad = 2
	Dark = 3
	Chaotic = 4
	

def findMood(pos):
	return int(pos)

class MusicStroke:
	def __init__(self, pos, color):
		mood = findMood(pos)
		self.ref_y = pos.y
		self.composer = Composer(color, mood)
		self.arclen = 0
		self.prev = 0
	def tic(self, arclen, y):
		self.arclen += arclen
		offset = int(arclen / .05) - self.prev

		if (y < self.ref_y):
			offset = -offset
			
		composer.tic(offset)
		self.prev = offset

	def stop(self):
		composer.stop()

