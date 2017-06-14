# Udacity Full Stack Web Developer nanodegree
# Programming Fundamentals
# Use Classes
# Movie class design
# 2017-06-12 Robert Buckley

import webbrowser

class Movie():
	"""
	This class provides a way to store movie related information
	
	Attributes:
	    title (str):     the movie's title
	    storyline (str): a brief synopsis about the film
	    poster_image_url (str): 
		web URL pointing to the an image of the movie's poster
	    trailer_youtube_url (str):
		web URL of the movie's official trailer on YouTube
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
