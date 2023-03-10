import os
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'tango_with_django_project.settings')

import django

django.setup()
from rango.models import Category, Page


def populate():
    python_pages = [
        {
            'title': 'Official Python Tutorial',
            'url': 'http://docs.python.org/3/tutorial/'
        },
        {
            'title': 'How to Think like a Computer Scientist',
            'url': 'http://www.greenteapress.com/thinkpython/'
        },
        {
            'title': 'Learn Python in 10 Minutes',
            'url': 'http://www.korokithakis.net/tutorials/python/'
        }
    ]

    django_pages = [
        {
            'title': 'Official Django Tutorial',
            'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/'
        },
        {
            'title': 'Django Rocks',
            'url': 'http://www.djangorocks.com/'
        },
        {
            'title': 'How to Tango with Django',
            'url': 'http://www.tangowithdjango.com/'
        }
    ]

    other_pages = [
        {
            'title': 'Bottle',
            'url': 'http://bottlepy.org/docs/dev/'
        },
        {
            'title': 'Flask',
            'url': 'http://flask.pocoo.org'
        }
    ]

    cats = {
        'Python': {
            'pages': python_pages,
            'views': 128,
            'likes': 64
        },
        'Django': {
            'pages': django_pages,
            'views': 64,
            'likes': 32
        },
        'Other Frameworks': {
            'pages': other_pages,
            'views': 32,
            'likes': 16
        }
    }

    for cat, cat_data in cats.items():
        c = Category.objects.get_or_create(name=cat)[0]
        c.views = cat_data.get('views', 0)
        c.likes = cat_data.get('likes', 0)
        c.save()
        for _cat_data in cat_data['pages']:
            p = Page.objects.get_or_create(category=c, title=_cat_data['title'])[0]
            p.url = _cat_data['url']
            p.views = random.randint(0, 128)
            p.save()

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f"- {c}: {p}")


if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
