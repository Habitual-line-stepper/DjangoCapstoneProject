from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from band.models import Band
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.forms import AuthenticationForm
from .forms import BandForm
from django.contrib import messages

# Create your views here.

def home(request):
    """
    Renders the home page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    some_band = Band.objects.first()
    context = {'bands': Band.objects.all(), 'some_band': some_band}
    return render(request, 'home.html', context)


def band_list(request):
    """
    Renders the band list page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    bands = Band.objects.all()
    return render(request, 'band_list.html', {'bands': bands})


class BandListView(ListView):
    """
    Renders the band list page using the ListView class.

    Attributes:
        model (Band): The model that the ListView uses to retrieve data.
        template_name (str): The name of the template used to render the page.
        context_object_name (str): The name of the context object that the ListView uses to pass data to the template.

    """
    model = Band
    template_name = 'band_list.html'
    context_object_name = 'bands'

    
def login_view(request):
    """
    Renders the login page and authenticates a user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('bands:home')
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'bands/login.html', {'form': form})


def register(request):
    """
    Renders the registration page and registers a new user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('bands:home')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})
    
    
@login_required
def add_band(request):
    """
    Renders the add band page and adds a new band.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    if request.method == 'POST':
        form = BandForm(request.POST, request.FILES)
        if form.is_valid():
            band = form.save(commit=False)
            band.user = request.user
            band.save()
            return redirect('bands:band_list')
    else:
        form = BandForm()
    return render(request, 'add_band.html', {'form': form})
     
@login_required
def edit_band(request, pk):
    """
    Renders the edit band page and adds a new band.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    bands = Band.objects.all()
    selected_band_pk = request.POST.get('band_select')
    selected_band = get_object_or_404(Band, pk=selected_band_pk) if selected_band_pk else None
    if request.method == 'POST':
        form = BandForm(request.POST, request.FILES, instance=selected_band)
        if form.is_valid():
            band_pk = request.POST.get('band_select')  
            selected_band = get_object_or_404(Band, pk=band_pk)
            form.save()
            return redirect('bands:band_list_noarg')
    else:
        form = BandForm(instance=selected_band)
    return render(request, 'edit_band.html', {'form': form, 'bands': bands, 'selected_band': selected_band})





@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})
    
