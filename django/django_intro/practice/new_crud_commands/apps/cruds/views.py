from django.shortcuts import render

# Create your views here.
def index(request):
    print('hello world!')
    return render(request, 'cruds/index.html')


# ############CREATING###############
# newly_created_movie = Movie.objects.create(title="The Princess Bride",description="the best movie ever",release_date="1987-09-25",duration=98)
# print(newly_created_movie.id)	# view the new movie's id

# newly_created_movie = Movie(title="The Princess Bride",description="the best movie ever",release_date="1987-09-25",duration=98)
# newly_created_movie.save()

# ############READING###############
# # All
# all_movies = Movie.objects.all()
# # Filter (WHERE)
# some_movies = Movie.objects.filter(release_date='2018-11-16')
# # Exclude (WHERE NOT)
# other_movies = Movie.objects.exclude(release_date='2018-11-16')
# #   a list of instances, we can iterate through 
# for m in all_movies:    # m represents each movie instance as we iterate through the list
#     print(m.title)	# that means m has all the properties of the Movie class, including title, release_date, etc.

# ########SINGLE RECORDS
# # Get
# one_movie = Movie.objects.get(id=7)
# # First
# first_movie = Movie.objects.first()
# # Last
# last_movie = Movie.objects.last()

# print("Movie 7", one_movie.title)
# print("First movie", first_movie.release_date)
# print("Last movie", last_movie.description)


# ############UPDATING###############

# movie_to_update = Movie.objects.get(id=42)	# let's retrieve a single movie,
# movie_to_update.description = "the answer to the universe"	# update one/some of its field values
# movie_to_update.title = "The Hitchhiker's Guide to the Galaxy"
# movie_to_update.save()	# then make sure all changes to the existing record get saved to the database

# ############DELETING###############

# movie_to_delete = Movie.objects.get(id=2)	# let's retrieve a single movie,
# movie_to_delete.delete()	# and then delete it