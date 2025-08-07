from django.shortcuts import render, redirect
from .forms import CredentialForm
from django.contrib.auth.decorators import login_required
from .models import Credential
from django.http import HttpResponse




def home(request):
    return render(request, 'home.html')



@login_required
def add_credential(request):
    if request.method == 'POST':
        form = CredentialForm(request.POST)
        if form.is_valid():
            credential = form.save(commit=False)
            credential.user = request.user  # Link to the logged-in user
            credential.save()
            return redirect('credential_success')  # Redirect after saving
    else:
        form = CredentialForm()
    return render(request, 'add_credential.html', {'form': form})


def credential_success(request):
    return render(request, 'success.html')


@login_required
def view_credentials(request):
    credentials = Credential.objects.filter(user=request.user)
    return render(request, 'view_credentials.html', {'credentials': credentials})
