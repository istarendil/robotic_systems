from setuptools import setup
from glob import glob
import os

package_name = 'scara'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('urdf/*.urdf.xml')),
        (os.path.join('share', package_name, 'meshes', 'visual'), glob('meshes/visual/*')),
        (os.path.join('share', package_name, 'meshes', 'collision'), glob('meshes/collision/*')),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='istarendil',
    maintainer_email='alberto.iztatik@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'trajectory_generator = scara.trajectory_generator:main',
            'scara_joint_publisher = scara.scara_joint_publisher:main',
            'virtual_pendant = scara.virtual_pendant:main',
        ],
    },
)
