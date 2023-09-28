from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import MyModel


class MyModelAdmin(ModelAdmin):
    model = MyModel
    menu_label = "My Model (modeladmin)"
    menu_icon = "snippet"
    list_display = ("choice_field",)


modeladmin_register(MyModelAdmin)
