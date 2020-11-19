from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length = 30)

    def save_location(self):
        self.save()

    def delete(self):
        self.delete()
    def update(self,field,val):
        Location.objects.get(id=self.id).update(field=val)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 30)
    def save_category(self):

        self.save()

    def delete(self):

        Category.objects.get(id=self.id).delete()

    def update(self,field,val):

        Category.objects.get(id=self.id).update(field=val)
        
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"

class Image(models.Model):
    name = models.CharField(max_length = 30)
    image = CloudinaryField('image', null=True)
    description = models.TextField()
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save_image(self):
        self.save()

    def delete_image(self):
        Image.objects.get(id = self.id).delete()

    def update_image(self, val):
        Image.objects.filter(id = self.id).update(name=val)

    @classmethod
    def get_image_by_id(cls,image_id):
        return cls.objects.get(ide=image_id)
    @classmethod
    def get_images(cls):
        return cls.objects.all()
    @classmethod
    def search_image(cls,category):
        searched_image = cls.objects.filter(category__name__icontains=category)
        return searched_image
    @classmethod
    def filter_by_location(cls,location):
        img_location = Location.objects.get(name=location)
        return cls.objects.filter(location_id=img_location.id)
    def __str__(self):
        return self.name
