from django.contrib.auth.models import Group
from core.models import User  # your custom user model

def run():
    # Get groups
    BasicUser = Group.objects.get(name='BasicUser')
    PremiumUser = Group.objects.get(name='PremiumUser')

    # Get single users
    user1 = User.objects.get(username='fuser1')
    user2 = User.objects.get(username='fuser2')
    user3 = User.objects.get(username='fuser3')
    user4 = User.objects.get(username='fuser4')

    # Add users to groups
    user1.groups.add(BasicUser)
    user2.groups.add(BasicUser)
    user3.groups.add(PremiumUser)
    user4.groups.add(PremiumUser)

    print("✅ Users added to groups successfully")
