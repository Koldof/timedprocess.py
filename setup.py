from setuptools import setup

setup(
	name="timedprocess.py",
	version="1.1",
	description="Run a program for a specified duration",
	author = "Aaron Delaney",
	url = "https://github.com/koldof/timedprocess.py",
	author_email = "king.koldof@gmail.com",
	license = "GPLv3",
	py_modules=['timedprocess'],
	keywords="timed processes",
	install_requires = [
		'Click',
	],
	entry_points='''
		[console_scripts]
		timedprocess=timedprocess:cli
	''',
)
