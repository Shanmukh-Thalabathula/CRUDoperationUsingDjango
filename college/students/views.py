from django.shortcuts import render, redirect, get_object_or_404
from students.models import Students
from students.forms import StudentForm
from django.contrib import messages

# Home View
def home(request):
    students = Students.objects.all()
    return render(request, 'students/home.html', {'students': students})


def details(request, pk):
    student = get_object_or_404(Students, id=pk)
    return render(request, 'students/details.html', {'student': student})

# Add Student View
def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student successfully added.")
            return redirect('home')  # Redirect to 'home' or any other suitable URL
    else:
        form = StudentForm()
    return render(request, 'students/add.html', {'form': form})

# Update Student View
def update(request, pk):
    student = get_object_or_404(Students, id=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student details successfully updated.")
            return redirect('details', pk=student.id)
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/update.html', {'form': form, 'id': student.id})

# Delete Student View
def delete(request, pk):
    student = get_object_or_404(Students, id=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, "Student successfully deleted.")
        return redirect('home')
    return render(request, 'students/delete.html', {'form': student, 'id': student.id})

# Search View
def search(request):
    if request.method == 'POST':
        query = request.POST.get('q', '')
        students = Students.objects.filter(full_name__icontains=query) if query else Students.objects.all()
    else:
        students = Students.objects.all()
    return render(request, 'students/home.html', {'students': students})


