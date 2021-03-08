# from PIL import Image

from django.forms import ModelChoiceField  #, ModelForm, ValidationError
from django.contrib import admin
# from django.utils.safestring import mark_safe

from  .models import  *

# Register your models here.

# class ClosetAdminForm(ModelForm):

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['image'].help_text = mark_safe(
#         """<span style = "color : red; font-size : 14px;"> При загрузке изображения с разришением больше {}x{} оно юудет обрезано! </span>"""
#         .format(*Product.MAX_RESOLUTION))

#     def clean_image(self): #Для определения размера изображения
#        image = self.cleaned_data['image']
#        img = Image.open(image)
#        min_height, min_width = Product.MIN_RESOLUTION
#        max_height, max_width = Product.MAX_RESOLUTION
#        if image.size > Product.MAX_IMAGE_SIZE:
#            raise ValidationError('Размер изображения не должен привышать 3Мб!')
#        if img.height < min_height or img.width < min_width:
#            raise ValidationError('Разрешение изображение меньше минимального!')
#        if img.height > min_height or img.width > max_width:
#            raise ValidationError('Разрешение изображение больше максимального!')
#        return image


class ClosetAdmin(admin.ModelAdmin):

    # form = ClosetAdminForm
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slag = 'closets'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



class Chest_of_drawersAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'chest_of_drawers':
            return ModelChoiceField(Category.objects.filter(slag = 'chest_of_drawerss'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



class BedAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'Beds':
            return ModelChoiceField(Category.objects.filter(slag = 'Beds'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



class TV_standAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'TV_stands':
            return ModelChoiceField(Category.objects.filter(slag = 'TV_stands'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



class Kitchen_AreaAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'Kitchen_Areas':
            return ModelChoiceField(Category.objects.filter(slag = 'Kitchen_Areas'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



class Dinner_tableAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'Dinner_tables':
            return ModelChoiceField(Category.objects.filter(slag = 'Dinner_tables'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



class Corner_sofaAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'Corner_sofas':
            return ModelChoiceField(Category.objects.filter(slag = 'Corner_sofas'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



class Baby_bedAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'Baby_beds':
            return ModelChoiceField(Category.objects.filter(slag = 'Baby_beds'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



class Footwear_standAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'Footwear_stands':
            return ModelChoiceField(Category.objects.filter(slag = 'Footwear_stands'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



class ChairAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'Chairs':
            return ModelChoiceField(Category.objects.filter(slag = 'Chairs'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



class Coffee_tablesAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'Coffee_tables':
            return ModelChoiceField(Category.objects.filter(slag = 'Coffee_tables'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



class Hinged_shelfAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'Hinged_shelfs':
            return ModelChoiceField(Category.objects.filter(slag = 'cHinged_shelfs'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



class Computer_deskAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'Computer_desks':
            return ModelChoiceField(Category.objects.filter(slag = 'Computer_desks'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



class CupboardAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'Cupboards':
            return ModelChoiceField(Category.objects.filter(slag = 'Cupboards'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



class Straight_sofaAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'Straight_sofa':
            return ModelChoiceField(Category.objects.filter(slag = 'Straight_sofas'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Closet, ClosetAdmin)
admin.site.register(Chest_of_drawers, Chest_of_drawersAdmin)
admin.site.register(Bed, BedAdmin)
admin.site.register(TV_stand, TV_standAdmin)
admin.site.register(Kitchen_Area, Kitchen_AreaAdmin)
admin.site.register(Dinner_table,Dinner_tableAdmin)
admin.site.register(Corner_sofa, Corner_sofaAdmin)
admin.site.register(Baby_bed, Baby_bedAdmin)
admin.site.register(Footwear_stand, Footwear_standAdmin)
admin.site.register(Chair, ChairAdmin)
admin.site.register(Coffee_table, Coffee_tablesAdmin)
admin.site.register(Hinged_shelf, Hinged_shelfAdmin)
admin.site.register(Computer_desk, Computer_deskAdmin)
admin.site.register(Cupboard, CupboardAdmin)
admin.site.register(Straight_sofa, Straight_sofaAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
