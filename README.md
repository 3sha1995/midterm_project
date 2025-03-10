MIDTERM PROJECT SET UP

Step 1: Create a Django Project and App
  Project Name: task_manager
  App Name: tasks

Step 2: Define the Task Model
   id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField() 

Step 3: Apply Migrations
  python manage.py makemigrations tasks
  python manage.py migrate

Step 4: Implement CRUD Functionality
  task_list
  task_create
  task_update
  task_delete

Step 5: Define URLs

Step 6: Create Basic Templates
  task_list.html
  task_form.html
  task_confirm_delete.html

Step 7: Add Basic Styling
  I add static to use to reference for css

Step 8 (final): Run the Project
  python manage.py runserver
  
  
