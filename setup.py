from distutils.core import setup

from pip.req import parse_requirements


def main():
    setup(
        name='spiget',
        version='0.0.1',
        packages=[
            'spiget'
        ],
        url='',
        license='',
        author='Brandon Curtis',
        author_email='bcurtis@artectis.com',
        description='Spiget.org API Interaction',
        install_requirements=reqs
    )


if __name__ == "__main__":
    reqs = parse_requirements('requirements.txt')
    reqs = [ir for ir in reqs]

    main()
