import os
from django.contrib.auth import get_user_model

User = get_user_model()

username = "gautam"
email = "imgautamyadav@gmail.com"
password = "Gny@206"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(
        username=username,
        email=email,
        password=password
    )
    print("Superuser created")
else:
    print("Superuser already exists")