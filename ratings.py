"""Restaurant rating lister."""

import random
# put your code here
restaurant_ratings = {}

def alpha_ratings(data):
    restaurant_data = open(data)

    for line in restaurant_data:
        #strips any trailing whitespace
        lines = line.rstrip()
        #puts the name and score in a list separately indexed
        name_rating = lines.split(":") 

        restaurant_ratings[name_rating[0]] = int(name_rating[1])

def show_restaurants():
    for restaurant, rating in sorted(restaurant_ratings.items()):
        print(f'{restaurant}: {rating}')
   




def add_restaurant():
    new_restaurant = input("Please provide restaurant name: ")
    new_score = input("Please provide the restaurant score: ")
    #validates user input for score
    while True:
        if new_score not in "12345":
            print("That is not a valid score.")
            new_score = input(" Please input a value between 1 - 5: ")
        else:
            break
    
    restaurant_ratings[new_restaurant.title()] = int(new_score)

    return alpha_ratings("scores.txt")

def suprise_me():
    suprise = random.choice(list(restaurant_ratings.keys()))
    print(f"{suprise} has a rating of {restaurant_ratings[suprise]}")
    rating = input("Please input your updated rating: ")
    while True:
        if rating not in "12345":
            print("That is not a valid score.")
            new_score = input(" Please input a value between 1 - 5: ")
        else:
            break
    restaurant_ratings[suprise]=int(rating)

def user_selection():
    alpha_ratings("scores.txt")
    print("Welcome! to Yumscore")
    while True:
        print("Choose from the following options")
        print()
        print("[S]ee all ratings")
        print("[A]dd and rate a new restaurant")
        print("[R]andomly choose a restaurant")
        print("[Q]uit")
        print()
        selection = input("Please input your selection: ")
        while True:
            if selection not in "saqrSAQR":
                print("That is not a valid score.")
                selection = input(" Please input either 'S', 'A', 'R', or 'Q': ")
            else:
                break
                
        if selection.upper() == "S":
            show_restaurants()
            print()
        elif selection.upper() == "A":
            add_restaurant()
            print()
        elif selection.upper() == "R":
            suprise_me()
        else:
            print("Goodbye")
            break


user_selection()