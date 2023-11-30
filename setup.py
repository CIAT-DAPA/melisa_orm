from setuptools import setup, find_packages

setup(
    name="melisa_orm",
    version='v1.0.2',
    author="stevensotelo",
    author_email="h.sotelo@cgiar.com",
    description="orm for mellisa",
    url="https://github.com/CIAT-DAPA/melisa_orm",
    download_url="https://github.com/CIAT-DAPA/melisa_orm",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    keywords='mongodb orm melissa',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "mongoengine==0.26.0"
    ]
)
