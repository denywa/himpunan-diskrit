from setuptools import setup, find_packages

setup(
    name="himpunan_tim5",  
    version="1.0.0",  
    author="Deny Wahyudi Asaloei",
    author_email="dwa1503@gmail.com",
    description="Library Python untuk implementasi teori himpunan",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/denywa/himpunan-library",
    packages=find_packages(),
    python_requires=">=3.6",
)
