from django.shortcuts import render
from django.views.generic import DetailView

from .models import Closet, Chest_of_drawers, Bed, TV_stand, Kitchen_Area, Dinner_table, Corner_sofa, Baby_bed, Footwear_stand, Chair, Coffee_table, Hinged_shelf, Computer_desk, Cupboard, Straight_sofa

# Create your views here.

def test_view(request):
    return render(request, 'base.html', {})


class ProductDetailView(DetailView):

    CT_MODEL_CLASS = {
        'closet' : Closet,
        'chest_of_drawers' : Chest_of_drawers,
        'bed' : Bed,
        'tv_stand' :  TV_stand,
        'kitchen_area' : Kitchen_Area,
        'dinner_table' : Dinner_table,
        'corner_sofa' : Corner_sofa,
        'baby_bed' : Baby_bed,
        'footwear_stand' : Footwear_stand,
        'chair' : Chair,
        'coffee_table' : Coffee_table,
        'hinged_shelf' : Hinged_shelf,
        'computer_desk' : Computer_desk,
        'cupboard' : Cupboard,
        'straight_sofa' : Straight_sofa
    }
    
    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_CLASS[kwargs['ct_model']]
        self.queryset=self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

        

    # Model = model
    # queryset = Model.objects.all()
    context_object_name = 'product'
    template_name = 'product_detail.html'
    slud_url_kwarg = 'slug'
