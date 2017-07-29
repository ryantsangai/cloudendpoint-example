This example demonstrate how to develop a Google Cloud Endpoint service from scratch.
I try my best to keep the commits clean and easy to read. So if you want to learn step by step, you may read from first commit

Concept you should know:
1. Google Cloud Endpoint can be used in App Engine flexible environment, App Engine standard environment, Compute Engine and Container Engine.
2. This example only demonstrate GAE Standard Environment for Python
3. To implement GAE Standard Environment, you need to use [protorpc](https://cloud.google.com/appengine/docs/standard/python/tools/protorpc/)
4. Cloud Endpoints supports OpenApi Spec(also known as Swagger Spec) and gRPC, GAE Standard Environment only support OpenApi
5. You can use (Api Explorer)[https://developers.google.com/apis-explorer] to test your api, by the path **/_ah/api/explorer**

# Deployment
[Official Deployment Doc](https://cloud.google.com/endpoints/docs/frameworks/python/test-deploy#generating_and_deploying_an_api_configuration_file)
For TLDR
1. First you need to generate the spec by endpoints command to json
2. Deploy the json spec to service-management
3. Configure app.yaml with **ENDPOINTS_SERVICE_VERSION** and **ENDPOINTS_SERVICE_NAME**
4. Deploy the app


# Reference
[Google Cloud Endpoint Doc](https://cloud.google.com/endpoints/docs/)