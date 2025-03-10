from django.shortcuts import render, redirect
from .models import Task



#to retrieve all tasks from the database
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

#to create a new task list
def task_create(request):
    error_message = None
    title = request.POST.get("title", "")
    description = request.POST.get("description", "")
    due_date = request.POST.get("due_date", "")

    if request.method == "POST":
        if title and due_date:
            if "-" in due_date and len(due_date) == 10: # para to macheck kung yung date ay format yyyy-mm-dd
                Task.objects.create(title=title, description=description, due_date=due_date)
                return redirect('task_list')
            error_message = "Invalid date format. Please enter a valid date."
       

    return render(request, 'task_form.html', {'error_message': error_message, 'task': {'title': title, 'description': description, 'due_date': due_date}})
#for edit at magupdate
def task_update(request, id):
    task = Task.objects.filter(id=id).first()
    if not task:
        return redirect('task_list')

    error_message = None
    title = task.title
    description = task.description
    due_date = task.due_date.strftime("%Y-%m-%d")

    if request.method == "POST":
        new_title = request.POST.get("title", "")
        new_description = request.POST.get("description", "")
        new_due_date = request.POST.get("due_date", "")

        if new_title and new_due_date:
            if "-" in new_due_date and len(new_due_date) == 10: # para to macheck ifang date is na format yyyy-mm-dd
                task.title = new_title
                task.description = new_description
                task.due_date = new_due_date
                task.save()
                return redirect('task_list')
            error_message = "Invalid date format. Please enter a valid date."


    return render(request, 'task_form.html', {'task': {'id': id, 'title': title, 'description': description, 'due_date': due_date}, 'error_message': error_message})


#to delete a task
def task_delete(request, id):
    task = Task.objects.filter(id=id).first()
    if request.method == "POST" and task:
        task.delete()
        return redirect('task_list')

    return render(request, 'task_confirm_delete.html', {'task': task, 'id': id})
