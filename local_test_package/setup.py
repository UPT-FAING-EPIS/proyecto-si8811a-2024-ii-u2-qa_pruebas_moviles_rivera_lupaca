from setuptools import setup, find_packages

setup(
    name="local-tests-package",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pytest",
        "Appium-Python-Client",
    ],
    description="Paquete para pruebas locales en Android con Appium y Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
)
