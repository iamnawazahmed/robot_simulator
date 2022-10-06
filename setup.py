from setuptools import setup
import os
from glob import glob

package_name = 'robot_simulator'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        
        (os.path.join('share',package_name,'launch'),glob('launch/*')),
        (os.path.join('share',package_name,'worlds'),glob('worlds/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Mohammed Nawaz Shaikh',
    maintainer_email='iamnawazahmed@gmail.com',
    description='The differential drive robot simulation package',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'driving_node=robot_simulator.driving_node:main',
        'teleop_twist_keyboard=robot_simulator.teleop_twist_keyboard:main'
        ],
    },
)
