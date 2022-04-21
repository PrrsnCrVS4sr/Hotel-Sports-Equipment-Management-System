# coding: utf-8
from main.models import SportItem
SportItem.objects.create(name="Basketball", isBorrowed=False)
SportItem.objects.create(name="Tennis Raquet", isBorrowed=False)
SportItem.objects.create(name="Godt Cart", isBorrowed=False)
SportItem.objects.all()
