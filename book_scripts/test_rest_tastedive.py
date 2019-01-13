import requests_with_caching
import json


##############################################################
## step 1
##############################################################
def get_movies_from_tastedive(instr):
    baseurl = "https://tastedive.com/api/similar"
    params_diction = {}
    params_diction['q'] = instr
    params_diction['type'] = 'movies'
    params_diction['limit'] = 5

    # get response
    td_resp = requests_with_caching.get(baseurl, params=params_diction)
    # Useful for debugging: print the url! Uncomment the below line to do so.
    # print(td_resp.url)  # Paste the result into the browser to check it out...
    # print(json.dumps(td_resp.json(), indent=4))
    return td_resp.json()


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movies_from_tastedive("Bridesmaids")
get_movies_from_tastedive("Black Panther")


##############################################################
## step 2
##############################################################
def extract_movie_titles(movie_resp):
    movie_titles = [movie['Name'] for movie in movie_resp['Similar']['Results']]
    return movie_titles


##############################################################
## step 3
##############################################################
def get_related_titles(movie_list):
    related_movie_list = set()

    for movie in movie_list:
        for title in extract_movie_titles(get_movies_from_tastedive(movie)):
            related_movie_list.add(title)

    return list(related_movie_list)


##############################################################
## step 4
##############################################################
def get_movie_data(title):
    baseurl = "http://www.omdbapi.com/"
    params_diction = {}
    params_diction['t'] = title
    params_diction['r'] = 'json'

    # get response
    omdb_resp = requests_with_caching.get(baseurl, params=params_diction)
    # Useful for debugging: print the url! Uncomment the below line to do so.
    # print(omdb_resp.url)  # Paste the result into the browser to check it out...
    # print(json.dumps(omdb_resp.json(), indent=4))
    return omdb_resp.json()


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_data("Venom")
# get_movie_data("Baby Mama")

##############################################################
## step 5
##############################################################
def get_movie_rating(movie_details):
    print(movie_details['Ratings'])

    movie_rating = 0
    for movie in movie_details['Ratings']:
        if movie['Source'] == 'Rotten Tomatoes':
            movie_rating = int(movie['Value'][:-1])
        print('Rating: [{Source}], [{Value}]'.format(**movie))

    print(movie_rating)
    return movie_rating


##############################################################
## step 6
##############################################################
def get_sorted_recommendations(movie_list):
    related_movies_list = []

    return related_movies_list
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])

