# Udacity Full Stack Web Developer nanodegree
# Programming Fundamentals
# Use Classes
# movie trailer site main script
# 2017-06-12 Robert Buckley

import media
import fresh_tomatoes
import json

def load_movies(filename):
	"""
	Return a list of Movie objects loaded from a JSON file

	filename: name of a JSON file to load movie info from
	"""
	movies = []

	with open(filename, 'r') as f:
		moviedb_text = f.read()

		# Convert JSON data to list of dicts and grab only the list of 'movies'
		moviedb_dicts = json.loads(moviedb_text)["movies"]

		# Create a new Movie object from each movie dict and append it to 
		# the movie list.
		# It's not really necessary for each Movie object to be associated
		# with a unique variable name as these aren't even really used.
		for movie_dict in moviedb_dicts:
			movies.append(
				media.Movie(
					movie_dict["title"],
					movie_dict["storyline"],
					movie_dict["poster_image_url"],
					movie_dict["trailer_youtube_url"]
					)
				)
	return movies

def main():
	movies = load_movies("moviesdb.json")
	fresh_tomatoes.open_movies_page(movies)

if __name__ == "__main__":
	main()