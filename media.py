# Udacity Full Stack Web Developer nanodegree
# Programming Fundamentals
# Use Classes
# Movie class design
# 2017-06-12 Robert Buckley

import webbrowser

class Movie():
	"""
	This class provides a way to store movie related information
	"""
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	def __init__(self, title, storyline, poster_image, trailer_youtube):
		self.title = title
		self.storyline = storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		"""
		Launches the movie's trailer URL in a web browser
		"""
		webbrowser.open(self.trailer_youtube_url)