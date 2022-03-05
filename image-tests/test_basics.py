import shutil

def test_psql():
	# Make sure the psql commandline tool is installed
	assert shutil.which('psql')
