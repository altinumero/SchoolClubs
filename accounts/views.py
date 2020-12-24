from django.shortcuts import render, redirect


# Create your views here.
def registerPage(request):
    from accounts.forms import SignupForm
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form, }
    return render(request, 'registration/register.html', context)
