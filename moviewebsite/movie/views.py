from .forms import MovieForm, ProfileForm
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Movie, Review,Category,Profile
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def admin_panel(request):
    categories = Category.objects.all()
    movies = Movie.objects.all()
    users = User.objects.all()
    user_profiles = Profile.objects.all()
    return render(request, 'admin_panel.html', {'categories': categories, 'movies': movies, 'users': users, 'user_profiles': user_profiles})

def index(request):
    movie = Movie.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,'index.html',context)
def add_category(request):
    if request.method == 'POST':
        name = request.POST['name']
        Category.objects.create(name=name)
        return redirect('admin_panel')
    return render(request, 'add_category.html')


def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"details.html",{'movie':movie})

def addmovie(request):
    categories = Category.objects.all()
    if request.method == "POST":
        title=request.POST.get('title',)
        desc=request.POST.get('desc',)
        year=request.POST.get('year',)
        actors=request.POST.get('actors',)
        img=request.FILES['img']
        youtube_link = request.POST.get('youtube_link',)
        category_id = request.POST.get('category')
        category = Category.objects.get(pk=category_id)
        movie=Movie(title=title,desc=desc,year=year,img=img,actors=actors,youtube_link=youtube_link,category=category)
        movie.save()
        return redirect('/')
    return render(request, 'addmovie.html', {'categories': categories})

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'submit.html',{'form':form,'movie':movie})


def delete(request,id):
    if request.method == "POST":
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')


def delete_user(request, user_id):
    if request.method == "POST":
        user = User.objects.get(pk=user_id)
        user.delete()
    return redirect('admin_panel')


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    reviews = Review.objects.filter(movie=movie)
    context = {'movie': movie, 'reviews': reviews}
    return render(request, 'movie_detail.html', context)




@login_required
def view_profile(request):
    profile = request.user.profile
    return render(request, 'view_profile.html', {'profile': profile})




@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('movie:view_profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})