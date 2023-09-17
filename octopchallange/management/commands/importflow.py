import decimal
import os
from time import strftime, strptime
from django.core.management.base import BaseCommand, CommandError
from octopchallange.models import Reading

class Command(BaseCommand):
  help = "Import data flow file to the system"

  def add_arguments(self, parser):
    parser.add_argument('filepath', type=str, help='data flow file path')

  def handle(self, *args, **options):
    '''Imports and parses a flow file'''

    filepath = options["filepath"]
    filename = os.path.basename(filepath)
    self.stdout.write((f'Importing file: {filepath}'))
    file = open(filepath, 'r')
    lines = file.readlines()

    count = 0
    # For each line in the flow file, splits the data into workable chunks and checks the first field to assess the lines type.
    # Ideally we would have these as enum for "026=MPAN Cores", "028=Meter/Reading Types" and "030=030Register Readings".
    for line in lines:
      fields = line.split("|")
      type = fields[0]
      if type == '026':      
        mpan = fields[1]
      if type == '028':        
        meter_id = fields[1]
      if type == '030':
        meter_register=fields[1]
        # Hacky conversion between DateTime format. Couldn't find how ot directly convert into the format django wants.
        reading_date_time=strftime('%Y-%m-%d %H:%M:%S', strptime(fields[2], '%Y%m%d%H%M%S'))
        register_reading=decimal.Decimal(fields[3])
        reading = Reading(mpan=int(mpan), meter_id=meter_id, meter_register=meter_register, reading_date_time=reading_date_time, register_reading=register_reading, flow_file=filename)
        try:
          reading.save()
          count+=1
          self.stdout.write(
            self.style.SUCCESS(f'Successfully added MPAN: {mpan}, Meter ID: {meter_id}, Meter Register: {meter_register}, DateTime: {reading_date_time}, Reading: {register_reading}')
          )
        except(CommandError):
          self.stdout.write(
          self.style.ERROR('Oops, something went wrong!')
        )
      else:
          self.stdout.write(
          self.style.ERROR('A type is missing. Check that the line containes all required types')
        )
    self.stdout.write(
          self.style.SUCCESS(f'Added {count} readings')
        )