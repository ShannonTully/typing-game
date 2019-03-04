from pygame import mixer 
# import keyboard as k
from getch import getch as gc
import time



class KeyPlay:

	def __init__(self):

		self.timer = 0
		self.song = mixer

		self.load_song()

	def load_song(self):
		self.song.init()
		self.song.music.load('03_Klad_Get.mp3')
		self.play_music()

	def play_music(self):
		while type(gc()) is str:
			# import pdb; pdb.set_trace()
			if self.timer == 0:
				self.song.music.play(start=self.timer)
			else:
				self.song.music.unpause()
			time.sleep(.12)
			self.song.music.pause()
			self.timer += 1
		self.play_music()


	# k.wait()

if __name__ == '__main__':
	KeyPlay()