from setuptools import setup

requires = [
    'pyramid',
    'zope.sqlalchemy',
    'pyramid_tm',
    'waitress',
    'pytest',
    'webtest',
    'pytest-cov',
    'sqlalchemy'
]

setup(name='tutorial', 
    install_requires=requires,
    entry_points="""\
      [paste.app_factory]
      main = app:main
      """)
