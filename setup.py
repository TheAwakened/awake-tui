from setuptools import setup
from awake import constants

setup(
	name = 'awake-tui',
	packages = ['awake'],
	python_requires='>=3',
	version = constants.VERSION,
	description = 'Awake with text-based user interface (TUI)',
	author = 'Marcus Mu',
	author_email = 'chunkhang@gmail.com',
	license = 'UNLICENSE',
	url = 'https://github.com/TheAwakened/awake-tui',
	keywords = [
		'awake',
		'tui',
		'console',
		'terminal',
		'curses'
	], 
	classifiers = [
		'Intended Audience :: End Users/Desktop',
		'Environment :: Console',
		'Programming Language :: Python :: 3 :: Only'
	],
	entry_points = {
		'console_scripts': [
			'awake=awake.awake:main'
		]
	}	
)