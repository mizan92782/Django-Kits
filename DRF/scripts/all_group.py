from django.contrib.auth.models import Group

def run():
  # Get all groups
  groups = Group.objects.all()

  # Print group names
  for group in groups:
      print(group.name)
