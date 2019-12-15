from setuptools import setup, find_packages

setup(name='bokehBorn',
      version='0.0.1',
      description="bokehBorn",
      author='Golam Mostaeen',
      author_email='golammostaeen@gmail.com',
      license='',
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
        'pandas',
        'bokeh==1.4.0',
        'numpy',
        'seaborn']
      )
