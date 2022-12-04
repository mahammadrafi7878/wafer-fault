from setuptools import find_packages,setup


REQUIREMENT_FILES='requirements.txt'
HYPHEN="-e ."



def get_requirements():
    with open (REQUIREMENT_FILES) as requirement_file:
        requirement_list=requirement_file.readlines()
    requirement_list=[requirement_name.replace("/n", "") for requirement_name in requirement_list]
    if HYPHEN in requirement_list:
        requirement_list.remove(HYPHEN)
    return requirement_list

setup(
    name="sensor",
    version="0.0.1",
    author="mahammad rafi",
    author_email="mahammadrafishaik222@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),

)