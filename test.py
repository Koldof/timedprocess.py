import unittest
import timedprocess

import click
from click.testing import CliRunner

class TestProcessTiming():
	def test_invalid_process(self):
		expected_return_value = -1
		arguments = [10, 'invalidpath.exe']
		
		runner = CliRunner()
		result = runner.invoke(timedprocess.cli, arguments)
		
		assert result.exit_code == expected_return_value
		
	def test_valid_process(self):
		expected_return_value = 0
		arguments = [10, "C:\Windows\System32\eventvwr.exe"]
		
		runner = CliRunner()
		result = runner.invoke(timedprocess.cli, arguments)
		print result.output
		
		assert result.exit_code == expected_return_value

if __name__ == '__main__':
	testclass = TestProcessTiming()
	testclass.test_invalid_process()
	testclass.test_valid_process()
	
	print 'Sucess!'