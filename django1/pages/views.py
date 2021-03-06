from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def lotto(request):
    import random
    pick = random.sample(range(1, 46), 6)
    context = {
        'pick' : pick
    }
    return render(request, 'lotto.html', context)
    
def computer(request):
    import random
    languages = ['HTML', 'CSS', 'bootstrap', 'django', 'python']
    language = random.choice(languages)
    context = {
        'languages' : languages,
        'language' : language
    }
    return render(request, 'computer.html', context)

def hi(request, name):
    context = {
        'name' : name
    }
    return render(request, 'hi.html', context)

def add(request, a, b):
    result = a + b
    context = {
        'result' : result
    }
    return render(request, 'add.html', context)

def posts(request, id):
    content = 'Life is short, you need python!'
    replies = ['유익!!', '별로다!!!', '감사합니다!!']
    no_replies = []
    user = 'hanpy'
    context = {
        'id' : id,
        'content' : content,
        'replies' : replies,
        'no_replies' : no_replies,
        'user' : user,
    }
    return render(request, 'posts.html', context)