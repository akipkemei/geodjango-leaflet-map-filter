from django.contrib.gis.db import models
from django.utils import timezone
from autoslug import AutoSlugField
from easy_thumbnails.fields import ThumbnailerImageField

def image_upload_folder(instance, filename):
	return "apartments_images/%s" % (filename)

choices_city = (		
	('New York City', 'NYC'),
	('Syracuse', 'Syracuse'),
	('Buffalo', 'Buffalo'),
	('Rochester', 'Rochester'),
	('Yonkers', 'Yonkers')
)

class ApartmentsNY(models.Model):
	name = models.CharField("Name of the apartment", max_length=50)
	slug = AutoSlugField(populate_from='name', unique=True) 
	city = models.CharField("City", max_length=70, choices=choices_city)
	price = models.IntegerField("Price per night [$]")
	wifi = models.BooleanField("WiFi", default=False)
	breakfast = models.BooleanField("Breakfast", default=False)
	image = ThumbnailerImageField(upload_to=image_upload_folder, blank=True)

	geom = models.PointField(srid=4326)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Apartments in NY"

