from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'index.html')

def chat_view(request):
    return render(request, 'pages/chat.html')

def default_view(request):
    return render(request, 'pages/default.html')

def sidebar_view(request):
    return render(request, 'components/sidebar.html')