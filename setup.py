from setuptools import setup, find_packages

setup(
    name='mmm',
    version='0.1',
    packages=find_packages(),  # Bu satır önemli
    install_requires=[
        'click',
        'requests',
        'colorama'
    ],
    entry_points={
        'console_scripts': [
            'mmm=mmm.cli:cli',  # CLI uygulamanın giriş noktası
        ],
    },
)