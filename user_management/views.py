from django.http import request, HttpResponseRedirect,HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import json
import urllib.request

from . models import User
from . forms import UserForm


def LandingPage(request):
		return render(request, 'login_page.html')


def LoginPage(request):
		return render(request, 'login_page.html')


def ProfilePage(request):
		return render(request, 'user_management/profile_page.html')


def LoginUser(request):
	email = request.POST['email']
	password = request.POST['password']

	user = authenticate(request, email=email, password=password)

	if user is not None and user.is_active:
		login(request, user)
		return redirect('profile_page')

	else:
		print('User does not exist or is Inactive')
		messages.warning(request,'Invalid username or password')
		return HttpResponseRedirect('/login')


@login_required(login_url='login')
def UpdateUserProfile(request):
	if request.method == 'POST':
		instance = User.objects.get(pk=request.user.id)
		old_address = instance.home_address
		form  = UserForm(request.POST,instance=instance)
		if form.is_valid():
			post = form.save(commit=False)

			print('updating user info')

			post.save()
			
			address = post.home_address

			print(old_address)
			print(address)
			#UPDATE USER COORDINATES IF THEY HAVE CHANGED
			if old_address != address:
				print('Executing update statement')
				try:
					api_key = 'ge-30cc89b091fb3056'
					
					query = f"https://api.geocode.earth/v1/search?api_key={api_key}&boundary.country=ZA&text={address}".replace(' ', '+')
					
					response = json.load(urllib.request.urlopen(query))

					User.objects.filter(pk=request.user.id).update(
						location = response['features'][0]['properties']['label'],
						user_lat = response['features'][0]['geometry']['coordinates'][1],
						user_lon = response['features'][0]['geometry']['coordinates'][0],
					)
				except Exceptions as e:
					print(e)
			
			messages.success(request,'Profile successfully updated')
			return HttpResponseRedirect('/profile')
		else:
			print(form.errors)
			messages.warning(request,"Invalid Form, Please fill in all fields required fields: "+str(form.errors))
			return HttpResponseRedirect('/profile')
	else:
		messages.danger(request,'Something went wrong, please fill in all fields required fields')
		return HttpResponseRedirect('/profile')
		



def LocationMap(request):
		return render(request, 'user_management/location_map.html')



@login_required(login_url='login')
def GetUsersLocations(request):
	data = []
	if request.user.is_staff:
		
		try:
			usrs = User.objects.filter(is_active=1).values('id','first_name','last_name',
				'profile_photo','job_title','location','user_lat','user_lon',)


			for u in usrs:
				info = {
					'id'			:u['id'],
					'name'		:u['first_name']+' '+u['last_name'],
					'photo'		:u['profile_photo'],
					'title'		:u['job_title'],
					'location':u['location'],
					'lat'			:u['user_lat'],
					'lon'			:u['user_lon'], 
				}
				data.append(info)

			return JsonResponse(data,safe=False)
		except Exception as e:
			print(e)
			return JsonResponse(data,safe=False)

	else:
		try:
			usrs = User.objects.filter(is_active=1,pk=request.user.id).values('id','first_name','last_name',
				'profile_photo','job_title','location','user_lat','user_lon',)


			for u in usrs:
				info = {
					'id'			:u['id'],
					'name'		:u['first_name']+' '+u['last_name'],
					'photo'		:u['profile_photo'],
					'title'		:u['job_title'],
					'location':u['location'],
					'lat'			:u['user_lat'],
					'lon'			:u['user_lon'], 
				}
				data.append(info)

			return JsonResponse(data,safe=False)
		except Exception as e:
			print(e)
			return JsonResponse(data,safe=False)