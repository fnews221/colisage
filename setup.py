from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in colisage/__init__.py
from colisage import __version__ as version

setup(
	name="colisage",
	version=version,
	description="Liste de Colisage",
	author="AT BA",
	author_email="info@gsent.fr",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
