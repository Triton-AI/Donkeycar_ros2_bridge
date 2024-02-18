from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'Donkeycar_ros2_bridge'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),\
        (os.path.join('share', package_name,'include'), glob('Donkeycar_ros2_bridge/*config.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='moises',
    maintainer_email='mdlopezme@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'manage.py = Donkeycar_ros2_bridge.manage:main'
        ],
    },
)
