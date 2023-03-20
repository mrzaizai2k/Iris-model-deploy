# iris-model-deploy
Just try to deploy a simple ML model like Iris classification

Here are the steps to run your Flask app with Docker on a new PC and connect to it with HTML:

1. Install Docker
2. Clone the project repository: `git clone <repository-url>`
3. Build the Docker image: create new project for that. Open terminal > command prompt > `docker build -t <image-name>`
4. Run the Docker container `docker run -p 5000:5000 <image-name>`
5. Open the html file again

If you want to connect port 8000 in local host to port 5000 in container 

1. Run the Docker container `docker run -p 5000:5000 <image-name>`
2. Change the file `templates/index.html` to `fetch('http://localhost:8000/predict'`
