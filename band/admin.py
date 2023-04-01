from django.contrib import admin
from django.utils.html import format_html
from .models import Band

class BandAdmin(admin.ModelAdmin):
    """
    Customizes the Django admin interface for the Band model.
    """
    list_display = ('name', 'date_formed', 'genre', 'description', 'image_tag')
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        """
        Returns an HTML image tag with the preview of the image field.
        
        Parameters:
        -----------
        obj: Band object
            The object containing the image to preview.
            
        Returns:
        --------
        str:
            The HTML code for the image tag.
        """
        return format_html('<img src="{}" width="150" height="150" />'.format(obj.image.url) if obj.image else '-')

    image_tag.short_description = 'Image Preview'

admin.site.register(Band, BandAdmin)
