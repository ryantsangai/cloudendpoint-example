PROJECT_NAME = "cloudendpoints-demo"

# first time install
init:
	source `which virtualenvwrapper.sh`; \
	mkvirtualenv $(PROJECT_NAME); \
	workon $(PROJECT_NAME); \
	ln -s ~/.virtualenvs/$(PROJECT_NAME)/lib/python2.7/site-packages lib; \
	pip install -r requirements.txt;

# update packages
install:
	source `which virtualenvwrapper.sh`; \
	workon $(PROJECT_NAME); \
	pip install -r requirements.txt;

start:
	source `which virtualenvwrapper.sh`; \
	workon $(PROJECT_NAME); \
	dev_appserver.py . --log_level debug;
