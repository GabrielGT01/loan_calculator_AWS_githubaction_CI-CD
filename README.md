# Loan Risk Score App

A machine learning-powered web application that predicts the risk score for loan applicants based on historical data. This project leverages a trained CatBoost model, Flask API, Docker, and a full CI/CD pipeline with GitHub Actions, deploying to AWS services including ECS, ECR, and EC2.

---

## 🚀 Features

- **Risk Prediction:** Predict loan risk scores based on applicant data.
- **Machine Learning:** Trained using CatBoost and scikit-learn.
- **Web Interface:** User-friendly UI built with Flask.
- **Containerization:** Dockerized for portability and easy deployment.
- **CI/CD Pipeline:** Automated testing and deployment using GitHub Actions.
- **Cloud Deployment:** Hosted on AWS using ECR, ECS, and EC2.

---

## 🧠 Machine Learning Workflow

1. **Data Preprocessing:** Cleaned and prepared the dataset (`Loan.csv`) for modeling.
2. **Model Training:** Utilized CatBoost for its efficiency with categorical data.
3. **Model Evaluation:** Assessed model performance using appropriate metrics.
4. **Serialization:** Saved the trained model using joblib for deployment.

---

## 🖥️ Application Architecture

- **Frontend:** Flask templates rendering HTML pages for user interaction.
- **Backend:** Flask routes handling form submissions and returning predictions.
- **Model Integration:** Loaded the serialized CatBoost model to make predictions based on user input.

---

## 🐳 Dockerization

The application is containerized using Docker for consistency and ease of deployment.

**Sample Dockerfile:**

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```
# Loan Risk Score App

A machine learning-powered web application that predicts the risk score for loan applicants based on historical data. This project leverages a trained CatBoost model, Flask API, Docker, and a full CI/CD pipeline with GitHub Actions, deploying to AWS services including ECS, ECR, and EC2.

---

## ☁️ Cloud Infrastructure

This project uses several AWS services to achieve a robust, secure, and scalable deployment for the Loan Risk Score App.

### **Infrastructure Components**

#### **1. Amazon Elastic Container Registry (ECR)**
- Acts as a secure, private Docker image repository.
- GitHub Actions CI workflow builds the Docker image and pushes it to ECR on every code change or push to the main branch.

#### **2. Amazon Elastic Compute Cloud (EC2)**
- Provides the virtual servers (instances) where your Docker containers (the Flask application) actually run.
- The deployment pipeline connects to the EC2 instance, pulls the latest Docker image from ECR, and starts (or restarts) the container.
- Security Groups restrict inbound traffic (e.g., allow only HTTP/HTTPS or a specific IP range).

#### **3. Amazon Elastic Container Service (ECS) [Optional/Scalable]**
- Can be used to manage, orchestrate, and scale multiple containers.
- ECS pulls images directly from ECR and manages running, updating, and scaling your containers (e.g., for high availability or zero-downtime deployments).
- **Fargate** can be leveraged for serverless compute (no need to manage EC2 instances), or you can use ECS with EC2 launch type.

#### **4. IAM (Identity and Access Management)**
- IAM Roles are used to securely grant GitHub Actions workflow permission to interact with AWS (pushing images, updating services, etc.).
- Separate IAM roles control EC2/ECS access to pull images from ECR, enhancing security by granting only the permissions needed.

---

### **Typical Cloud Deployment Workflow**

1. **Code is pushed to GitHub.**
2. **GitHub Actions runs CI/CD pipeline:**
    - Linting, testing.
    - Build Docker image.
    - Push Docker image to Amazon ECR.
3. **Deployment job:**
    - Connects securely (via SSH or AWS SSM) to EC2 or triggers ECS update.
    - Pulls the latest image from ECR.
    - Restarts the Docker container (or ECS service/task) with the new image.
4. **End users** interact with the running Flask app via a public or private endpoint (EC2 public IP, Load Balancer DNS, or ECS Service Endpoint).

---

### **Architecture Diagram**

  +----------+       CI/CD         +----------+         Pull Image       +----------+
  |  GitHub  |  ----------------> |  ECR     |  --------------------->  |  EC2/ECS |
  +----------+   Push Docker Img  +----------+      (docker run)        +----------+
       |                                                                  |
       |  GitHub Actions Workflow                                         |
       +------------------------------------------------------------------+
---

### **Security and Best Practices**

- **Secrets Management:** All AWS keys and sensitive info are stored as GitHub Secrets, never hard-coded.
- **IAM Roles:** Principle of least privilege for CI/CD and EC2/ECS roles.
- **Network Security:** Use Security Groups, VPC, and optionally an Application Load Balancer for production.
- **Scalability:** ECS or EC2 Auto Scaling can be added as traffic grows.

---

## Example AWS Resources Used

- **ECR Repository:** `loan-risk-ecr` (stores Docker images)
- **EC2 Instance:** t3.micro (runs Flask/Docker container)
- **(Optional) ECS Cluster:** Runs scalable Docker tasks
- **IAM Roles:** 
    - `GitHubActionsDeployRole` (CI/CD pipeline)
    - `EC2ContainerRole` or `ECSServiceRole`
- **Security Group:** Allows HTTP/HTTPS or custom ports

---

## 📦 Example CloudFormation/Terraform Resources (optional for IaC)

If you want to provision the infrastructure automatically, you can use CloudFormation or Terraform with resources like:

- `AWS::ECR::Repository`
- `AWS::EC2::Instance`
- `AWS::ECS::Cluster`
- `AWS::IAM::Role`
- `AWS::EC2::SecurityGroup`

---

## 🔗 References

- [AWS ECR Documentation](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html)
- [AWS ECS Documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html)
- [AWS EC2 Documentation](https://docs.aws.amazon.com/ec2/index.html)
- [IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [GitHub Actions for AWS](https://github.com/aws-actions)

---

