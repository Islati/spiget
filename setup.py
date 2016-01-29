from setuptools import setup

# from pip.req import parse_requirements

# reqs = parse_requirements('requirements.txt', session=False)
# reqs = [str(ir.req) for ir in reqs]
#

def main():
    setup(
        name='spiget',
        version='0.1.0',
        packages=[
            'spiget'
        ],
        url='https://github.com/TechnicalBro/spiget',
        license='',
        author='Brandon Curtis',
        author_email='freebird.brandon@gmail.com',
        description='Spiget.org API Interaction',
        download_url='https://github.com/TechnicalBro/spiget/tarball/0.1.0',
        keywords=['spigotmc', 'spiget', 'minecraft', 'bukkit'],
        install_requires=[
            "requests==2.9.1"
        ]
    )


if __name__ == "__main__":
    main()
