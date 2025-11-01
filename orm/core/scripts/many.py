from core.models import Restaurant,Staff

def run():
  
  # create staff
  Rahim = Staff.objects.create(name='Rahim')
  Karim = Staff.objects.create(name='Karim')
  Sahim = Staff.objects.create(name='Tahim')
  
  
  res = Restaurant.objects.all()
  
  # create many to many ralationship
  Rahim.restaurant.add(res[3])
  Rahim.restaurant.add(res[2])
  Rahim.restaurant.add(res[1])
  
  Karim.restaurant.add(res[3])
  Karim.restaurant.add(res[2])
  Karim.restaurant.add(res[1])
  
  
  Sahim.restaurant.add(res[3])
  Sahim.restaurant.add(res[2])
  Sahim.restaurant.add(res[1])
  