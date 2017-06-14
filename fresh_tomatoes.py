# From github repo:
#     https://github.com/adarsh0806/ud036_StarterCode
# Used per recommendation by Udacity project instructions
# Heavily modified to externalize the HTML used
#   and to fix an issue with movie tile alignments

import webbrowser
import os
import re


def load_html(filename):
    """
    Load HTML page content or templates from an external file

    filename (str): name of external file containing HTML content

    Returns HTML content as a string
    """
    content = ""
    with open(filename, 'r') as f:
        content = f.read()

    return content


# Styles and scripting for the page
main_page_head = load_html("fresh_tomatoes_main_page_html.txt")


# The main page layout and title bar
main_page_content = load_html("fresh_tomatoes_main_page_content_html.txt")


# A single movie entry html template
movie_tile_content = load_html("fresh_tomatoes_movie_tile_html.txt")


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_title_short=(movie.title if (len(movie.title) < 20) 
                                else movie.title[:19] + '...'),
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
