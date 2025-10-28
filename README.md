# Kubernetes CI/CD Demo

This project demonstrates a complete CI/CD pipeline for a simple containerized application, automatically building and publishing the image to the GitHub Container Registry (ghcr.io) and providing the Kubernetes manifests to deploy it.

This project shows:
* **Containerization:** A best-practice, multi-stage Dockerfile.
* **CI/CD Automation:** A GitHub Actions workflow that builds, scans, and pushes the container image.
* **Security:** Integrated `Trivy` scanning to check for OS and application vulnerabilities.
* **Kubernetes:** Declarative `Deployment` and `Service` manifests to run the app in a K8s cluster.

## Project Structure
/
├── .github/workflows/ci.yml  # GitHub Actions pipeline
├── app/                      # Application source code
│   ├── main.py               # Simple Python Flask app
│   └── Dockerfile            # Multi-stage Dockerfile
├── k8s/                      # Kubernetes manifests
│   └── deployment.yml        # Deployment & Service
└── README.

## How It Works

### 1. The CI Pipeline (`.github/workflows/ci.yml`)

On every push to the `main` branch, the following happens:
1.  **Checkout:** The code is checked out.
2.  **Login to GHCR:** The workflow authenticates to the GitHub Container Registry.
3.  **Build & Push (pre-scan):** The Docker image is built and pushed with a `pre-scan` tag.
4.  **Scan with Trivy:** Trivy scans the `pre-scan` image for `HIGH` or `CRITICAL` vulnerabilities. If any are found, the build fails.
5.  **Tag & Push (latest):** If the scan passes, the image is re-tagged as `latest` and `:${{ github.sha }}` and pushed to GHCR.

### 2. The Application (`app/`)

A very simple Python Flask app that returns "Hello, Kubernetes!"

### 3. The Deployment (`k8s/deployment.yml`)

This file contains two Kubernetes objects:
* **`Deployment`:** Tells Kubernetes to run 3 replicas of the container image.
* **`Service`:** Creates a `LoadBalancer` to expose the application to the internet.

## How to Use

### 1. Run the CI Pipeline

1.  Create a new, public GitHub repository named `k8s-ci-cd-demo`.
2.  Push the files from this project into the new repository.
3.  The GitHub Actions workflow will run automatically. Check the "Actions" tab.
4.  After it succeeds, go to your repository's main page. On the right-hand side, click "Packages" to see your published container image.

### 2. Deploy to Kubernetes (Locally with Minikube)

1.  **Install Minikube:** Follow the official guide to install [Minikube](https://minikube.sigs.k8s.io/docs/start/).
2.  **Start Minikube:**
    ```sh
    minikube start
    ```
3.  **Update the Deployment:**
    * Open `k8s/deployment.yml`.
    * Find the line `image: ghcr.io/YOUR-USERNAME/k8s-ci-cd-demo:latest`.
    * Replace `YOUR-USERNAME` with your actual GitHub username.
4.  **Apply the Manifests:**
    ```sh
    kubectl apply -f k8s/
    ```
5.  **Check the Status:**
    ```sh
    # See the pods being created
    kubectl get pods
    
    # See the service
    kubectl get service
    ```
6.  **Access the Service:**
    ```sh
    minikube service flask-app-service
    ```
    This will open the application in your browser.