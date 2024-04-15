from django.shortcuts import render
from .models import Manga

# mangas = [
#   {'name': 'Martial Peak', 'genre': 'Action', 'description': 'The journey to the martial peak is a lonely solitary and long one.', 'chapter': 3744},
#   {'name': 'Re:Monster', 'genre': 'Fantasy', 'description': 'Reincarnated into a new world as a goblin with is skill from his old world.', 'chapter': 99},
#   {'name': 'Goblin Slayer', 'genre': 'Fantasy', 'description': 'Boy loses everything because a goblin attack. Now he is the formost expert on killing goblins', 'chapter': 94},
# ]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def mangas_index(request):
    mangas = Manga.objects.all()
    return render(request, 'mangas/index.html', {'mangas': mangas})

def mangas_detail(request, manga_id):
    manga = Manga.objects.get(id=manga_id)
    return render(request, 'mangas/detail.html', {'manga': manga})