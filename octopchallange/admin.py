from django.contrib import admin

from octopchallange.models import Reading

# Register your models here.
class ReadingAdmin(admin.ModelAdmin):
    list_display = ('mpan', 'meter_id', 'meter_register', 'reading_date_time', 'register_reading', 'flow_file')
    search_fields = ('mpan', 'meter_id')

admin.site.register(Reading, ReadingAdmin)