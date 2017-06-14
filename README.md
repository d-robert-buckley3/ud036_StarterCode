# Movie Trailer Site

This exercise demonstrates the creation of one's own class.  We created a new class 'Movie', added some variables to it for movie info, then added a method of playing the movie's trailer on YouTube.

Later we imported another file, fresh_tomatoes.py, which takes a list of our Movie objects and creates a web site out of them.

### Setup

On a Python enabled system:

* Clone this repo to a local folder using the green "Clone or Download" button to the upper right above
* Execute using: python entertainment_center.py

#### Comments on the lesson

I made some changes to the main script from what was shown in the lesson videos.  It bothered me having all the movie data (a database, really) inside the main script, or even inside a Python file at all.  I moved all that data out into a JSON file and added a function to read in all that data into dict format, then instantiate each Movie object with the data in each.  This makes the main script much cleaner and keeps all the data separate.

I also fixed what I felt was an issue with the fresh_tomatoes.py file.  Two of the films I selected had some pretty long titles.  When they were rendered into movie tiles in the grid, their names were printed onto 2 lines of text instead of one.  This broke the perfect pattern of tiles.  The 2 tiles that would have been arranged directly beneath the movies with long names were instead pushed down to a third row in the grid leaving large gaps where they should have been.  The second row consisted of much white space with the 3rd tile off to the right.  I made a change to print only the first 19 characters of the title into the movie tile for all films whose names exceeded 20 characters.

But, then this bothered me because now there was no way to view the full title of the film except in its poster image, which could be difficult for some posters. I tried to add a tooltip on hover for each tile using [sample code](https://www.w3schools.com/css/css_tooltip.asp) from the W3 Schools pages on CSS.  It doesn't seem to be working, but it doesn't seem to affect the existing html, so I left it in so that someone with more CSS experience can explain to me what I did wrong.

I've had very superficial exposure to CSS this far.  I didn't want to belabor it so I left it as is so I can move on.  I know I will learn some CSS later.  Perhaps then I can return to this and do a better job.  Who knows, maybe I'm already close.

EDIT: After code review I have incorporated the instructions on how to make the tooltip work.  It looks great now!  I also externalized all the HTML that was in fresh_tomatoes.py so they are now read in from TXT files.
