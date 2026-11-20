movie_list = ["The Matrix", "Inception", "Interstellar"]

print(f"The list movie_list includes my top {len(movie_list)} favorite movies.")
print(movie_list)

print(sorted(movie_list))
print(movie_list)  # sorted() displays a sorted copy; the original list stays in its order.

movie_list.sort()
print(movie_list)  # .sort() changes the original list.

movie_list.append("Parasite")
print(f"The list movie_list now includes my top {len(movie_list)} favorite movies.")
print(movie_list)