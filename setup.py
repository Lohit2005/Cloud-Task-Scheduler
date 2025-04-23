from setuptools import setup, find_packages

setup(
    name="cloud_scheduler",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy>=1.21",
        "matplotlib>=3.5"
    ],
)
