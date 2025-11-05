from core .models import User

def run():
    for i in range(1, 10):
        username = f'fuser{i}'
        password = f'123{i}'
        
        # Use create_user to hash the password automatically
        user = User.objects.create_user(username=username, password=password)
        print(f"Created user: {username}")
    


    

    