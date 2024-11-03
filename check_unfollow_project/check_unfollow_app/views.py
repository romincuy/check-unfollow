import json
from django.shortcuts import render
from .forms import UploadFileForm

def check_unfollow(request):
    result = []
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Memuat data dari file followers
            followers_file = request.FILES['followers_file']
            followers_data = json.load(followers_file)
            followers = [entry['value'] for item in followers_data for entry in item['string_list_data']]
            
            # Memuat data dari file following
            following_file = request.FILES['following_file']
            following_data = json.load(following_file)
            following = [entry['value'] for item in following_data['relationships_following'] for entry in item['string_list_data']]
            
            # Menentukan akun yang tidak mengikuti balik
            result = [user for user in following if user not in followers]
    
    else:
        form = UploadFileForm()

    return render(request, 'check_unfollow_app/check_unfollow.html', {'form': form, 'result': result})

