from django.shortcuts import render
from . import forms
from . import models
from django.views.generic import TemplateView
from cart.forms import CartAddProductForm


# Ляльки
class DollBeregyniaTable(TemplateView):
    product_form = forms.DollForm
    product_cart_form = CartAddProductForm

    def get(self, request):
        context = {}
        all_products = models.Doll.objects.filter(product_category__name='Берегиня')
        context['products'] = all_products
        context['product_form'] = self.product_form
        context['cart_product_form'] = self.product_cart_form
        return render(request, 'products/Beregynia.html', context)


class DollBlagodatTable(TemplateView):
    product_form = forms.DollForm
    product_cart_form = CartAddProductForm

    def get(self, request):
        context = {}
        all_products = models.Doll.objects.filter(product_category__name='Благодать')
        context['products'] = all_products
        context['product_form'] = self.product_form
        context['cart_product_form'] = self.product_cart_form
        return render(request, 'products/Blagodat.html', context)


class DollCholovichijOberigTable(TemplateView):
    product_form = forms.DollForm
    product_cart_form = CartAddProductForm

    def get(self, request):
        context = {}
        all_products = models.Doll.objects.filter(product_category__name='Чоловічий оберіг')
        context['products'] = all_products
        context['product_form'] = self.product_form
        context['cart_product_form'] = self.product_cart_form
        return render(request, 'products/CholovichijOberig.html', context)


class DollVjazaniLialkiTable(TemplateView):
    product_form = forms.DollForm
    product_cart_form = CartAddProductForm

    def get(self, request):
        context = {}
        all_products = models.Doll.objects.filter(product_category__name='В"язані ляльки')
        context['products'] = all_products
        context['product_form'] = self.product_form
        context['cart_product_form'] = self.product_cart_form
        return render(request, 'products/VjazaniLialki.html', context)


class DollGospodarBlogopoluchTable(TemplateView):
    product_form = forms.DollForm
    product_cart_form = CartAddProductForm

    def get(self, request):
        context = {}
        all_products = models.Doll.objects.filter(product_category__name='Господарочка-блогополучниця')
        context['products'] = all_products
        context['product_form'] = self.product_form
        context['cart_product_form'] = self.product_cart_form
        return render(request, 'products/Gospodar-blogopoluch.html', context)


class DollHarakternaLialkaTable(TemplateView):
    product_form = forms.DollForm
    product_cart_form = CartAddProductForm

    def get(self, request):
        context = {}
        all_products = models.Doll.objects.filter(product_category__name='Характерна лялька')
        context['products'] = all_products
        context['product_form'] = self.product_form
        context['cart_product_form'] = self.product_cart_form
        return render(request, 'products/HarakternaLialka.html', context)


class DollJangolTable(TemplateView):
    product_form = forms.DollForm
    product_cart_form = CartAddProductForm

    def get(self, request):
        context = {}
        all_products = models.Doll.objects.filter(product_category__name='Янгол')
        context['products'] = all_products
        context['product_form'] = self.product_form
        context['cart_product_form'] = self.product_cart_form
        return render(request, 'products/Jangol.html', context)


class DollKozaTable(TemplateView):
    product_form = forms.DollForm
    product_cart_form = CartAddProductForm

    def get(self, request):
        context = {}
        all_products = models.Doll.objects.filter(product_category__name='Коза')
        context['products'] = all_products
        context['product_form'] = self.product_form
        context['cart_product_form'] = self.product_cart_form
        return render(request, 'products/Koza.html', context)


class DollKrupjanychkaTable(TemplateView):
    product_form = forms.DollForm
    product_cart_form = CartAddProductForm

    def get(self, request):
        context = {}
        all_products = models.Doll.objects.filter(product_category__name='Круп"яничка')
        context['products'] = all_products
        context['product_form'] = self.product_form
        context['cart_product_form'] = self.product_cart_form
        return render(request, 'products/Krupjanychka.html', context)


class DollKuvadkaTable(TemplateView):
    product_form = forms.DollForm
    product_cart_form = CartAddProductForm

    def get(self, request):
        context = {}
        all_products = models.Doll.objects.filter(product_category__name='Кувадка')
        context['products'] = all_products
        context['product_form'] = self.product_form
        context['cart_product_form'] = self.product_cart_form
        return render(request, 'products/Kuvadka.html', context)


class DollLyhomankaTable(TemplateView):
    product_form = forms.DollForm
    product_cart_form = CartAddProductForm

    def get(self, request):
        context = {}
        all_products = models.Doll.objects.filter(product_category__name='Лихоманка')
        context['products'] = all_products
        context['product_form'] = self.product_form
        context['cart_product_form'] = self.product_cart_form
        return render(request, 'products/Lyhomanka.html', context)


class DollMaterynstvoTable(TemplateView):
    product_form = forms.DollForm
    product_cart_form = CartAddProductForm

    def get(self, request):
        context = {}
        all_products = models.Doll.objects.filter(product_category__name='Материнство')
        context['products'] = all_products
        context['product_form'] = self.product_form
        context['cart_product_form'] = self.product_cart_form
        return render(request, 'products/Materynstvo.html', context)


class DollMetlushkaTable(TemplateView):
    product_form = forms.DollForm
    product_cart_form = CartAddProductForm

    def get(self, request):
        context = {}
        all_products = models.Doll.objects.filter(product_category__name='Метлушка')
        context['products'] = all_products
        context['product_form'] = self.product_form
        context['cart_product_form'] = self.product_cart_form
        return render(request, 'products/Metlushka.html', context)


class DollNaKukurudziTable(TemplateView):
    product_form = forms.DollForm
    product_cart_form = CartAddProductForm

    def get(self, request):
        context = {}
        all_products = models.Doll.objects.filter(product_category__name='На кукурудзі')
        context['products'] = all_products
        context['product_form'] = self.product_form
        context['cart_product_form'] = self.product_cart_form
        return render(request, 'products/NaKukurudzi.html', context)


class DollNaSchastiaTable(TemplateView):
    product_form = forms.DollForm
    product_cart_form = CartAddProductForm

    def get(self, request):
        context = {}
        all_products = models.Doll.objects.filter(product_category__name='На щастя')
        context['products'] = all_products
        context['product_form'] = self.product_form
        context['cart_product_form'] = self.product_cart_form
        return render(request, 'products/NaSchastia.html', context)


class DollNerozluchnykyTable(TemplateView):
    product_form = forms.DollForm
    product_cart_form = CartAddProductForm

    def get(self, request):
        context = {}
        all_products = models.Doll.objects.filter(product_category__name='Нерозлучники')
        context['products'] = all_products
        context['product_form'] = self.product_form
        context['cart_product_form'] = self.product_cart_form
        return render(request, 'products/Nerozluchnyky.html', context)


class DollOchysnaTable(TemplateView):
    product_form = forms.DollForm
    product_cart_form = CartAddProductForm

    def get(self, request):
        context = {}
        all_products = models.Doll.objects.filter(product_category__name='Очисна')
        context['products'] = all_products
        context['product_form'] = self.product_form
        context['cart_product_form'] = self.product_cart_form
        return render(request, 'products/Ochysna.html', context)


class DollPastkaDliaSnivTable(TemplateView):
    product_form = forms.DollForm
    product_cart_form = CartAddProductForm

    def get(self, request):
        context = {}
        all_products = models.Doll.objects.filter(product_category__name='Пастка для снів')
        context['products'] = all_products
        context['product_form'] = self.product_form
        context['cart_product_form'] = self.product_cart_form
        return render(request, 'products/PastkaDliaSniv.html', context)


class DollPodorognyciaTable(TemplateView):
    product_form = forms.DollForm
    product_cart_form = CartAddProductForm

    def get(self, request):
        context = {}
        all_products = models.Doll.objects.filter(product_category__name='Подорожниця')
        context['products'] = all_products
        context['product_form'] = self.product_form
        context['cart_product_form'] = self.product_cart_form
        return render(request, 'products/Podorognycia.html', context)


class DollPodushaPodrugkaTable(TemplateView):
    product_form = forms.DollForm
    product_cart_form = CartAddProductForm

    def get(self, request):
        context = {}
        all_products = models.Doll.objects.filter(product_category__name='Подушка-подружка')
        context['products'] = all_products
        context['product_form'] = self.product_form
        context['cart_product_form'] = self.product_cart_form
        return render(request, 'products/PodushaPodrugka.html', context)


class DollShytiLialkiTable(TemplateView):
    product_form = forms.DollForm
    product_cart_form = CartAddProductForm

    def get(self, request):
        context = {}
        all_products = models.Doll.objects.filter(product_category__name='Шиті ляльки')
        context['products'] = all_products
        context['product_form'] = self.product_form
        context['cart_product_form'] = self.product_cart_form
        return render(request, 'products/ShytiLialki.html', context)


class DollStovbychkaTable(TemplateView):
    product_form = forms.DollForm
    product_cart_form = CartAddProductForm

    def get(self, request):
        context = {}
        all_products = models.Doll.objects.filter(product_category__name='Стовбичка')
        context['products'] = all_products
        context['product_form'] = self.product_form
        context['cart_product_form'] = self.product_cart_form
        return render(request, 'products/Stovbychka.html', context)


class DollVeduchkaTable(TemplateView):
    product_form = forms.DollForm
    product_cart_form = CartAddProductForm

    def get(self, request):
        context = {}
        all_products = models.Doll.objects.filter(product_category__name='Ведучка')
        context['products'] = all_products
        context['product_form'] = self.product_form
        context['cart_product_form'] = self.product_cart_form
        return render(request, 'products/Veduchka.html', context)


class DollVelykodniaTable(TemplateView):
    product_form = forms.DollForm
    product_cart_form = CartAddProductForm

    def get(self, request):
        context = {}
        all_products = models.Doll.objects.filter(product_category__name='Великодня')
        context['products'] = all_products
        context['product_form'] = self.product_form
        context['cart_product_form'] = self.product_cart_form
        return render(request, 'products/Velykodnia.html', context)


class DollVerbnaTable(TemplateView):
    product_form = forms.DollForm
    product_cart_form = CartAddProductForm

    def get(self, request):
        context = {}
        all_products = models.Doll.objects.filter(product_category__name='Вербна')
        context['products'] = all_products
        context['product_form'] = self.product_form
        context['cart_product_form'] = self.product_cart_form
        return render(request, 'products/Verbna.html', context)


class DollPodrudziaTable(TemplateView):
    product_form = forms.DollForm
    product_cart_form = CartAddProductForm

    def get(self, request):
        context = {}
        all_products = models.Doll.objects.filter(product_category__name='Подружжя')
        context['products'] = all_products
        context['product_form'] = self.product_form
        context['cart_product_form'] = self.product_cart_form
        return render(request, 'products/Podrudzia.html', context)


class DollVesniankaTable(TemplateView):
    product_form = forms.DollForm
    product_cart_form = CartAddProductForm

    def get(self, request):
        context = {}
        all_products = models.Doll.objects.filter(product_category__name='Веснянка')
        context['products'] = all_products
        context['product_form'] = self.product_form
        context['cart_product_form'] = self.product_cart_form
        return render(request, 'products/Vesnianka.html', context)
