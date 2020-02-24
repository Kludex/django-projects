from django.utils import timezone

from django.core.management.base import BaseCommand

from paste.models import Paste

class Command(BaseCommand):
    help = """
            deletes pastes not updated in last 24 hrs

            Use this subcommand in a cron job
            to clear older pastes
           """
    def handle(self, **options):
        now = timezone.now()
        yesterday = now - timezone.timedelta(1)
        old_pastes = Paste.objects.filter(updated__lte=yesterday)
        old_pastes.delete()
