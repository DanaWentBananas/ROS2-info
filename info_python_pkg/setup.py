from setuptools import setup

package_name = 'info_python_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='danana',
    maintainer_email='devbot333@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "number_counter_x.py=info_python_pkg.number_counter:main",
            "number_publisher_x.py=info_python_pkg.number_publisher:main",
            "hardware_status_msg_x.py=info_python_pkg.hardware_status_msg:main"
        ],
    },
)
