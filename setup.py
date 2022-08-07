"""Install the package."""

from setuptools import setup
from mypythontools_cicd import packages

if __name__ == "__main__":
    extras_requirements = {
        i: packages.get_requirements(f"requirements/extras_{i}.txt", path="requirements") for i in ["data"]
    }

    setup(
        **packages.get_package_setup_args("pyvueeel", development_status="alpha"),
        **packages.personal_setup_args_preset,
        description="Micro framework for python / vue / js applications",
        long_description=packages.get_readme(),
        install_requires=packages.get_requirements("requirements/requirements.txt"),
        extras_require=extras_requirements,
    )
