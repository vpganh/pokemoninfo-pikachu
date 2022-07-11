# pokemoninfo-pikachu

## Deploy a Web App Using Python and IBM Code Engine
Why do this project?
Whether you are just learning Python and Flask or a seasoned developer you need to find a place to deploy your app, to make it available to the world. You can build your own server or maybe get a virtual machine from one of the cloud providers like Digital Ocean, AWS, IBM, Azure, Google etc. But that is so 2012. You want to do it the Cloud Native way and that means you are going to look at containers and Kubernetes.

In this project you will deploy a Python Flask application on to a Code Engine cluster. We are not going to build a complex Python-Flask application, as the focus of this project is deployment not coding Python. Instead, will build just the customary ‘hello-world’ application and get it deployed on to a real Code Engine cluster. The technologies we would be working with are Flask, Docker, Code Engine (IBM Cloud Code Engine Service) and Skills Network Cloud IDE (powered by Eclipse Theia).

Flask is lightweight, minimalistic Python web framework designed to get an application up and running quickly. It is sometimes called a micro-framework as it does not require specific tools or plug-ins to run. This project is not really about Flask.

Docker is an open source application that allows us to package an application along with all it’s dependencies. Allowing us to create, manage, deploy, and replicate applications using containers. Docker defines a container as “a standard unit of software that packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another.”

Any application deployed using Docker is isolated from the operating system resources and ensures that it works uniformly across various environments. Deploying our Flask application using Docker will allow us to replicate the application across different servers with minimal reconfiguration.

Code Engine is a platform by IBM that enables developers to easily deploy code without having to worry about server side maintenance. This allows for efficiency, scaling and abstraction of infrastructure. The IBM Cloud Code Engine Service (ICE) is “a fully managed, serverless platform. Bring your container images, batch jobs, or source code and let IBM Cloud Code Engine manage and secure the underlying infrastructure for you.”

Cloud IDE (by IBM Developer Skills Network) is a complete Integrated Development Environment (IDE) that runs in a web browser. It is based on Eclipse Theia which was inspired by the popular Visual Studio Code (VS Code) and it supports many of it’s extensions. The Cloud IDE you are using is configured and optimized for deploying applications to IKS.

## Prerequisites (optional)
To do this project, you will need the following:

An IBM Cloud account (sign up for a free account)
A very basic knowledge of Python

## Building and Containerizing the Flask application
Let’s create our `Hello World` application! In the Cloud IDE, create an app folder (hint: use File/New Folder menu) and switch to it. Inside this directory create a `main.py` file

Open a terminal session in the Cloud IDE and switch in to the project directory where we have the `Dockerfile` and the app directory. Run `$ docker build -t hello-world` . in the Cloud IDE terminal. This builds the image, giving it a tag called hello-world.

Next run the image using `$ docker run -dp 8080:8080 hello-world`.

Finally using the Launch Application tab at port 8080 (specified in our flask script), we are able to see the output of our Flask application.

