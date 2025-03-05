from setuptools import setup, find_packages

setup(
    name='wikipedia-traffic-analysis',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'dask',
        'matplotlib',
        'sqlite3',
        'glob2',
        'gzip',
        'pytest'
    ],
    entry_points={
        'console_scripts': [
            'process-wikipedia=scripts.data_processing:process_wikipedia_data',
            'query-database=scripts.database_manager:query_data',
            'plot-traffic=scripts.visualization:plot_time_series'
        ]
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A project to analyze Wikipedia traffic using Dask & SQLite',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/your-username/wikipedia-traffic-analysis',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
