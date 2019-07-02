cli:
	@cd pardocs-malaya && hug -f main.py -c hello_world bob 10 
run:
	@cd pardocs-malaya && gunicorn main:__hug_wsgi__


