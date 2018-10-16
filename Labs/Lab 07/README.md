# Lab 07

In this lab we will create a private repo in Azure and deploy our image to it. 

To do this we will be using the Azure CLI. Hopefully that is installed on your laptops. 

We will start by building the resource group and then deploy a new container registry. 

## Step 1 

Connect to Azure via the Azure CLI 

Open a command prompt and type =:

```
az login
```

This will prompt you to go to https://microsoft.com/devicelogin and enter the device id you have been given. 

Your session will be locked while you're logged in. 

Select the appropiate subscription. 

```
az account set -s "599eb5a3-0fc5-4e18-a220-39ebaa74f940"
```
Replace that number with the subscription id of your Azure. 

## Step 2 

Create a new resource group 

```
az group create -l northeurope -n M3ModelManagement
```

You can check that this has been created by logging in to the Azure Portal. 

## Step 3

Create an instance of ACR inside your new resource group. 

```
az acr create --resource-group M3ModelManagement --name M3ModelManagementTerry --sku Basic
```

The name which you choose will need to be unique across all of Azure. So you cannot use the one that I have listed. Remove the Terry and replace with your own name. 

Again once that has completed you can check in Azure if it has been created. 

## Step 4 

Login to your new instance of ACR. This will authenticate that our connection is good and that we are allowed to deploy images. 

```
az acr login --name M3ModelManagementTerry
```

You should see the "Login Succeeded" 

## Step 5

We now need to get the full path to the ACR. We will need to deploy our models. 

```
az acr list --resource-group M3ModelManagement --query "[].{acrLoginServer:loginServer}" --output table
```

This will return something that looks like **m3modelmanagementterry.azurecr.io**

## Step 6

We now need to take our local docker image an deploy it. ACR can collect multiple version of the same image and source control them for you. Each new upload acts as a new version. We will first tag the image with the version is. This is V1 of our model so we will append v1 to the end. This is indicated by the :1. 

```
docker tag diabetesproduction m3modelmanagementterry.azurecr.io/diabetesproduction:v1
```

Now we need to push this model to ACR. 

```
docker push m3modelmanagementterry.azurecr.io/diabetesproduction:v1
```

Azure CLI should kick in and start pushing all the layers of your image in to Azure. Some parts are quite large so this may take a minute or so.

You can validate that it has been pushed by looking in Azure in ACR and selecting repositories. Or run the following: 

```
az acr repository list --name m3modelmanagementterry --output table
```



Once your image has been pushed, this lab is complete. 


