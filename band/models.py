from django.db import models
from django.db import migrations
from django.contrib.auth.models import User

class Band(models.Model):
    """
    A class that represents a music band.

    Attributes:
        name (CharField): the name of the band.
        date_formed (DateField): the date when the band was formed.
        genre (CharField): the genre of music the band plays.
        description (TextField): a brief description of the band.
        image (ImageField): the image of the band.
        user (ForeignKey): the user who created the band.
    """
    name = models.CharField(max_length=100)
    date_formed = models.DateField()
    genre = models.CharField(max_length=100)
    description = models.TextField(default="Band description")
    image = models.ImageField(upload_to='band_images', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        """
        Returns:
            str: the name of the band.
        """
        return self.name


def set_default_id(apps, schema_editor):
    """
    A function to set default ID values for bands created before auto-incrementing IDs were implemented.

    Args:
        apps: a registry containing all installed apps.
        schema_editor: a class used to manipulate database schemas.

    Returns:
        None.
    """
    Band = apps.get_model('bands', 'Band')
    for band in Band.objects.all():
        band.id = band.pk
        band.save()

class Migration(migrations.Migration):
    """
    A class that represents a Django migration to set default ID values for bands created before auto-incrementing IDs were implemented.

    Attributes:
        dependencies (list): a list of migration dependencies.
        operations (list): a list of migration operations.
    """

    dependencies = [
        ('bands', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(set_default_id),
    ]
