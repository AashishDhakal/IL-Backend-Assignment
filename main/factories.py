from factory.fuzzy import FuzzyInteger, FuzzyDate
from main.models import MyModel
from factory.django import DjangoModelFactory
from datetime import datetime


class MyModelFactory(DjangoModelFactory):
    class Meta:
        model = MyModel

    date = FuzzyDate(
        start_date=datetime.fromisoformat('2022-01-01'),
        end_date=datetime.fromisoformat('2022-02-20')
    )
    distance = FuzzyInteger(low=10, high=100)
