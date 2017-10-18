from setuptools import setup

setup_requires = [
    'pyramid',
    'zope.sqlalchemy',
    'pyramid_tm',
    'waitress',
    'sqlalchemy',
    'pyramid_debugtoolbar'
]

test_require = [
    'pytest',
    'webtest',
    'pytest-cov'
]

setup(name='trying-pyramid', 
    setup_requires=setup_requires,
    test_require=test_require,
    entry_points="""\
      [paste.app_factory]
      main = app.main:main
      """)
