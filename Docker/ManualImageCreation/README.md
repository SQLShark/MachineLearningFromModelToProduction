# Commands requied to get this all working. 
This is here both as an instruction and also a means for me to remember how to process a model. 

So to run a model inside a container you need to first navigate to the location of the Dockerfile. 

```
cd "G:\GitHubProjects\session-DataScienceDevops\Docker\DiabetesProductionDocker"
```

Then we need to build the model 
```
docker build -t diabetes .
``` 

Lets check that the image has been created as intended. 

```
docker images
```

Lets run the model using our local version of Docker
```
docker run -d --name diabetes -p 5071:5071 diabetes
```

We can also stop our model with 
```
docker stop diabetes
```

The important part of that last call is the -p parameter. That is forwarding the port from the docker image to my machine. Now all of these steps have been completed, we can open our web browser and train then score our model.

1. http://localhost:5071/train?var1=0
2. http://localhost:5071/score?var1=10

To stop running our model we need to find the name of the instance running.

```
docker ps
```

Now that we have an image that works, we need to deploy that image to our registry. To do this we will need to switch to the Azure CLI.

```
az login
https://microsoft.com/devicelogin
<Get the code>

az acr login --name devopsml


az acr list --resource-group session-datasciencedevops --query "[].{acrLoginServer:loginServer}" --output table


docker tag diabetes devopsml.azurecr.io/diabetes:v1

docker push devopsml.azurecr.io/diabetes:v1
```

Lets check that image was uploaded. 

```
az acr repository list --name devopsml --output table
```

Log in to the Kubernetes cluster
```
az aks get-credentials --resource-group session-datasciencedevops  --name devopsml

kubectl get nodes
```

```
kubectl apply -f azure-vote-all-in-one-redis.yaml
```

Change the directory
```
G:
cd G:\GitHubProjects\session-DataScienceDevops\Kubernetes
```

```
kubectl apply -f productiondiabetes.yaml
```

Now we need to check if the service is running. It will be marked as pending until it has completed. 
```
kubectl get services
```

Lets also deploy the dashboard
```
az aks browse --resource-group session-datasciencedevops  --name devopsml
```

If there were any problems then this will show them. 

az acr repository list --name devopsml --output table

```
az aks show --resource-group session-datasciencedevops --name devopsml --query "servicePrincipalProfile.clientId" --output table

8edd6a3b-1f96-42af-8985-8f4d824ffc59

az acr show --name devopsml --resource-group session-datasciencedevops --query "id" --output table

/subscriptions/599eb5a3-0fc5-4e18-a220-39ebaa74f940/resourceGroups/session-datasciencedevops/providers/Microsoft.ContainerRegistry/registries/devopsml

az role assignment create --assignee 8edd6a3b-1f96-42af-8985-8f4d824ffc59 --role Reader --scope /subscriptions/599eb5a3-0fc5-4e18-a220-39ebaa74f940/resourceGroups/session-datasciencedevops/providers/Microsoft.ContainerRegistry/registries/devopsml
```
Good blog for when thing dont go quite right: 
https://docs.microsoft.com/en-us/azure/container-registry/container-registry-auth-aks
