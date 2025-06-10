from django.core.management.base import BaseCommand
global iface
class Command(BaseCommand):
    help = 'Lance l\'interface Gradio'

    def handle(self, *args, **options):
        iface.launch()        