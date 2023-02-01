def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        "full_name": "Michael Young",
        "student_id": 10073390,
        "pizza_toppings": ["PINEAPPLE", "HAM", "CHEESE"],
        "movies": [
            {
                "title": "spriderman",
                "genre": "sci-fi"
            },
            {
                "title": "never back down",
                "genre": "action"
            }
        ]
    
    }
    new_movie = {
        "title": "sweeney todd: the demon barber of fleet street",
        "genre": "musical"
    }
    about_me["movies"].insert(1, new_movie)

    print_student_name_and_id(about_me)
    print("\n")
    print_pizza_toppings(about_me,)
    print("\n")
    add_pizza_toppings(about_me, ("onion", "bacon", "mushroom"))
    print_pizza_toppings(about_me)
    print("\n")
    print_movie_genres(about_me)
    print("\n")
    print_movie_titles(about_me["movies"])

# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    full_name = about_me["full_name"]
    first_name, last_name = full_name.split()
    print(f"MY name is {full_name}, but you can call me Sir {first_name}.")
    print(f"My student ID is {about_me['student_id']}")
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me["pizza_toppings"].extend(toppings)
    about_me["pizza_toppings"] = [topping.lower() for topping in about_me["pizza_toppings"]]
    about_me["pizza_toppings"].sort()
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print("My favourite pizza toppings are:")
    for topping in about_me["pizza_toppings"]:
        print("-", topping)
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    genres = [movie["genre"] for movie in about_me["movies"]]
    genres_str = ", ".join(genres)
    print(f"I like to watch {genres_str} movies.")
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    titles = [movie["title"].title() for movie in movie_list]
    titles_str = ", ".join(titles)
    print(f"Some of my favourite movies are {titles_str}!")
    return
    
if __name__ == '__main__':
    main()