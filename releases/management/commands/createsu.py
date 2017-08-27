from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from syah_site.settings.base import get_env_variable


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username="heendog").exists():
            pw = get_env_variable("DJANGO_ADMIN_PASSWORD")
            User.objects.create_superuser("heendog", "admin@admin.com", pw)
            self.stdout.write(
                self.style.SUCCESS('Successfully created new super user'))
