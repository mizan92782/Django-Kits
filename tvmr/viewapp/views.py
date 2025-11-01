
from urllib import response
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View



def json_data_view(request):

  data={
    'name' : 'mizanur',
    'book': {
      
      'arabic' : "quran",
      'english' : 'name janinah'
      
      
    }
  }
  return JsonResponse(data)



def post_data(request):
  
  if request.method=='POST':
    
    print(f'Request comes from :  url : {request}')
    print(f'Request method : {request.method}')
    print(f' Post date and token  : {request.POST}')

    print("\n"*3)
    print("Server csrf token and data niye ase ---- \n")
    print(f' server sent to csrf tokens : {request.POST['csrfmiddlewaretoken']}')
    print(f' name : {request.POST['name']}')
    print(f' age : {request.POST['age']}')
    print(request.POST.get('name'))
    print(request.POST.get('age'))
    print(request.POST.get('password'))
    print(request.COOKIES.get('theme', 'light'))

    print(request.META.get)
    print(request.user.is_authenticated)
  
 
  
  return render(request,'viewt/post_data.html')









#! =============== Class based view ==========



#! =============== Base class based view
'''
-> View class extends kore
'''
class base_view(View):

    def get(self, request):
        return render(request, 'viewt/base_cbv.html')  # ✅ use request

    def post(self, request):  # ✅ fix typo
        print("This is POST")
        return HttpResponse("this is post")
    













#! ============== Generic Class-Based Views (GCBV)
''' 
-> এগুলো common patterns এর জন্য তৈরি।
-> types : ListView,DetailsView,CreateView,UpdateView,DeleteView
'''



#! ===================== Templated view
'''
->  static html page er jonno use Hoi 
-> no need to learn
'''




# ! ===============================