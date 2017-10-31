# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    print("Setuptools is needed to install all dependencies")
    print("Setuptools: https://pypi.python.org/pypi/setuptools")

import platform

if not platform.system() == "Linux":
    print("Warning: UncertainPy not tested for current operating system")

name = "testme1"

uncertainpy_req = ["xvfbwrapper", "chaospy", "tqdm", "h5py",
                   "multiprocess", "numpy", "scipy", "seaborn"]

extras_require = {
    'spike_features':  ["efel"],
    'network_features': ["elephant", "neo", "quantities"],
}


anaconda_req = ["xvfbwrapper", "chaospy", "tqdm", "h5py",
                "multiprocess", "numpy", "scipy", "seaborn",
                "efel", "elephant",  "neo", "quantities"]

long_description = open("README.md").read()

packages = ['uncertainpy', 'uncertainpy.models', 'uncertainpy.features', 'uncertainpy.plotting', 'uncertainpy.utils']
setup(name=name,
      version="0.9.2",
    #   url="https://github.com/simetenn/uncertainpy",
    #   author="Simen Tennøe",
    #   description='Uncertainty quantification and sensitivity analysis',
    #   long_description=long_description,
      python_requires=">=2.7",
      packages=find_packages("src"),
      package_dir={"": "src"},
      data_files=["README.md"],
      install_requires=anaconda_req,
      extras_require=extras_require,
      )
