### Cloud Monitoring App on Kubernetes

This project is a cloud monitoring application built with Python using the Flask framework), Docker, Kubernetes, and AWS services. It demonstrates how to create a monitoring application and deploy it to a Kubernetes cluster on AWS.

### Prerequisites: 
Programmatic access and AWS CLI configured.
Python 3 installed.
Docker and Kubectl installed.

Part 1: Deploying the Flask Application Locally:
 Step 1: Clone the Code
Clone the code from the repository: git clone <repository_url> 
 Step 2: Install Dependencies
The application uses the psutil, Flask, Plotly, and boto3 libraries. Install them using pip:
pip3 install -r requirements.txt 
 Step 3: Run the Application
To run the application, navigate to the root directory of the project and execute the following command:
python3 app.py 
This will start the server on localhost:5000. Navigate to http://localhost:5000/ on your browser to access the application.

Part 2: Dockerize the Application
 Step 1: Create a Dockerfile in the root directory of the project.
 Step 2: Build the Docker Image: docker build -t <image_name> . 
 Step 3: Run the Docker Container: docker run -p 5000:5000 <image_name>
 Step 4: Pushing the Docker Image to ECR
 Step 5: Create an ECR Repository in your aws console, 
 then Push the Docker Image to ECR: docker push <ecr_repo_uri>:<tag>

Part 3 - Deploy the application on AWS EKS Cluster
To deploy the application on AWS EKS Cluster, you need to follow the below steps:

Create two IAM Roles: Amazon EKS Cluster IAM Role and Amazon EKS Node IAM Role. 
You can refer to the official AWS documentation for detailed instructions on how to create these roles.

Part 4- Create an EKS Cluster and Deploying the Application Using Python
 Step 1: Create an EKS Cluster
 Create an EKS cluster and add a node group.
 
 Step 2: To connect to your EKS Cluster, check that you have installed kubectl correctly by running the following command: kubectl version

Note: Before deploying your Kubernetes cluster, ensure your VPC and subnets are appropriately configured. Also, create a security group and add an incoming rule allowing port 5000.

 Step 3: Create a Kubernetes deployment and service using a Python script, and name the file "eks.py". Then, copy and paste the script provided below into the file. Once you have done this, run the script by executing the command "python eks.py".
 
 Replace <image Uri> in the eks.py with the actual URI of your Docker image in the ECR registry.
 
 Step 4: Deploy your application on AWS EKS Cluster: 
 run the following commands
 
 kubectl get deployment -n default: This will check depolyments to see if your container successfuly on the EKS Cluster. 
  
  kubectl get pods -n default: To check if the pods were successfully deployed on your nodes.
  The app pods will be running. 

Finally, to check container port is open to network communication: 
  kubectl get service -n default 

This will create a Kubernetes service that exposes the application on port 5000. To access the application, you can use the load balancer DNS name or IP address associated with the service.





 

