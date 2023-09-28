from django.db import models

from wagtail.models import Page
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet


class HomePage(Page):
    pass


class MyModel(models.Model):
    class MyChoices(models.TextChoices):
        # First value is the actual value stored in the database.
        # Second value is the display value, which should display in the admin.
        # The problem is that SnippetViewSet does not render the display value.
        CHOICE1 = "choice1", "Label Choice 1"
        CHOICE2 = "choice2", "Label Choice 2"
        CHOICE3 = "choice3", "Label Choice 3"

    choice_field = models.CharField(
        max_length=255,
        choices=MyChoices.choices,
        default=MyChoices.CHOICE1,
    )

    # You can create a custom method to get the display value for the choice field.
    # This is described here in the documentation: https://docs.wagtail.org/en/v5.1.2/topics/snippets/customising.html
    # def get_choice_field_display(self):
    #     return self.MyChoices(self.choice_field).label


# See wagtail_hooks.py for the ModelAdmin version.
# The ModelAdmin has the expected behavior, because it does use the display
# value for the choice field by default with no extra code required.
@register_snippet
class MyModelSnippetViewSet(SnippetViewSet):
    model = MyModel
    # This does not work properly. The choice field is rendered as the actual value stored in the database.
    list_display = ("choice_field",)

    # As a work around, you can specify a function to the display value for the choice field.
    # This is not ideal, because it requires extra code. It would be better if SnippetViewSet
    # was able to render the display value for the choice field by default.
    # list_display = ("get_choice_field_display",)
