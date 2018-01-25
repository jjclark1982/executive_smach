#!/usr/bin/env python

from distutils.core import setup

setup(
    author='Jonathan Bohren',
    description='SMACH is a task-level architecture for rapidly creating complex robot\n    behavior. At its core, SMACH is a ROS-independent Python library to build\n    hierarchical state machines. SMACH is a new l...',
    license='BSD',
    long_description='SMACH is a task-level architecture for rapidly creating complex robot\n    behavior. At its core, SMACH is a ROS-independent Python library to build\n    hierarchical state machines. SMACH is a new library that takes advantage of\n    very old concepts in order to quickly create robust robot behavior with\n    maintainable and modular code.',
    maintainer='Isaac I. Y. Saito',
    maintainer_email='gm130s@gmail.com',
    name='smach',
    packages=['smach'],
    package_dir={'smach': 'src/smach'}, 
    version='2.0.1'
)
