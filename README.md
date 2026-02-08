<!--
title: 'AWS Simple HTTP Endpoint example in Python'
description: 'This template demonstrates how to make a simple HTTP API with Python running on AWS Lambda and API Gateway using the Serverless Framework.'
layout: Doc
framework: v4
platform: AWS
language: python
authorLink: 'https://github.com/serverless'
authorName: 'Serverless, Inc.'
authorAvatar: 'https://avatars1.githubusercontent.com/u/13742415?s=200&v=4'
-->

# AWS Python HTTP API – Serverless Project

This project is a simple serverless HTTP API built on AWS using Python and the Serverless Framework. The goal of this project was to understand how a real-world serverless application is structured, deployed, and managed using AWS-managed services.
The entire infrastructure is created from scratch using Infrastructure as Code (IaC) via the Serverless Framework, which internally uses AWS CloudFormation.

**What this project does**

-> Deploys Python Lambda functions on AWS

-> Exposes them using API Gateway (HTTP API)

-> Uses Serverless Framework for deployment  
-> Runs in us-east-2 (Ohio) region

It includes two endpoints:

  / → returns a hello message
  
  /bye → returns a bye message

**Tech Stack**

-> Language: Python 3.9

-> Framework: Serverless Framework (v4)

-> Cloud Provider: AWS

-> Core Services Used:

  -> AWS Lambda
  
  -> AWS API Gateway (HTTP API)
  
  -> AWS CloudFormation
  
  -> AWS IAM

**AWS CloudWatch Logs**

Project Structure
aws-python-http-api-project/
├── handler.py          # Lambda function handlers
├── serverless.yml      # Infrastructure & service configuration
├── README.md           # Project documentation
├── .gitignore

**Architecture Overview**

**Deployed Architecture**

<img width="1054" height="632" alt="image" src="https://github.com/user-attachments/assets/7b790656-3e17-4093-b5dc-3f22fb4c7164" />

This project uses a simple AWS serverless architecture.

-> API Gateway receives HTTP requests from users

-> AWS Lambda handles request processing and business logic

-> DynamoDB is used for storing and retrieving data

-> Amazon S3 manages object storage

-> Amazon CloudWatch captures logs and monitors executions

-> IAM controls access and permissions between services

-> CloudFormation provisions and manages all infrastructure as code

-> The response is then returned to the client through the API Gateway.

All resources are deployed and managed using the Serverless Framework, which automatically generates and applies CloudFormation stacks behind the scenes.

**Deployment**

  The service is deployed using the Serverless CLI.

    **serverless deploy**

  During deployment:
  
  -> Lambda functions are packaged
  
  -> CloudFormation stack is created/updated
  
  -> API Gateway endpoints are provisioned
  
  -> IAM roles and permissions are configured automatically

**API Endpoints**

  After deployment, the API is accessible via the generated API Gateway URL:

  -> GET /
  
  -> GET /bye

  The Serverless Framework provides the exact endpoint URL after deployment.

**Why Serverless Framework**

-> Simplifies AWS infrastructure management

-> Reduces boilerplate CloudFormation code

-> Handles packaging, deployment, and permissions

-> Makes serverless development faster and more maintainable


**Why I built this**

I built this project to:

-> Get hands-on experience with AWS serverless services

-> Understand how the Serverless Framework works internally

-> Practice deploying real cloud resources instead of only reading docs

**Notes**

-> This project focuses on core serverless concepts, not frontend or database integration

-> No credentials or secrets are stored in this repository

-> .serverless and AWS-related local files are ignored using .gitignore

**Author**

  **Shubham**
  
  _Cloud & DevOps Enthusiast_
