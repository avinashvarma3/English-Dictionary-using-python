import json
from difflib import get_close_matches

data = json.load(open("data.json"))
def meaning(key):
    key = key.lower()
    if key in data:
        return data[key]
    elif len(get_close_matches(key, data.keys())) > 0:
        yn = input("Is the word %s ?Please enter Y to continue, or N if no: "%get_close_matches(key,data.keys())[0])
        yn = yn.lower()
        if yn == "y":
            return data[get_close_matches(key,data.keys())[0]]
        elif yn == "n":
            return "Sorry The word doesn't exist,please check!"
    else:
        return "Sorry,this word isn't available in the dictionary!"
word = input("enter a word: ")
result = (meaning(word))
if type(result) == list:
    for item in result:
        print(item)
else:
    print(result)
input('Press ENTER to exit dictionary :D  ')
