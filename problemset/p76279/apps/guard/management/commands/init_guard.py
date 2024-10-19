from django.core.management.base import BaseCommand

from apps.guard.models import SecurityConfig, ViewDetail
from apps.guard.utils import list_views


class Command(BaseCommand):
    """ This command initializes the gurad
        for enhancing the security of your project.
    """
    help = 'Initialize Guard app'

    def handle(self, *args, **options):
        for v in list_views():
            try:
                ViewDetail.objects.get(path=v[0])
            except ViewDetail.DoesNotExist:
                ViewDetail.objects.create(
                    name=v[1],
                    path=v[0]
                )
        if SecurityConfig.objects.count() == 1:
            SecurityConfig.objects.create()

