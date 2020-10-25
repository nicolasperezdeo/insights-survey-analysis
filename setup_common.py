from setuptools import find_packages
import survey_analysis_tool


def define_args():
    install_requirements = ['setuptools>=40.3,<49.2', 'numpy>=1.16,<2.0', 'matplotlib>=3.0.1,<3.2.1', 'scikit-image']

    test_requirements = ['pytest>=4.3,<4.4', 'pytest-cov>=2.7,<2.8']
    args = {
        'name': 'Survey Analysis Tool',
        'version': survey_analysis_tool.__version__,
        'url': 'https://github.com/nicolasperezdeo/insights-survey-analysis/',
        'author': 'Nicolas Perez de Olaguer',
        'author_email': 'nicolasperezdeo@gmail.com',
        'classifiers': ['Development Status :: 3 - Alpha', 'Programming Language :: Python :: 3'],
        'packages':  find_packages(),
        'python_requires': '>=3.5',
        'entry_points': {'console_scripts': ['perform_analysis=survey_analysis_tool.bin.perform_analysis:main']},
        'install_requires': install_requirements,
        'extras_require': {'testing': test_requirements},
        'project_urls': {'Source':
                         'https://github.com/nicolasperezdeo/insights-survey-analysis/'}
    }
    return args
