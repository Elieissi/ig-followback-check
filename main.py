# Quick script to check who follows you back on Instagram
import json

# Load followers, instagram labeled the followers file followers_1, if yours is different, change file name.
with open("followers_1.json", "r", encoding="utf-8") as file: 
    list_of_followers = []
    data = json.load(file)
    for dic in data:
        followers = dic["string_list_data"][0]["value"]
        list_of_followers.append(followers)

# Load following
with open("following.json", "r", encoding="utf-8") as file:
    list_of_following = []
    data = json.load(file)
    unwrapped = data["relationships_following"]
    for dic in unwrapped:
        following = dic["string_list_data"][0]["value"]
        list_of_following.append(following)

# Print who doesn't follow you back
print("\nUsers who don't follow you back:\n")
followers_set = set(list_of_followers) #faster lookup this way
for user in list_of_following:
    if user not in followers_set:
        print(user)
