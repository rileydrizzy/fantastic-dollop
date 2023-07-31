"""doc
"""

import setuptools

with open("README.md", "r", encoding= "utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

repo_name = ""
Author_user_name = "Ipadeola Ladipo Ezekiel"
src_repo = ""
Author_Email = "ipadeolaoladipo@outlook.com"
project_url = ""

setuptools.setup(
    name= src_repo,
    version= __version__,
    license= "",
    author= Author_user_name,
    description= "",
    long_description= long_description,
    long_description_content = "text/markdown",
    url= project_url,
    keywords= [],
    package_dir= {"" : "src"},
    packages= setuptools.find_packages(where= "src")
)
