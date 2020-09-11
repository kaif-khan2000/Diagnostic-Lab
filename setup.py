import os

os.system("pip install django")
print("django installed")
os.system("python manage.py makemigrations")
os.system("python manage.py migrate")

print("creating a super user")
os.system("python manage.py createsuperuser")