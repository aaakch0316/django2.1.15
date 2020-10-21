from django.shortcuts import render

# Create your views here.
def detail(request):
    test = 'testing base.html'
    context = {
        'test' : test,
    }
    return render(request, 'articles/detail.html', context)