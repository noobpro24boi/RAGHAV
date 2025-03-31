movie_dict = {
  "The Godfather": 9.2,
  "The Shawshank Redemption": 9.3,
  "The Dark Knight": 9.0,
  "Forrest Gump": 8.8,
  "Star Wars: Episode IV - A New Hope": 8.6
}

movie = input("Enter a movie title: ")
if movie in movie_dict:
  print(movie + " has a rating of " + str(movie_dict[movie]) + " on IMDb.")
else:
  print("Sorry, that movie is not in the database.")
