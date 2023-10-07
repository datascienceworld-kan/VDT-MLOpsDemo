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

[![Video 1](https://i9.ytimg.com/vi/fM_4jWS0w00/mq1.jpg?sqp=CITcg6kG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgZShlMA8=&rs=AOn4CLD-P3GwuOffS8T9OPDzGkDV6qoQrA)](https://youtu.be/fM_4jWS0w00)

Now that we know what mlops is and the popular tools used, lets now see what the common issues with a traditional data science model training workflow are and how those issues can be fixed.   

[![Video 2](https://i9.ytimg.com/vi/5tXn2xYyX3w/mq2.jpg?sqp=CLDeg6kG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGC0gSSh_MA8=&rs=AOn4CLCNyYylBBYaEOJM8RGVuU7OUeY-sQ)](https://youtu.be/5tXn2xYyX3w)

### Part2: Building training pipelines

**Note: All the codes used in part 2 videos are [here](./part2/)**

In the previous few videos, we saw what mlops is and how a traditional data science workflow is not effective. In this section we will see how to create a model training pipeline.

Let’s first look at how to create a data ingestion pipeline. We will assume that our data is on a data lake and we need to decouple the ingestion code from the location of the data

[![Video 3](https://i9.ytimg.com/vi/VfEceK2AbeY/mq3.jpg?sqp=CLDeg6kG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGIgYihiMA8=&rs=AOn4CLCpK66289xlsXVnD51Zjbtaodh8Xg)](https://youtu.be/VfEceK2AbeY)

The next part is to build a feature engineering pipeline. Let’s look at the next video and see what principles can be followed to create a feature engineering pipeline. 

[![Video 4](https://i9.ytimg.com/vi/xDoiWSHs7Y8/mq2.jpg?sqp=CLDeg6kG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGwgbChsMA8=&rs=AOn4CLCYHmA2grIO9chtsEfHhDWXXW7SZQ)](https://www.youtube.com/watch?v=xDoiWSHs7Y8 "Video 4")

Finally let’s see how to create a model training pipeline.

[![Video 5](https://i9.ytimg.com/vi/zffaeWPl_bc/mq3.jpg?sqp=CLDeg6kG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgZShlMA8=&rs=AOn4CLBR52D1gVbbRD5Co-XtBu67JLiHjw)](https://youtu.be/zffaeWPl_bc)



### Part 3: Orchestrating ml pipelines using mlflow

**Note: All the codes used in part3 are [here](./part3/)**

So far we’ve created individual components of a training pipeline. Let’s now see how we can run all these components together using mlfow acting as an orchestrator. So far we’ve created individual components of a training pipeline. Let’s now see how we can run all these components together using mlfow acting as an orchestrator. 

[![Video 6](https://i9.ytimg.com/vi/twgblvN9hIw/mq2.jpg?sqp=CLDeg6kG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgZShlMA8=&rs=AOn4CLASTEajfatJ704ZjDJlEF-l7R6QjA)](https://youtu.be/twgblvN9hIw)

Now that we know that in order to package everything together, we need to use the Mflow project file. Let’s refactor our code to integrate the data validation component of our pipeline with an MLflow project.

[![Video 7](https://i9.ytimg.com/vi/-yH1jN5aJbA/mq2.jpg?sqp=CLDeg6kG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgZShlMA8=&rs=AOn4CLBqP5p9_5DAsq8QrxFUssjW-lM1tA)](https://youtu.be/-yH1jN5aJbA)

Once we have the data ingestion component, let’s see how we can run it using mlflow.

[![Video 8](https://i9.ytimg.com/vi/14TSmbLB94o/mq3.jpg?sqp=CLDeg6kG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGF4gXiheMA8=&rs=AOn4CLB4ucTz33BeqPwjfdmxLKikSgRdkw)](https://youtu.be/14TSmbLB94o)

Let’s do the same exercise with our feature engineering component.

[![Video 9](https://i9.ytimg.com/vi/J1gWyKBJ8Ew/mq3.jpg?sqp=CLDeg6kG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgZShlMA8=&rs=AOn4CLDgQ6Y-JziP555XTxRwq9sPrkDZVg)](https://youtu.be/J1gWyKBJ8Ew)

Let’s now integrate the model training component into our training pipeline workflow.

[![Video 10](https://i9.ytimg.com/vi/lRZubYQ1SzQ/mq3.jpg?sqp=CLDeg6kG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGYgZihmMA8=&rs=AOn4CLC-DqUe88hWTf1b3whiMCGX28UBNA)](https://youtu.be/lRZubYQ1SzQ)

Now in the videos below we will see how:
1. Run one component after the other
2. Remove the need to manually specify commandline arguments.

In the video below let's see how can we make the training components run one after the other

[![Video 11a](https://i9.ytimg.com/vi/hAOefBEzD0w/mq2.jpg?sqp=CNzgg6kG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgZShlMA8=&rs=AOn4CLARAhTZzuzOtE5QzEWyV40b3BOhWQ)](https://youtu.be/hAOefBEzD0w)

Now lets see how can we use mlflow's python client to run the components in our pipeline.

[![Video 11b](https://i9.ytimg.com/vi/gu_R6c30lmE/mq3.jpg?sqp=CNzgg6kG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgZShlMA8=&rs=AOn4CLDaR_gWi4zTXOVq-neqS1ZPSMgkHQ)](https://youtu.be/gu_R6c30lmE)

Let's complete writing the run.py file and run all the components together

[![Video 11c](https://i9.ytimg.com/vi/rtlm85u8xwk/mq2.jpg?sqp=CNzgg6kG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGHIgWyg5MA8=&rs=AOn4CLDHcffNoa58ORJHJUG5R9rjC_cqvQ)](https://youtu.be/rtlm85u8xwk)

Now let's see how can we use hydra a configuration management system to handle the configurations used in the model training pipeline

[![Video 11d](https://i9.ytimg.com/vi/BOY6kxbtzLU/mq2.jpg?sqp=CNzgg6kG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgZShlMA8=&rs=AOn4CLD9Woj24BzGzVszQEpb0nf_DNIXLA)](https://youtu.be/BOY6kxbtzLU)

Now lets see how to remove all the hardcoded parameters in each of our components with configurations managed by the hydra.

[![Video 11e](https://i9.ytimg.com/vi/GytDuRyj_E0/mq2.jpg?sqp=CNzgg6kG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgZShlMA8=&rs=AOn4CLByWAuFf0dWLGvDzXQ8Sf8ipVM9Vg)](https://youtu.be/GytDuRyj_E0)

Now as a last step, lets package our `run.py` file also as an mlproject. 

[![Video 11f](https://i9.ytimg.com/vi/qQNntfA8tLw/mq2.jpg?sqp=CNzgg6kG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgZShlMA8=&rs=AOn4CLCi2QsxoP9H980AL4JRYv3PBvYrDA)](https://youtu.be/qQNntfA8tLw)

### Part4: Tracking model experiments and runs using mlflow

**Note: All the codes used in part4 are [here](./part4/)**  

Mlflow not just acts as an orchestrator of training pipeline but it can also act as a repository of model experiments that one does. It can be used to store model artefacts, hyperparameters, accuracy metrics and even training datasets as well. This gives us the ability to version control training runs as well and not just our model training code.

Let’s look at the video below to get an overview of what experiment tracking means and why that might be of interest to us.

[![Video 12](https://i9.ytimg.com/vi/oH_k89pJkfI/mq1.jpg?sqp=CNzgg6kG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgZShlMA8=&rs=AOn4CLCayVXG5qkl3aqmyfEJUHrmZnmyFA)](https://youtu.be/oH_k89pJkfI)

Now once we understand what experiment tracking is and why it might be of importance to us, let's see how mlflow tracking server works.

[![Video 13](https://i9.ytimg.com/vi/ryUPBjRVNmQ/mq1.jpg?sqp=CNzgg6kG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgZShlMA8=&rs=AOn4CLCc6qFYaG0bAfTalzBSDT4k4xEKPQ)](https://youtu.be/ryUPBjRVNmQ)

Now that we know the various modes in which an mlflow tracking server can run. Let’s now create a tracking server with s3 as artefact storage and postgres as metric store

[![Video 14](https://i9.ytimg.com/vi/KvKXSgieSFE/mq2.jpg?sqp=CNzgg6kG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGEggZShUMA8=&rs=AOn4CLAlwSwptcooplQtihvi8XwreUegVg)](https://youtu.be/KvKXSgieSFE)

Now that we have finally created the mlflow tracking server. Let’s see how to use mlflow tracking server to log model artefacts and model metrics

[![Video 15](https://i9.ytimg.com/vi/TvoDiWBMNFg/mq3.jpg?sqp=CNzgg6kG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGcgZyhnMA8=&rs=AOn4CLCsCrWnnSt1t-xryItOMM0b1mjvZA)](https://youtu.be/TvoDiWBMNFg)

Finally let’s make changes to our training pipeline code and include experiment tracking feature.

[![Video 16](https://i9.ytimg.com/vi/86yppjtwl9k/mq2.jpg?sqp=CNzgg6kG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGkgaShpMA8=&rs=AOn4CLD7N4xKMhgh8PTQalxWn3rbZwbDYQ)](https://youtu.be/86yppjtwl9k)