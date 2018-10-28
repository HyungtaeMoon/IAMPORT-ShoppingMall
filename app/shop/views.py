from django.shortcuts import render
from django.views.generic import ListView
from .models import Item

index = ListView.as_view(model=Item,
                         queryset=Item.objects.filter(
                             is_public=True
                         ))
