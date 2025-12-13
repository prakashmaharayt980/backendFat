
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(email='admin@example.com').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("Superuser created: admin@example.com / admin123")
else:
    print("Superuser already exists")
