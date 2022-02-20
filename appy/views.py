from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'appy/index.html',{})

def searched(request):
    if request.method == "POST":
        searched = request.POST['searchbar']
        searched = searched.upper()
        return render(request,'appy/searchedCoin.html',{
            'searched':searched
            })
    else:
        return render(request,'appy/searchedCoin.html',{
         
            })
def about(request):
    return render(request,'appy/about.html',{})