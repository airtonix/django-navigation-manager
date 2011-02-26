from distutils.core import setup
from setuptools import find_packages, setup
setup(
	name='django_navigation_manager',
	version='0.0.2dev',
	maintainer = "Zenobius Jiricek",
	maintainer_email = "airtonix@gmail.com",
	url="airtonix.net/projects/django-navigation-manager",
	description = "Django application that helps other applications declare navigation bar items.",
	license='LICENSE.md',
	packages=find_packages(exclude='tests'),
	include_package_data = True
)

