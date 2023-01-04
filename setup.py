from distutils.core import setup

setup(name='pke',
      version='1.8.1',
      description='Python Keyphrase Extraction module',
      author='pke contributors',
      author_email='florian.boudin@univ-nantes.fr',
      license='gnu',
      packages=['pke', 'pke.unsupervised', 'pke.supervised',
                'pke.supervised.feature_based', 'pke.unsupervised.graph_based',
                'pke.unsupervised.statistical', 'pke.supervised.neural_based'],
      url="https://github.com/boudinfl/pke",
      install_requires=[
            "six==1.14.0",
            "spacy==2.2.4",
            "nltk==3.4",
            "networkx==2.4",
            "numpy==1.19.2",
            "scipy==1.4.1",
            "scikit-learn==0.23.1",
            "unidecode==1.3.4",
            "future==0.18.2",
            "joblib==0.14.1"
      ],
      package_data={'pke': ['models/*.pickle', 'models/*.gz']}
      )
