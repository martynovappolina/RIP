from django.shortcuts import render

def menu(request):
    return render(request, 'menu.html', {
        'pages': [
            {'title': 'картинки котиков', 'id': 1},
            {'title': 'картинки собачек', 'id': 2},
            {'title': 'просто картинки', 'id': 3},
        ]
    })

def page(request, id):
    return render(request, 'page.html', {'data': {
        'id': id
    }})