import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="udica",
    version="0.0.1",
    author="Lukas Vrabec",
    author_email="lvrabec@redhat.com",
    description="A tool for generating SELinux security policies for containers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.cee.redhat.com/lvrabec/udica",
    packages=["udica"],
    # scripts=["bin/udica"],
    entry_points = {
        'console_scripts': ['udica=udica:main'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
)
