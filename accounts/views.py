from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def profile(request):
    request.user # django.contrib,auth.models.AnonymousUser
    return render(request, 'accounts/profile.html')