help:
	@echo "Run make build to compile into 'build/sales_grid' folder."
	@echo "Run make start to execute the dialog script locally"


.PHONY: build help, msg-short, msg-long, msg-warn, msg-error, msg-yes

build:
	oooscript compile --embed --config "$(PWD)/config.json" --embed-doc "$(PWD)/data/src_doc/src_doc.ods" --build-dir "$(PWD)/data"
	rm -f "$(PWD)/data/odev_cell_controls.py"

start:
	python $(PWD)/start.py
