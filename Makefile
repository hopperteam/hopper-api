all: python

python: python/*
	$(MAKE) -C python

clean:
	$(MAKE) -C python clean

.PHONY: all python clean