clean:
	@echo Cleaning...
	@-rm -rf ./build

website:
	@mkdir -p ./build
	@mkdir -p ./build/css
	@mkdir -p ./build/gfx
	@mkdir -p ./build/manual
	python ./build.py
	cp assets/css/* build/css/
	cp assets/gfx/* build/gfx/
	cp -rv ../../Reticulum/docs/manual/* build/manual/
	cp -rv ../../Reticulum/docs/Reticulum\ Manual.pdf build/manual/

upload:
	. ./build.env; \
	rsync -rv build/ "$$DEPLOY_TARGET" --delete

pt:
	. ./build.env; \
	echo "$$DEPLOY_TARGET"

deploy: clean website upload
