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
	cp -r ../../Reticulum/docs/manual/* build/manual/
	cp -r ../../Reticulum/docs/Reticulum\ Manual.pdf build/manual/
	cp -r ../../Reticulum/docs/Reticulum\ Manual.epub build/manual/

docsfolder:
	@mkdir -p ./docs
	cp -rv ./build/* ./docs/
	touch ./docs/.nojekyll

github:	website docsfolder

upload:
	. ./build.env; \
	rsync -rv -e "ssh -p $${DEPLOY_PORT}" build/ $${DEPLOY_TARGET} --delete;

deploy: clean website upload
