from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
  help = "Import data flow file to the system"

  def add_arguments(self, parser):
    parser.add_argument('filepath', type=str, help='data flow file path')

  def handle(self, *args, **options):
    print(f'Importing file: {options["filepath"]}')