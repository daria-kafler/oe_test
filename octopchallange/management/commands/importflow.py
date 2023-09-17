import decimal
from time import strftime, strptime
from django.core.management.base import BaseCommand, CommandError
from octopchallange.models import Reading

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
        meter_register=fields[1]
        reading_date_time=strftime('%Y-%m-%d %H:%M:%S', strptime(fields[2], '%Y%m%d%H%M%S'))
        register_reading=decimal.Decimal(fields[3])

        print(f'MPAN: {mpan}, Meter ID: {meter_id}, Meter Register: {meter_register}, DateTime: {reading_date_time}, Reading: {register_reading}')
        reading = Reading(mpan=int(mpan), meter_id=meter_id, meter_register=meter_register, reading_date_time=reading_date_time, register_reading=register_reading)
        reading.save()
        print(f'Reading: {reading}')
        count+=1
    print(f'Total Readings: {count}')