from django.urls import path,include
from .views import ContactListView,MessageDetailView,AddContactView
urlpatterns = [
    path('',ContactListView.as_view(),name='contact-list'),
    path('add/',AddContactView.as_view(),name='add-contact'),
    path('<int:pk>/',MessageDetailView.as_view(),name='send-message')
]