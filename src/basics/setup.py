from setuptools import setup
import os
from glob import glob

package_name = 'basics'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='istarendil',
    maintainer_email='istarendiln@todo.todo',
    description='Basic package for learning',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'node = basics.01_node:main',
            'publisher = basics.02_publisher:main',
            'subscriber = basics.03_subscriber:main',
            'server = basics.04_server:main',
            'client = basics.05_client:main',
            'parameters = basics.06_parameters:main',
            'action_server = basics.07_action_server:main',
            'action_client = basics.08_action_client:main',
        ],
    },
)
