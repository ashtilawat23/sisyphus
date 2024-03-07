from setuptools import setup, find_packages

setup(
    name='sisyphus',
    version='0.1.0',
    author='Ashalesh Tilawat',
    author_email='ashtilawat23@example.com',
    description='A Python package for building Narrow Task AI Agents with built-in reliability checks.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ashtilawat23/sisyphus',
    packages=find_packages(),
    install_requires=[
        'langchain>=0.1.0',  # Assuming you're using LangChain; specify the version you're compatible with
        'numpy>=1.18.5',  # Common dependency for numerical operations
        'pandas>=1.0.5',  # Useful for data manipulation and analysis
        'torch>=1.5.0',  # PyTorch, in case you're working with neural networks
        'transformers>=4.0.0',  # Hugging Face's Transformers, for state-of-the-art NLP models
        # Add any other dependencies your package might need
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'sisyphus=sisyphus.cli:main',  # Placeholder for a command-line interface, if applicable
        ],
    },
)