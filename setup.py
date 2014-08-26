from setuptools import setup

setup(
    name = "SlackImageStorage",
    version = "0.2",
#    packages = find_packages(),

    author = "Michael Wang",
    author_email = "michaelwang2012@163.com",
    # and others; thank you all

    description = "slack image storage engine",
    long_description = """
 slack image storage engine
""".strip(),
    license = "MIT",
    keywords = "storage engine",
#    url = "http://eagain.net/software/fs/",
    url = "http://eagain.net/gitweb/?p=fs.git",

    classifiers = """\
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Programming Language :: Python
Topic :: Software Development :: Libraries
Topic :: System :: Filesystems
Development Status :: 3 - Alpha
""".splitlines(),
# TODO Development Status :: 4 - Beta
# TODO Development Status :: 5 - Production/Stable

)
