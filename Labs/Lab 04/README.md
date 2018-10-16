# Lab 04 - Hello World! in Docker

Welcome to lab 4. In this lab we are keeping things simple and just executing a super basic image. 

In this lab we will do a few things. 

1. We will pull an image from the cloud to our local machines
2. We will build that image on our Docker instance
3. We will run the instance and see what it does 
4. we will check the image is there
5. we will remove the image from our local Docker instance. 

## Details.

For this lab we will be executing the Hello World application example from docker. 

### Step 1 

Open the IDE you're using for Docker. This could be the commandline of your choice. CMD on windows, terminal on Linux. You could use PowerShell or VSCode. The choice is yours. 

Once you have you IDE open run the following:

```
docker ps
```

Docker ps will return all the running instances of images on your local machine. 

At this time there should be nothing running locally. We are just running this to check that Docker is running on your local machine. If Docker is not running make sure the service is running. If you have no luck, let me know and we will work through it. 

### Step 2

We are now going to pull an image from Docker Hub. 

Execute the following command to pull an image from Docker Hub. 

```
docker pull hello-world
```

This should start pulling all the layers of the image to your local machine. 

### Step 3

Let's run the image

```
docker run hello-world 
```

"Hello from Docker!" if all worked then this is what you should have seen. Isn't Docker nice! 

### Step 4

Now we have pulled the image you can try to pull the image again and you will see that it recognises that there is no difference and just does nothing. 

```
docker pull hello-world
```

The image is up-to-date

### Step 5 

Now we don't want that image any more. Let's remove it. 

First we will check the image is there. 
```
docker images 
```

Then we will remove it. 

```
docker rmi hello-world -f
```

The -f is force. This will tell Docker to just cut the ties and remove it. 

Run the followeing to confirm it has been removed. 
```
docker images 
```

Lab complete. 


