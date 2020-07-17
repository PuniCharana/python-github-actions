from app import index, version

def test_index():
	assert index() == "Hello World!"

def test_version():
	assert version() == "0.0.1"
