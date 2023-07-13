from setuptools import setup  #, find_packages
from pathlib import Path
from re import search

base_path = Path(__file__).parent

repo_url = 'https://github.com/gitagogaming/AnimazePy'
home_url = repo_url
docs_url = 'https://github.com/gitagogaming/AnimazePy'
long_description = (base_path / "README.md").read_text("utf8")
api_version = search(
  r'__version__ = "(.+?)"', (base_path / "AnimazePy" / "__init__.py").read_text("utf8")
).group(1)

classifiers = [
  'Development Status :: 4 - Beta',
  'Intended Audience :: Developers',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
  'Programming Language :: Python :: 3'
]

setup(
  name = 'AnimazePy',
  version = api_version,
  description = 'A Python Wrapper for the Animaze API',
  long_description = long_description,
  long_description_content_type = "text/markdown",
  url = home_url,
  project_urls = {
    'Documentation': docs_url,
    'Source': repo_url,
    'Issues': repo_url + "issues",
  },
  author = 'Gitago',
  author_email=  'gitproductions.814@gmail.com',
  license = 'GPLv3+',
  classifiers = classifiers,
  keywords = 'Animaze, API, SDK',
  packages = ['AnimazePy'],
  python_requires = '>=3',
  install_requires = [
    'websockets'
  ]
)