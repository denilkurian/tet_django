from django.shortcuts import render,redirect
from .models import Candidate,Trash


############## for listing all candidate list and also how many of them
def listall(request):
    candidates = Candidate.objects.all()
    dummy = 'i am dummy message'
    count = Candidate.objects.all().count()
    return render(request,'base.html',context={'candidates':candidates,'dummy':dummy,'count':count})


############# to delete all candidate also restoring 
def delete_candidate(request):
    if request.method == 'POST':
        delete = Candidate.objects.all()
        for candidate in delete:
            trash = Trash.objects.create(
                name=candidate.name,
                email=candidate.email,
                phone=candidate.phone
            )
        delete.delete()
        return redirect('all')
    return render (request,'base.html')



############# to delete each candidate also restoring         
def delete_each_candidate(request,pk):
    if request.method == 'POST':
        candidate = Candidate.objects.get(id=pk)
        trash = Trash.objects.create(
            name=candidate.name,
            email=candidate.email,
            phone=candidate.phone
        )
        candidate.delete()
        return redirect('all')
    return render (request,'base.html')



############# trash bin where deleted candidates are seen
def trash(request):
    trashes = Trash.objects.all()
    return render(request,'trash.html',context={'trashes':trashes})


############ function created for restore 
def restore_trash(request,pk):
    if request.method == 'POST':
        trash = Trash.objects.get(id=pk)
        candidate = Candidate.objects.create(
            name=trash.name,
            email=trash.email,
            phone=trash.phone
        )
        trash.delete()
        return redirect('all')
    return render (request,'trash.html')


############# clear the whole trash
def clear_trash(request):
     if request.method == 'POST':
        clear = Trash.objects.all().delete()
        return redirect ('trash') 
     



########clear the whole trash using url calling by js
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,JsonResponse

@login_required  # Ensure the user is logged in
def clear_trash(request):
    if request.method == 'POST':
        Trash.objects.all().delete()
        return HttpResponse("Trash cleared successfully.")


####### delete the single trash using url calling by js
def clear_single_trash(request,pk):
    if request.method == 'POST':
        Trash.objects.get(id=pk).delete()
        return JsonResponse("Trash cleared successfully.")



######### to add each candidate
def add_new_candidate(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        name = request.POST.get('name')

        saving = Candidate(email=email,phone=phone,name=name)
        saving.save()
        return redirect('all')
    return render (request,'base.html')



from django.shortcuts import render, get_object_or_404

def add_update_candidate(request, pk=None):
    candidate = get_object_or_404(Candidate, pk=pk) if pk else None

    if request.method == 'POST':
        if candidate:
            candidate.name = request.POST.get('name')
            candidate.email = request.POST.get('email')
            candidate.phone = request.POST.get('phone')
            candidate.save()
        return redirect('all')
    return render(request, 'base.html', {'candidate': candidate})
        
       









