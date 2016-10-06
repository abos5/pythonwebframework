from django.test import TestCase
import markdown2
markdown_path = markdown2.markdown_path

filenames = [
    'a.md'
]

for filename in filenames:
    html = markdown_path('fixtures/%s' % filename)
    print(html)


# Create your tests here.
