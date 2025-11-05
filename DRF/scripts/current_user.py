

from urllib import request


def run():
    current_user = request.user  # this is the currently logged-in user
    print("Current user:", current_user.username)
    # You can check if the user is authenticated
    if request.user.is_authenticated:
        print("User is logged in")
    else:
        print("User is not logged in")
