from django.forms import ModelForm
from . import models


class DollCategoryForm(ModelForm):
    class Meta:
        model = models.Doll_Category
        fields = ('name',)


class DollForm(ModelForm):
    class Meta:
        model = models.Doll
        fields = ("product_category", "availability", "time", "price", "size_height", "pictures", "special")


class DekupazhCategoryForm(ModelForm):
    class Meta:
        model = models.Dekupazh_Category
        fields = ('name',)


class DekupazhForm(ModelForm):
    class Meta:
        model = models.Dekupazh
        fields = ("product_category", "availability", "time", "price", "size_height", "size_width", "pictures", "special")


class SkrapbukingCategoryForm(ModelForm):
    class Meta:
        model = models.Skrapbuking_Category
        fields = ('name',)


class SkrapbukingForm(ModelForm):
    class Meta:
        model = models.Skrapbuking
        fields = ("product_category", "availability", "time", "price", "size_height", "size_width", "pictures", "special")


class ServetkyCategoryForm(ModelForm):
    class Meta:
        model = models.Servetky_Category
        fields = ('name',)


class ServetkyForm(ModelForm):
    class Meta:
        model = models.Servetky
        fields = ("product_category", "availability", "time", "price", "quantity", "pictures", "special")


class OtherCategoryForm(ModelForm):
    class Meta:
        model = models.Servetky_Category
        fields = ('name',)


class MyloForm(ModelForm):
    class Meta:
        model = models.Mylo
        fields = ("product_category", "availability", "time", "price", "pictures", "special")


class BizhuteriaForm(ModelForm):
    class Meta:
        model = models.Bizhuteria
        fields = ("product_category", "availability", "time", "price", "pictures", "special")
