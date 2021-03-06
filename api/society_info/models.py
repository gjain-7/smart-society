from django.db import models
from django.utils.translation import ugettext_lazy as _


class Property_Info(models.Model):
    def __init__(self, *args, **kwargs):
        super(Property_Info, self).__init__(*args, **kwargs)
        self.__original_property_type = self.property_type
        self.__original_maintenance = self.maintenance
        self.__original_covered_area = self.covered_area

    property_type = models.CharField(
        _("Property Type"), max_length=25, primary_key=True
    )
    maintenance = models.IntegerField(_("Maintenance Amount"))
    covered_area = models.IntegerField(
        _("Covered Area"),
    )

    def __str__(self):
        return self.property_type

    class Meta:
        verbose_name = "Property Info"
        verbose_name_plural = "Properties"
        ordering = ["property_type"]


class Inventory(models.Model):
    def __init__(self, *args, **kwargs) -> None:
        super(Inventory, self).__init__(*args, **kwargs)
        self.__original_item = self.item
        self.__original_quantity = self.quantity

    item = models.CharField(_("Inventory Item"), max_length=50, primary_key=True)
    quantity = models.IntegerField(
        _("Quantity"),
    )

    def __str__(self):
        return self.item

    class Meta:
        verbose_name = "Inventory"
        verbose_name_plural = "Inventory Items"
        ordering = ["item"]


class Announcement(models.Model):
    categories = (
        ("Notification", "Notification"),
        ("Voting Result", "Voting Result"),
        ("Complaint", "Complaint"),
    )
    s_no = models.AutoField(primary_key=True)
    date = models.DateTimeField(_("Date and Time"), auto_now_add=True)
    author = models.CharField(_("Announcement Made by"), max_length=25)
    category = models.CharField(_("Category"), max_length=25, choices=categories)
    description = models.TextField(_("Description"))

    def save(self, *args, **kwargs):
        if not self.description:
            self.description = None
        super(Announcement, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-date"]
