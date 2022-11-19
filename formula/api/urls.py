from django.urls import path, include
from rest_framework.routers import DefaultRouter
from formula import views


router = DefaultRouter()
router.register('recipes', views.RecipeViewSet)
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)

app_name = 'formula'

urlpatterns = [
    path('', include(router.urls)),
]