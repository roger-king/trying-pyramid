from setuptools import setup

setup_requires = [
    'pytest-runner'
]

install_requires = [
    'pyramid',
    'zope.sqlalchemy',
    'pyramid_tm',
    'waitress',
    'sqlalchemy',
    'pyramid_debugtoolbar'
]

tests_require = [
    'pytest',
    'webtest',
    'pytest-cov'
]

setup(name='trying-pyramid', 
    setup_requires=setup_requires,
    install_requires=install_requires,
    tests_require=tests_require,
    entry_points="""\
      [paste.app_factory]
      main = app.main:main
      """)
