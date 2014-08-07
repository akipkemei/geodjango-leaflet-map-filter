from django.contrib.gis import admin as geoadmin
from website.models import ApartmentsNY

class ApartmentsNYAdmin(geoadmin.OSMGeoAdmin):

    list_display = ('name', 'city', 'price', 'wifi', 'breakfast')
    search_fields = ['name']
    list_filter = ('city',)
    default_lon =  -8236306.48
    default_lat =  5028376.23
    default_zoom = 5
    
geoadmin.site.register(ApartmentsNY, ApartmentsNYAdmin)
