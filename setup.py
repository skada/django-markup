from setuptools import setup, find_packages
import djangomarkup

setup(
    name = 'djangomarkup',
    version = djangomarkup.__versionstr__,
    description = 'Support for various markup languages in Django applications',
    long_description = '\n'.join((
        '(TODO)',
    )),
    author = 'centrum holdings s.r.o',
    license = 'BSD',

    packages = find_packages(
        where = '.',
        exclude = ('docs', 'tests')
    ),

    entry_points = {
        'setuptools.file_finders': ['dummy = setuptools_entry:dummylsfiles'],
    },

    include_package_data = True,

)

