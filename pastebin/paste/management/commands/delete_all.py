from django.core.management.base import BaseCommand

from paste.models import Paste

class Command(BaseCommand):
    help = """
            deletes all pastes
           """

    def handle(self, **options):
        pastes = Paste.objects.all()
        pastes.delete()
