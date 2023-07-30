from django.core.management import BaseCommand

from catalog_app.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()

        category_list = [
            {'pk': 1, 'name': 'Фрукт', 'desc': 'Свежие из Астрахани'},
            {'pk': 2, 'name': 'Овощи', 'desc': 'Свежие из Грузии'},
            {'pk': 3, 'name': 'Ягоды', 'desc': 'Свежие из Турции'},
            {'pk': 4, 'name': 'Сухофрукты', 'desc': 'Свежие из Ташкента'},
            {'pk': 5, 'name': 'Маринад', 'desc': 'Из Абхазии'},
        ]

        category_for_create = []
        for category_id in category_list:
            category_for_create.append(
                Category(**category_id)
            )

        Category.objects.bulk_create(category_for_create)


        products = [
            {'name': 'Абрикос', 'desc': 'Жёлтый', 'category_id': 1, 'price': '123'},
            {'name': 'Вишня', 'desc': 'Красная', 'category_id': 3, 'price': '456'},
            {'name': 'Салат', 'desc': 'Китайский', 'category_id': 2, 'price': '789'},
            {'name': 'Огурец', 'desc': 'Длинный', 'category_id': 2, 'price': '987'},
            {'name': 'Помидор', 'desc': 'Бычье сердце', 'category_id': 2, 'price': '654'},
            {'name': 'Арбуз', 'desc': 'Без косточек', 'category_id': 3, 'price': '321'},
            {'name': 'Изюм', 'desc': 'Обыкновенный', 'category_id': 4, 'price': '147'},
            {'name': 'Корнишон', 'desc': 'В банках', 'category_id': 5, 'price': '258'},
        ]

        products_for_create = []
        for prod in products:
            products_for_create.append(
                Product(**prod)
            )

        Product.objects.bulk_create(products_for_create)


