import webbrowser


class Movie():

    # __doc__
    '''The Movie class is used for creating movie objects that contians
    its title, storyline, poster link and trailer link.'''

    # Constructor
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Show Youtube trailer
    def show_trailer(self):
    	webbrowser.open(self.trailer_youtube_url)