from django.core.management import execute_from_command_line
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_ecommerce_project.settings')
execute_from_command_line()