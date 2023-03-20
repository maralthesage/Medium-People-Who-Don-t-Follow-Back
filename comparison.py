with open("followers.txt", "r") as followers:
    followers = followers.readlines()

with open("followings.txt", "r") as followings:
    followings = followings.readlines()


for item in followings:
    if item not in followers:
        print(item)