# Lab 08

In this lab we will use the private repo in Azure which now holds our image and deploy it using Kubernetes. 

## Step 1 

Create a new instance of Azure Kubernetes Service (AKS). 

```
az aks create --resource-group M3ModelManagement --name M3ModelManagement --node-count 1 --generate-ssh-keys
```

Right this is going to take a few minutes. Ask me some questions, take a comfort break, check some emails....

You could play this game to kill some time. http://guessthecorrelation.com/

Its taking a while eh?!? I bet you can hardly *contain* your excitement.... **tumbleweed.gif**

So in the background what this is doing is building all the infrastructure required to deploy any container to Kubernetes. The old version of AKS ACS used to show you all the stuff it made. It was really confusing. Now we just see one little resource. Much better. 

Ok, that has finished creating. 


## Step 2

If you followed the inctructions which were emailed out, you installed the wrong commandline. You needed AKS... Sorry about that. Let's fix that.

```
az aks install-cli
```

## Step 3


```
az aks get-credentials --resource-group M3ModelManagement --name M3ModelManagement
```