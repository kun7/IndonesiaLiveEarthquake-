"""
https://packaging.python.org/tutorials/packaging-projects/
"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="newestupdateearthquake-Indonesia",
    version="0.0.4",
    author="Kun Lanang",
    author_email="lanang7104@gmail.com",
    description="This package will get the latest update from indonesia earthquake monitoring agency BMKG",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kun7/IndonesiaLiveEarthquake-.git",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta"
    ],
    #package_dir={"": "src"},
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)