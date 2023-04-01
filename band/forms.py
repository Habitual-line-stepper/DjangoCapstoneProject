from django import forms
from .models import Band

class BandForm(forms.ModelForm):
    """
    A form that is used to create and update Band objects in the database.

    This form is a ModelForm, which means that it is automatically generated
    from the Band model. The `Meta` class defines the fields that are included
    in the form and specifies the widgets that are used to render the form
    fields in the HTML template.

    Attributes:
        Meta (class): A class that defines metadata for the form, including
            the model that the form is based on, the fields that are included
            in the form, and the widgets that are used to render the form
            fields in the HTML template.
    """

    class Meta:
        """
        Metadata for the `BandForm` class.

        The `Meta` class defines the model that the form is based on, the fields
        that are included in the form, and the widgets that are used to render
        the form fields in the HTML template.

        Attributes:
            model (class): The model that the form is based on.
            fields (list): A list of fields that are included in the form.
            widgets (dict): A dictionary that maps field names to widget objects.
                Each widget object specifies how the corresponding form field
                should be rendered in the HTML template.
        """
        model = Band
        fields = ['name', 'date_formed', 'genre', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_formed': forms.DateInput(attrs={'class': 'form-control'}),
            'genre': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
