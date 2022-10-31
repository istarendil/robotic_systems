from setuptools import setup

package_name = 'scara_pkg'

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
    maintainer='iztatik',
    maintainer_email='iztatik@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "tracer = scara_pkg.tracer:main",
            "solver = scara_pkg.solver:main",
            "simple_ui = scara_pkg.simple_ui:main"
        ],
    },
)
