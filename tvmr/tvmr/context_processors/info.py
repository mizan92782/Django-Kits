# ssors/info.py

def developer_info(request):
  
    # modeler age processor run hoi,tai,processor er bitor model imort korte hobe
    from tempt.models import Student  # import here to be safe
    from enums.student_enum import Gender

    return {
        'developer': "Mizanur Rahman",
        'age': 55,
        'color': 'black',
        'stu': Student.objects.filter(gender=Gender.MALE)  # use .filter(), no need for .all() before it
    }
