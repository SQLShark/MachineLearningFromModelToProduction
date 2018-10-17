# Lab 06 - Deploying your model

The last lab was a bit of a tangent, but it was to show some of the quirks of working with Docker. 

Now that we have a good grasp on the basics, lets do the same for our model. 

## Step 1

In step 4 we wrapped our model up in a Flask script. Now we have an api we can ping our model and get a response. What we dont want to do now is have to run the model each time manually. Lets put it in a docker container. 

Have a go at doing what you think you need to based on the last lab. 

Remember the general steps are: 
1. Create a dockerfile 
2. Create the application code 
3. Create a requirements.txt file
4. Build the image
5. Check that the model is running

If you do get stuck there is another file here with the answers. [Clicky]()