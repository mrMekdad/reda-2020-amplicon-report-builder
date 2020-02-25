from setuptools import setup

setup(
    name="reda-2020-amplicon-report-builder",
    version="0.1.0",
    description="Report generator for amplicon runs with per-sample status tables and markdown output.",
    author="Red@",
    packages=["amplicon_report_builder"],
    package_dir={"": "src"},
)
