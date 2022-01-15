
from django.urls import path
# import views
from .views import HomeView, AddPoductView, ProductDetailView, AddProductImagesView, DeleteProductView,DeleteImageView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('addproduct', AddPoductView.as_view(), name="addproduct"),
    path('productdetail/<int:pk>/', ProductDetailView.as_view(), name="productdetail"),
    path('addimage/<int:pk>/', AddProductImagesView.as_view(), name="addimage"),
    path('<pk>/delete/', DeleteProductView.as_view(), name="deleteproduct"),
    path('<pk>/deleteimage/', DeleteImageView.as_view(), name="deleteimage"),
]

