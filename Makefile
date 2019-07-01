help: ##
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

build: ##               Builds BPA inference image and solution according to the versions found the fig file
	$(info ----------------------------------------------------------------------------------------------------------------------)
	$(info ******************** Building bpa_inference solution  $(SOLUTION_VERSION) )
	$(info ********************   with inference image  $(INFERENCE_VERSION) )
	$(info ----------------------------------------------------------------------------------------------------------------------)
	@cd $(BASE_PATH_DOCKER); \
	./zip_app.sh $(INFERENCE_VERSION); \
	./build.sh $(INFERENCE_VERSION); \
	cd solution; \
	./build.sh $(SOLUTION_VERSION); \
	cd ../../; \
	echo "$(SOLUTION_VERSION) $(INFERENCE_VERSION)" > build_versions

push: ##                Pushes to artifactory the image and solution versions found in fig file
	$(info ----------------------------------------------------------------------------------------------------------------------)
	$(info ******************** Pushing BPA inference solution  $(SOLUTION_VERSION) )
	$(info ********************     and BPA inference image  $(INFERENCE_VERSION) )
	$(info ********************        artifact name  $(SOLUTION_REPOSITORY)/$(INFERENCE_TAG) )
	$(info ----------------------------------------------------------------------------------------------------------------------)
	@docker push $(SOLUTION_REPOSITORY)/$(INFERENCE_TAG)
	@docker push $(SOLUTION_REPOSITORY)/$(SOLUTION_TAG)
