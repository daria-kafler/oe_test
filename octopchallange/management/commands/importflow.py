from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
  help = "Import data flow file to the system"

  def add_arguments(self, parser):
    parser.add_argument('filepath', type=str, help='data flow file path')

  def handle(self, *args, **options):
    filepath = options["filepath"]
    print(f'Importing file: {filepath}')
    
    file = open(filepath, 'r')
    lines = file.readlines()

    count = 0
    for line in lines:
      fields = line.split("|")
      type = fields[0]
      if type == '026':      
        mpan = fields[1]
      if type == '028':        
        meter_id = fields[1]
      if type == '030':
        print(f'MPAN: {mpan}, Meter ID: {meter_id}, Meter Register: {fields[1]}, DateTime: {fields[2]}, Reading: {fields[3]}')
        count+=1
    print(f'Total Readings: {count}')