import requests #requesting the api i think
def get_recipes(food): #so tkinter can actually connect to here
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={food}" # it creates a key called meals so don't use food
    response = requests.get(url) #response is the answer to the request frfr
    data = response.json() #taking a json and turing it into a dict
    if data["meals"] is None: #if no recipe found in the list it will print no recipe found
        return None#appenertly not found in here use return because tkinter no print
    else: # each meal here is a dict so we kinda need to print many recipes at once and make it readable
        return data["meals"] #the loop lets you get many recipes so find the matching ones no delete
