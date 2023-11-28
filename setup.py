from setuptools import setup, find_packages

setup(
    name="orm_melisa",
    version='v1.0.10',
    author="Steven Sotelo",
    author_email="h.sotelo@cgiar.com",
    description="ORM for Melisa",
    url="https://github.com/CIAT-DAPA/melisa_orm",
    download_url="https://github.com/CIAT-DAPA/melisa_orm",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    keywords='mongodb orm melisa',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "mongoengine==0.27.0",
        "dnspython==2.4.2",
        "pymongo==4.6.0"
    ]
)