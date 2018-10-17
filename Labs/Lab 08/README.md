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

If you followed the instructions which were emailed out, you installed the wrong commandline. You needed AKS... Sorry about that. Let's fix that.

```
az aks install-cli
```

## Step 3
We need to authenticate of Azure CLI with the new AKS service. 

```
az aks get-credentials --resource-group M3ModelManagement --name M3ModelManagement
```


## Step 4
Let's take a look at what is running on our Kuberentes cluster. If you run the following you will see a list of all the nodes. Kubectl has numerous pronounceations. My preference is Kube-cuttle or Kube-cee-tee-ell

```
kubectl get nodes
```

This will show the one and only node we created. If we had scaled this deployment to multiples we would see that here. A node can contain multiple pods. What we are deploying is pods. We can run loads of pods on the same node, but they will share resources. 

## Step 5

We need to write some YAML. YAML is the slimmer version of Json (which is the slimmer version of XML). 

YAML is what Kubernetes need to read inorder to work out what needs to go in each POD. 

Create a new folder called "Kubernetes" and in that folder create a new file called diabetesproduction.yml

Add the following 
```
apiVersion: apps/v1beta1
kind: Deployment
metadata:
  name: productiondiabetes
spec:
  replicas: 1
  template:
    metadata:
      labels:
        app: productiondiabetes
    spec:
      containers:
      - name: productiondiabetes
        image: <your version>.azurecr.io/productiondiabetes:v1
        ports:
        - containerPort: 5071
          name: dockerport
---
apiVersion: v1
kind: Service
metadata:
  name: productiondiabetes
spec:
  type: LoadBalancer
  ports:
  - port: 80
    targetPort: dockerport
    protocol: TCP
  selector:
    app: productiondiabetes

```

Save your changes and close the file. 

## Step 6

Use the Kubectl command apply to install our container. 

```
kubectl apply -f G:\GitHubProjects\workshop-ModelManagement\MachineLearningFromModelToProduction\Kubernetes\productiondiabetes.yml
```
2 things should have been created. A deployment and a service

Lets see if that has built yet. 

```
kubectl get service productiondiabetes 
```

If this returns you an IP address then there is a good chance it has worked. To make sure we can look at the Kube dashboard. 

## Step 7 

Check the dashboard. Run the following 

```
az aks browse --resource-group M3ModelManagement --name M3ModelManagement
```

Now there is currently a bug connecting ACR and AKS. It is to do with the Service Pricipal which is created. We can resolve this by doing the following. 

Run the following and copy the result. 
```
az aks show --resource-group M3ModelManagement --name M3ModelManagement --query "servicePrincipalProfile.clientId" --output table
```
**c0f34e8c-3699-4759-b564-ec5c2e8949e7**

Run the following and copy the result
```
az acr show --name M3ModelManagementTerry --resource-group M3ModelManagement --query "id" --output table
```

**/subscriptions/599eb5a3-0fc5-4e18-a220-39ebaa74f940/resourceGroups/M3ModelManagement/providers/Microsoft.ContainerRegistry/registries/M3ModelManagementTerry**

Combine the two as follows and execute. 
```
az role assignment create --assignee c0f34e8c-3699-4759-b564-ec5c2e8949e7 --role Reader --scope /subscriptions/599eb5a3-0fc5-4e18-a220-39ebaa74f940/resourceGroups/M3ModelManagement/providers/Microsoft.ContainerRegistry/registries/M3ModelManagementTerry
```

Ok that should have resolved the security problem. 

Let's remove the old deployment and go again. 

```
kubectl delete -f G:\GitHubProjects\workshop-ModelManagement\MachineLearningFromModelToProduction\Kubernetes\productiondiabetes.yml
```
 Then apply 
 ```
 kubectl apply -f G:\GitHubProjects\workshop-ModelManagement\MachineLearningFromModelToProduction\Kubernetes\productiondiabetes.yml
 ```

 Open a new command prompt and run the following again: 

 ```
az aks browse --resource-group M3ModelManagement --name M3ModelManagement
 ```

 You will now see that there are no errors. 

 ## Step 8 lets test our model.

Run the following 
```
kubectl get services
```

Copy the IP address from the load balancer. Make sure you copy the external ip address. 

```
http://40.113.78.55/train
http://40.113.78.55/score?var1=1
```
Lab complete. You have now created a model and deployed it to a container running on Kubernetes. 

IF YOU HAVE 14 ERRORS run this: 

```
kubectl create clusterrolebinding kubernetes-dashboard -n kube-system --clusterrole=cluster-admin --serviceaccount=kube-system:kubernetes-dashboard
```