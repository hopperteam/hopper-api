publish: hopper_api/*
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload --repository pypi dist/*

clean:
	rm -rf dist hopper_api.egg-info hopper_api.egg-info build