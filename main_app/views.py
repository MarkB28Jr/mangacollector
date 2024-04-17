from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Manga, Read
from .forms import ReadMeForm

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
    # id_list = manga.read.all().values_list('id')
    # reads_manga_doesnt_have = Read.objects.exclude(id__in=id_list)
    readme_form = ReadMeForm()
    return render(request, 'mangas/detail.html', { 'manga': manga, 'readme_form': readme_form })


def add_readme(request, manga_id):
    form = ReadMeForm(request.POST)
    if form.is_valid():
      new_readme = form.save(commit=False)
      new_readme.manga_id = manga_id
      new_readme.save()
    return redirect('detail', manga_id=manga_id)
  
def assoc_read(request, manga_id, read_id):
    Manga.objects.get(id=manga_id).reads.add(read_id)
    return redirect('detail', manga_id=manga_id)

def remove_read(request, manga_id, read_id):
    manga.objects.get(id=manga_id).reads.remove(read_id)
    return redirect('detail', manga_id=manga_id)



class MangaCreate(CreateView):
    model = Manga
    fields = ['name', 'genre', 'description', 'chapter']

class MangaUpdate(UpdateView):
    model = Manga
    fields = ['genre', 'description', 'chapter']

class MangaDelete(DeleteView):
    model = Manga
    success_url = '/mangas'

class ReadList(ListView):
    model = Read

class ReadDetail(DetailView):
    model = Read

class ReadCreate(CreateView):
    model = Read
    fields = '__all__'

class ReadUpdate(UpdateView):
    model = Read
    fields = ['name', 'position']

class ReadDelete(DeleteView):
    model = Read
    success_url = '/reads'