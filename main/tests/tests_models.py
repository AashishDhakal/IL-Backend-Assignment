from django.test import TestCase
from main.models import MyModel
from main import factories


class FactoryModel:
    """
    Base test case for models
    """
    def test_instance(self):
        getattr(factories, f'{self.model}Factory')().save()


class MyModelFactoryTestCase(FactoryModel, TestCase):
    model = 'MyModel'


class CollectibleTestCase(TestCase):
    """
    Test basic operations on MyModel
    """
    def test_create_my_model(self):
        # create MyModel
        my_model = factories.MyModelFactory(
            date='2022-01-22',
            distance=10
        )
        self.assertEqual(my_model.date, '2022-01-22')
        self.assertEqual(my_model.id, 1)
        self.assertEqual(my_model.distance, 10)

        my_model = factories.MyModelFactory(
            date='2022-01-22',
            distance=10
        )
        self.assertEqual(my_model.date, '2022-01-22')
        self.assertEqual(my_model.id, 2)
        self.assertEqual(my_model.distance, 10)

    def test_retrieve_my_model(self):
        # retrieve MyModel
        factories.MyModelFactory(
            date='2022-02-03',
            distance=20
        )

        my_model = MyModel.objects.get(
            date='2022-02-03', distance=20
        )
        self.assertEqual(str(my_model.date), '2022-02-03')
        self.assertEqual(my_model.distance, 20)

    def test_update_my_model(self):
        # update MyModel
        my_model = factories.MyModelFactory()
        my_model.date = '2022-02-01'
        my_model.save(
            update_fields=['date', ]
        )

        self.assertEqual(my_model.id, 1)
        self.assertEqual(my_model.date, '2022-02-01')

    def test_delete_my_model(self):
        # delete MyModel
        factories.MyModelFactory()
        self.assertEqual(MyModel.objects.count(), 1)

        my_model = MyModel.objects.get(id=1)
        my_model.delete()
        self.assertEqual(MyModel.objects.all().count(), 0)
