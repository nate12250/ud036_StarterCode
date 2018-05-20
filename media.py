import webbrowser

class Movie():
    #Ratings for movies, not in the website
    VALID_RATINGS = ["G","PG","PG-13","R"]

    #Movie information contructor
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    
    #Shows trailer on click
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
