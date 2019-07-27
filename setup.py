from distutils.core import setup
from setuptools import find_packages

setup(
    name='InstaBoost',
    version='0.1',
    description='a python implementation for paper: "InstaBoost: Boosting Instance Segmentation Via Probability Map GuidedCopy-Pasting"',
    author='Haoshu Fang, Jianhua Sun, Runzhong Wang,  Minghao Gou, Yonglu Li, Cewu Lu',
    author_email='1751196720@qq.com',
    url='https://github.com/GothicAi/InstaBoost-pypi',
    packages=find_packages(),
    install_requires=[
      'numpy',
      'opencv-python',
      'scipy',
      'pycocotools',
      'matplotlib',
      'Pillow',
      'scikit-image'
    ]
)
