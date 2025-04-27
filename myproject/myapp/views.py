from django.shortcuts import render,get_object_or_404
from myapp.forms import BookingForm
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied  
from django.contrib.auth.decorators import login_required 
from django.template import loader 
from .models import Menu
@login_required 
def myview(request): 
    return HttpResponse("Hello World") 
def myview(request): 
    if request.user.is_anonymous(): 
        raise PermissionDenied() 
    


def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def book(request):
    return render(request, 'book.html')
def menu(request):
    menu_data=Menu.objects.all()
    main_data={"menu":menu_data}
    return render(request,"menu.html",{"menu": main_data})

def display_menu_item(request, pk): 
    menu_item = get_object_or_404(Menu, pk=pk)  # Trả về 404 nếu không tìm thấy
    return render(request, 'menu_item.html', {"menu_item": menu_item})


def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('booking_success')  # Chuyển hướng sau khi đặt bàn thành công
    else:
        form = BookingForm()
    return render(request, 'book.html', {'form': form})



def form_view(request):
    form=BookingForm()
    context={"form":form}
    return render(request,"home.html",context) 
#html response
def index(request,name):
    return HttpResponse("<h1>hello, {}.</h1>".format(name))
# render template with dymamic data

def index(request,name): 
    template = loader.get_template('hello.html') 
    context={'name': name}   
    return HttpResponse(template.render(context, request)) 
def aboutt(request):
    about_content={'about': "Sompo Restaurant is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."} 
    return render(request,"about.html",about_content)



#tags im dtl 
def tags(request): 
    langs = ['Python', 'Java', 'PHP', 'Ruby', 'Rust'] 
    return render(request, 'langs.html', {'langs':langs}) 
def login(request): 
    context={'user':'admin'} 
    return render(request, 'index.html', context) 