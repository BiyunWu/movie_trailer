# import media
import entertainment_center
import fresh_tomatoes

# Make a list of Movie objects from the module of entertainment_center
movies = [entertainment_center.shawshank, entertainment_center.schindlers_list, entertainment_center.dina]
# Open the browser to show the website.
fresh_tomatoes.open_movies_page(movies)

# The following code is used for test.
# print(media.Movie.__name__)
# print(media.Movie.__module__)
# print(media.Movie.__doc__)