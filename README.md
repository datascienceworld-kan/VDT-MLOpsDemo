## Mlops: A primer on creating robust model training pipelines

This repository contains code demos and videos for my youtube video series [here](https://www.youtube.com/watch?v=fM_4jWS0w00&list=PLH4UpMDxt47lN-vfaNtLrR0Kt3gK48QB5&index=1) on mlops. You can use this repo to follow along the video series. 

## Introduction:

It's not sufficient these days that you as a data professional are able to train models. It's also becoming increasingly important to be able to deploy these models in production and take care of the entire life cycle of an ML project. In this short module we will go through the basic guiding principles that one needs to adhere to while creating machine learning systems in production

After you complete the video series, you will be able to:

1. Clearly articulate what Mlops is and why is it needed.
2. Convert ml code in jupyter notebook into training pipeline components.
3. Use good code practices to create python scripts that can be used to implement training pipeline components.
4. Decouple the components from data-sources, model hyperparameters using config management tool such as hydra.
5. Orchestrate a training pipeline.
6. Log model artefacts and training metrics.

### Part 1: What is mlops anyways?

Let’s explore what mlops is and what are the common tools one would need to use.

[![Video 1](https://i9.ytimg.com/vi/fM_4jWS0w00/mq1.jpg?sqp=COSF9KgG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgZShlMA8=&rs=AOn4CLAP5Vz7iO-ge6DUgSUOaq1bLExR-w)](https://youtu.be/fM_4jWS0w00)

Now that we know what mlops is and the popular tools used, lets now see what the common issues with a traditional data science model training workflow are and how those issues can be fixed.   

[![Video 2](https://i9.ytimg.com/vi/5tXn2xYyX3w/mq1.jpg?sqp=COSF9KgG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgZShlMA8=&rs=AOn4CLAJz25w_Yb6vI8E7bFDgrN7PQNcHw)](https://youtu.be/5tXn2xYyX3w)

### Part2: Building training pipelines

**Note: All the codes used in part 2 videos are [here](./part2/)**

In the previous few videos, we saw what mlops is and how a traditional data science workflow is not effective. In this section we will see how to create a model training pipeline.

Let’s first look at how to create a data ingestion pipeline. We will assume that our data is on a data lake and we need to decouple the ingestion code from the location of the data

[![Video 3](https://i9.ytimg.com/vi/VfEceK2AbeY/mq1.jpg?sqp=CJCI9KgG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgZShlMA8=&rs=AOn4CLBVz1quebttUIod0ySXTjixIMZWtA)](https://youtu.be/VfEceK2AbeY)

The next part is to build a feature engineering pipeline. Let’s look at the next video and see what principles can be followed to create a feature engineering pipeline. 

[![Video 4](https://i9.ytimg.com/vi/xDoiWSHs7Y8/mq1.jpg?sqp=CLyK9KgG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgZShlMA8=&rs=AOn4CLC7CJVF33jgMlkqoEs5gaRbTchAVA)](https://www.youtube.com/watch?v=xDoiWSHs7Y8 "Video 4")

Finally let’s see how to create a model training pipeline.

[![Video 5](https://i9.ytimg.com/vi/zffaeWPl_bc/mq1.jpg?sqp=CLyK9KgG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgZShlMA8=&rs=AOn4CLDoO_RoVHpdULNI5ECUzpTBltV1Zg)](https://youtu.be/zffaeWPl_bc)



### Part 3: Orchestrating ml pipelines using mlflow

**Note: All the codes used in part3 are [here](./part3/)**

So far we’ve created individual components of a training pipeline. Let’s now see how we can run all these components together using mlfow acting as an orchestrator. So far we’ve created individual components of a training pipeline. Let’s now see how we can run all these components together using mlfow acting as an orchestrator. 

[![Video 6](https://i9.ytimg.com/vi/twgblvN9hIw/mq1.jpg?sqp=CLyK9KgG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgZShlMA8=&rs=AOn4CLDAgz1ioJVZejUuZQQQgj8zBroFPA)](https://youtu.be/twgblvN9hIw)

Now that we know that in order to package everything together, we need to use the Mflow project file. Let’s refactor our code to integrate the data validation component of our pipeline with an MLflow project.

[![Video 7](https://i9.ytimg.com/vi/-yH1jN5aJbA/mq1.jpg?sqp=COiM9KgG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgZShlMA8=&rs=AOn4CLC1h-TENeMcyfYeAnb3N-3-mUVlrg)](https://youtu.be/-yH1jN5aJbA)

Once we have the data ingestion component, let’s see how we can run it using mlflow.

[![Video 8](https://i9.ytimg.com/vi/14TSmbLB94o/mq2.jpg?sqp=CPCa9KgG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGF4gXiheMA8%3D&rs=AOn4CLAEEggqVXrmPrRRrMSRzqnvVA6YvA&retry=4)](https://youtu.be/14TSmbLB94o)

Let’s do the same exercise with our feature engineering component.

[![Video 9](https://i9.ytimg.com/vi/J1gWyKBJ8Ew/mq1.jpg?sqp=CMif9KgG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgZShlMA8=&rs=AOn4CLCTmyNWJ4u_hS2wbkdfHcVfwrT6Yg)](https://youtu.be/J1gWyKBJ8Ew)

Let’s now integrate the model training component into our training pipeline workflow.

[![Video 10](https://i9.ytimg.com/vi/lRZubYQ1SzQ/mq1.jpg?sqp=CMif9KgG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgZShlMA8=&rs=AOn4CLCjjOVRy7sZlXIYODOEBklZXgKqqg)](https://youtu.be/lRZubYQ1SzQ)

Now in the videos below we will see how:
1. Run one component after the other
2. Remove the need to manually specify commandline arguments.

In the video below let's see how can we make the training components run one after the other

[![Video 11a](https://i9.ytimg.com/vi/hAOefBEzD0w/mq1.jpg?sqp=CPSh9KgG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgZShlMA8=&rs=AOn4CLBoElda46PRhvENpfYmBAzoRpm9Rw)](https://youtu.be/hAOefBEzD0w)

Now lets see how can we use mlflow's python client to run the components in our pipeline.

[![Video 11b](https://i9.ytimg.com/vi/gu_R6c30lmE/mq1.jpg?sqp=CKCk9KgG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGcgZyhnMA8=&rs=AOn4CLD9Ejt7ZTgNK4877PkOpHgJuzqcdw)](https://youtu.be/gu_R6c30lmE)

Let's complete writing the run.py file and run all the components together

[![Video 11c](https://i9.ytimg.com/vi/rtlm85u8xwk/mq1.jpg?sqp=CMym9KgG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgZShlMA8=&rs=AOn4CLDRBTqLQ47HCY1nOZxvSWo9Fhekwg)](https://youtu.be/rtlm85u8xwk)

Now let's see how can we use hydra a configuration management system to handle the configurations used in the model training pipeline

[![Video 11d](https://i9.ytimg.com/vi/BOY6kxbtzLU/mq1.jpg?sqp=CPio9KgG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgZShlMA8=&rs=AOn4CLCu5LDTWeZVJeu0g5GQZ5SfZtcX9A)](https://youtu.be/BOY6kxbtzLU)

Now lets see how to remove all the hardcoded parameters in each of our components with configurations managed by the hydra.

[![Video 11e](https://i9.ytimg.com/vi/GytDuRyj_E0/mq2.jpg?sqp=CKSv-6gG-oaymwEmCMACELQB8quKqQMa8AEB-AHUBoAC4AOKAgwIABABGGggaChoMA8%3D&rs=AOn4CLBiFNhZzz4O4vEnjGqYXmswPMfavA&retry=4)](https://youtu.be/GytDuRyj_E0)

Now as a last step, lets package our `run.py` file also as an mlproject. 

[![Video 11f](https://i9.ytimg.com/vi/qQNntfA8tLw/mq2.jpg?sqp=CNCx-6gG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgZShlMA8=&rs=AOn4CLCJxn8H0igUK7_bzo1sGgdG69QxkA)](https://youtu.be/qQNntfA8tLw)

### Part4: Tracking model experiments and runs using mlflow

**Note: All the codes used in part4 are [here](./part4/)**  

Mlflow not just acts as an orchestrator of training pipeline but it can also act as a repository of model experiments that one does. It can be used to store model artefacts, hyperparameters, accuracy metrics and even training datasets as well. This gives us the ability to version control training runs as well and not just our model training code.

Let’s look at the video below to get an overview of what experiment tracking means and why that might be of interest to us.

[![Video 12](https://i9.ytimg.com/vi/oH_k89pJkfI/mq1.jpg?sqp=CNCx-6gG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgZShlMA8=&rs=AOn4CLCuE3kWQBn0be8IoC1xQCgoMxaprw)](https://youtu.be/oH_k89pJkfI)

Now once we understand what experiment tracking is and why it might be of importance to us, let's see how mlflow tracking server works.

[![Video 13](https://i9.ytimg.com/vi/ryUPBjRVNmQ/mq1.jpg?sqp=CPyz-6gG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgZShlMA8=&rs=AOn4CLA0xFRfEuOy4T0NO1qNTTINZs1YtA)](https://youtu.be/ryUPBjRVNmQ)

Now that we know the various modes in which an mlflow tracking server can run. Let’s now create a tracking server with s3 as artefact storage and postgres as metric store

[![Video 14](https://i9.ytimg.com/vi/KvKXSgieSFE/mq2.jpg?sqp=CPyz-6gG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGEggZShUMA8=&rs=AOn4CLCBSiFW6i5TRoYB6yI7dEp0x3gY1A)](https://youtu.be/KvKXSgieSFE)

Now that we have finally created the mlflow tracking server. Let’s see how to use mlflow tracking server to log model artefacts and model metrics

[![Video 15](https://i9.ytimg.com/vi/TvoDiWBMNFg/mq3.jpg?sqp=CPyz-6gG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGcgZyhnMA8=&rs=AOn4CLBebqhfxZPWMSI3nZWotAejT1qpLA)](https://youtu.be/TvoDiWBMNFg)

Finally let’s make changes to our training pipeline code and include experiment tracking feature.

[![]()]()