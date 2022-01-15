from django.shortcuts import redirect, render
from django.views.generic import TemplateView, CreateView, DetailView, DeleteView
from .forms import ProductForm
from django.urls import reverse_lazy
from .models import Images, Product

# Create your views here.
class HomeView(TemplateView):
	template_name = "home.html"
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['productlist'] = Product.objects.all()[::-1]
		return context
	

# add product
class AddPoductView(CreateView):
	template_name = "add_product.html"
	form_class = ProductForm
	success_url = reverse_lazy('home')


# delete product (/1/delete)
class DeleteProductView(DeleteView):
	model = Product
	success_url = reverse_lazy('home')

class DeleteImageView(DeleteView):
	model = Images
	success_url = reverse_lazy('home')

	# def get_context_data(self, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	context['product'] = Product.objects.all()[::-1]
	# 	return context
   
	
# product detail   
class ProductDetailView(TemplateView):
	template_name = "product_detail.html"
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['productobj'] = Product.objects.get(id = self.kwargs['pk'])
		return context
	
	
# add images of product
class AddProductImagesView(TemplateView):
	template_name = "add_images.html"
	
	def post(self, request,*args, **kwargs):
		try:
			images = request.FILES.getlist('images')
			product = Product.objects.get(id = self.kwargs['pk'])
			for image in images:
				product_image = Images.objects.create(
					product = product,
					images = image
				)
			return redirect('home')
		except Exception as e:
			print(e)