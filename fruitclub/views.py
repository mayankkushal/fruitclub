from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from fruitclub.models import Profile, SlideShowImage, ImageGroup
from fruitclub.forms import ProfileForm

# Create your views here.

def index(request):
	slideshow = ImageGroup.objects.get(name='banner')
	image_list = SlideShowImage.objects.filter(slideshow=slideshow)
	context_dict = {'image_list':image_list}
	return render(request, 'fruitclub/index.html', context_dict)

@login_required
def profile(request):
	if request.method == 'POST':
		profileform = ProfileForm(request.POST)
		if profileform.is_valid():
			profile = profileform.save(commit=False)
			profile.user = request.user
			profile.save()
		return redirect(index)
	else:
		profileform = ProfileForm()
	return render(request, 'fruitclub/profile.html', {'profileform':profileform})

def profile_page(request):
	profile = Profile.objects.get(user=request.user)
	return render(request, 'fruitclub/profile_page.html', {'profile':profile})