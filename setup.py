#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.

import runpy

from setuptools import find_packages, setup


version = runpy.run_path("iopath/version.py")["__version__"]

setup(
    name="iopath",
    version=version,
    author="FAIR",
    license="MIT licensed, as found in the LICENSE file",
    url="https://github.com/facebookresearch/iopath",
    description="A library for providing I/O abstraction.",
    python_requires=">=3.6",
    install_requires=[
        "boto3",
        "tqdm",
        "portalocker",
        "dataclasses; python_version<'3.7'",
    ],
    packages=find_packages(exclude=("tests",)),
)
