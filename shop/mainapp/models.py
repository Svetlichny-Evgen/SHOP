# import sys
# from PIL import Image

from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.files.uploadedfile import InMemoryUploadedFile

from django.urls import reverse

# from io import BytesIO

User = get_user_model()

def get_product_url(obj, viewname):
    ct_model = obj__.__meta.model_name
    return reverse(viewname, kwargs={'ct_model': ct_model, 'slag': obj.slag})



# Create your models here.

#****************
#1 Category
#2 Product
#3 CartProduct
#4 Cart
#5 Order
#****************
#6 Customer


# class MinResolutionErrorException(Exception):
#     pass

# class MaxResolutionErrorException(Exception):
#     pass


class LatestProductManager:
    @staticmethod
    def get_product_for_main_page(*args, **kwargs):
        with_respect_to = kwargs.get('with_respect_to')
        product = []
        ct_models = ContentType.objects.filter(model__in=args)
        for ct_models in ct_models:
            model_products = ct_model.model_class()._base_manager.all().order_by('-id')[:5]
            products.extend(model_products)
        if with_respect_to:
            ct_model = ContentType.objects.filter(model = with_respect_to)
            if ct_model.exists():
                if with_respect_to in args:
                    return sorted(products, key = lambda x: x.__class__._meta.model_name.startswitch(with_respect_to), reverse = True
                    )
        return products





class LatestProducts:

    objects = LatestProductManager()




class Category(models.Model):

    name = models.CharField(max_length = 255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):

    # MIN_RESOLUTION = (400, 400)
    # MAX_RESOLUTION = (800, 800)
    # MAX_IMAGE_SIZE = 3145728

    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name="Категоря", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.title

    #def save(self, *args, **kwargs):#Для определения размера изображения
    #    #image = self.image
    #    #image = Image.Open(image)
    #    #min_height, min_width = self.MIN_RESOLUTION
    #    #max_height, max_width = self.MAX_RESOLUTION
    #    #if img.height < min_height or img.width < min_width:
    #    #    raise MinResolutionErrorException('Разрешение изображение меньше минимального!')
    #    #if img.height > min_height or img.width > max_width:
    #    #    raise MaxResolutionErrorException('Разрешение изображение больше максимального!')
    #    image = self.image#Для автоматического обрезания изображения
    #    img.open(image)
    #    new_img = img.convert('RGB')
    #    resized_new_image = new_img.resize((200, 200), Image.ANTIALIAS)
    #    filestream = BytesIO()
    #    resized_new_image.save(filestream(), 'JPEG', quality = 90)
    #    filestream.seek(0)
    #    name = '{}.{}'.format(self.image.name.split('.'))
    #    self.image = InMemoryUploadedFile(filestream, 'ImageField', name, 'jpeg/image', sys.getsizeof(filestream) ,None)
    #    super().save(*args, **kwargs)


class Closet(Product):

    qty_doors = models.CharField(max_length=255, verbose_name = 'Количество дверей')
    height = models.CharField(max_length=255, verbose_name = 'Высота')
    long = models.CharField(max_length=255, verbose_name = 'Длина')
    depth = models.CharField(max_length=255, verbose_name = 'Глубина')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def det_absolute_url(self):
        return get_product_url(self, 'product_detail')

class Chest_of_drawers(Product):
    long = models.CharField(max_length=255, verbose_name = 'Длина')
    height = models.CharField(max_length=255, verbose_name = 'Высота')
    depth = models.CharField(max_length=255, verbose_name = 'Глубина')
    qty_boxes = models.CharField(max_length=255, verbose_name = 'Количество ящиков')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def det_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Bed(Product):
    bed_size_options = models.CharField(max_length=255, verbose_name = 'Варианты размеров спального места')
    long = models.CharField(max_length=255, verbose_name = 'Длина')
    width = models.CharField(max_length=255, verbose_name = 'Ширина')
    compartment_for_linen = models.BooleanField(default = True)

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def det_absolute_url(self):
        return get_product_url(self, 'product_detail')


class TV_stand(Product):
    long = models.CharField(max_length=255, verbose_name = 'Длина')
    height = models.CharField(max_length=255, verbose_name = 'Высота')
    depth = models.CharField(max_length=255, verbose_name = 'Глубина')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def det_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Kitchen_Area(Product):
    long = models.CharField(max_length=255, verbose_name = 'Длина')
    height = models.CharField(max_length=255, verbose_name = 'Высота')
    presence_of_drawers_for_dishes = models.CharField(max_length=255, verbose_name = 'Наличие ящиков для посуды')
    table_opens = models.BooleanField(default = True)

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def det_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Dinner_table(Product):
    countertop_materials = models.CharField(max_length=255, verbose_name = 'Материалы столешницы')
    body_materials = models.CharField(max_length=255, verbose_name = 'Материалы корпуса')
    long = models.CharField(max_length=255, verbose_name = 'Длина')
    height = models.CharField(max_length=255, verbose_name = 'Высота')
    width = models.CharField(max_length=255, verbose_name = 'Ширина')
    unfolded_size = models.CharField(max_length=255, verbose_name = 'Размер в разложенном виде')
    table_opens = models.BooleanField(default = True)

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def det_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Corner_sofa(Product):
    transformation_mechanism = models.CharField(max_length=255, verbose_name = 'Механизм трансформации')
    angle_length = models.CharField(max_length=255, verbose_name = 'Длина угла')
    length_of_corner_sofa = models.CharField(max_length=255, verbose_name = 'Длина углового дивана')
    length_of_bed_of_corner_sofa = models.CharField(max_length=255, verbose_name = 'Длина спального места углового дивана')
    bed_width_corner_sofa = models.CharField(max_length=255, verbose_name = 'Ширина спального места углового дивана')
    compartment_for_linen = models.BooleanField(default = True)

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def det_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Baby_bed(Product):
    facade = models.CharField(max_length=255, verbose_name = 'Фасад')
    bed_height = models.CharField(max_length=255, verbose_name = 'Высота кровати')
    bed_length = models.CharField(max_length=255, verbose_name = 'Длина кровати')
    bed_width = models.CharField(max_length=255, verbose_name = 'Ширина кровати')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)
    
    def det_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Footwear_stand(Product):
    body_materials = models.CharField(max_length=255, verbose_name = 'Материалы корпуса')
    facade = models.CharField(max_length=255, verbose_name = 'Фасад')
    long = models.CharField(max_length=255, verbose_name = 'Длина')
    height = models.CharField(max_length=255, verbose_name = 'Высота')
    depth = models.CharField(max_length=255, verbose_name = 'Глубина')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def det_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Chair(Product):
    height = models.CharField(max_length=255, verbose_name = 'Высота')
    depth = models.CharField(max_length=255, verbose_name = 'Глубина')
    width = models.CharField(max_length=255, verbose_name = 'Ширина')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def det_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Coffee_table(Product):
    long = models.CharField(max_length=255, verbose_name = 'Длина')
    height = models.CharField(max_length=255, verbose_name = 'Высота')
    width = models.CharField(max_length=255, verbose_name = 'Ширина')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def det_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Hinged_shelf(Product):
    long = models.CharField(max_length=255, verbose_name = 'Длина')
    height = models.CharField(max_length=255, verbose_name = 'Высота')
    depth = models.CharField(max_length=255, verbose_name = 'Глубина')
    material = models.CharField(max_length=255, verbose_name = 'Материал')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)
    def det_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Computer_desk(Product):
    long = models.CharField(max_length=255, verbose_name = 'Длина')
    height = models.CharField(max_length=255, verbose_name = 'Высота')
    width = models.CharField(max_length=255, verbose_name = 'Ширина')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def det_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Cupboard(Product):
    qty_doors = models.CharField(max_length=255, verbose_name = 'Количество дверей')
    height = models.CharField(max_length=255, verbose_name = 'Высота')
    long = models.CharField(max_length=255, verbose_name = 'Длина')
    depth = models.CharField(max_length=255, verbose_name = 'Глубина')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def det_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Straight_sofa(Product):
    transformation_mechanism = models.CharField(max_length=255, verbose_name = 'Механизм трансформации')
    height = models.CharField(max_length=255, verbose_name = 'Высота')
    length = models.CharField(max_length=255, verbose_name = 'Длина')
    depth = models.CharField(max_length=255, verbose_name = 'Глубина')
    filler = models.CharField(max_length=255, verbose_name = 'Наполнитель')
    compartment_for_linen = models.BooleanField(default = True)

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def det_absolute_url(self):
        return get_product_url(self, 'product_detail')


class CartProduct(models.Model):

    user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE, related_name = 'related_product')
    content_type = models.ForeignKey(ContentType, on_delete = models.CASCADE)
    object_id = models.PositiveIntegerField(default=0)
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1)#Кол-во
    total_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')

    def __str__(self):
        return "Продукты {} (для корзины)".format(self.product.title)

class Cart(models.Model):
    owner = models.ForeignKey('Customer', verbose_name='Владелец', on_delete=models.CASCADE)
    product = models.ManyToManyField(CartProduct, blank=True, related_name = 'related_cart' )
    total_product = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits = 9, decimal_places=2, verbose_name='Общая цена')

    def __str__(self):
        return str(self.id)

class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    address = models.CharField(max_length=255, verbose_name='Адрес')

    def __str__(self):
        return "Покупатель: {} {}".format(self.user.first_name, self.user.last_name)
