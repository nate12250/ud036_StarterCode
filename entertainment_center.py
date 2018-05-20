#website template
import fresh_tomatoes

#constructor
import media


#toy story information
toy_story = media.Movie("Toy Story",
                        "A story of his boy and his toys that come to life.",
                        "https://vignette.wikia.nocookie.net/pixar/images/4/4c/Toy-story-movie-posters-4.jpg/revision/latest/scale-to-width-down/320?cb=20160329080002",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#Avatar information
avatar = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#CHAPPiE information
chappie = media.Movie("Chappie",
                      "A robot that comes to life",
                      "https://upload.wikimedia.org/wikipedia/en/7/71/Chappie_poster.jpg",
                      "https://www.youtube.com/watch?v=lyy7y0QOK-0")
#Lord of the Rings: Fellowship of the Ring information
lotr = media.Movie("Lord of the Rings",
                   "A ring of power must be destroyed",
                   "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",
                   "https://www.youtube.com/watch?v=V75dMMIW2B4")
#rogue one information
rogue_one = media.Movie("Rogue One A Star Wars Story",
                       "Rebel spies steal the plans of the Death Star",
                       "https://images-na.ssl-images-amazon.com/images/I/51%2Bzb74v-TL.jpg",
                       "https://www.youtube.com/watch?v=pCUXmxbE7JA")
#inside out information
inside_out = media.Movie("Inside Out",
                        "This is what goes on inside your head",
                        "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",
                        "https://www.youtube.com/watch?v=yRUAzGQ3nSY")
#list of favorite movies
movies = [toy_story, avatar, chappie, lotr, rogue_one, inside_out]

#displays movie website from the list movies
fresh_tomatoes.open_movies_page(movies)
