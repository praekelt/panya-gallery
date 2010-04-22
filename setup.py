from setuptools import setup, find_packages

setup(
    name='django-gallery',
    version='dev',
    description='Django gallery app.',
    author='Praekelt Consulting',
    author_email='dev@praekelt.com',
    url='https://github.com/praekelt/django-gallery',
    packages = find_packages(),
    install_requires = [
        'django-filter>=0.5.3',
    ],
    include_package_data=True,
)
