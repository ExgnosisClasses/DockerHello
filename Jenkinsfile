pipeline {
    agent any

    environment {
        // Determins whether or not to run the service
        DEPLOY = "NO"
    }

    stages {
        stage("Registry") {
            // Ensure the registry is running. 
            steps {
                bat "docker start registry"
            }
        }
        stage('Build') {
            // Build the actual docker container
            steps {
                bat "docker build -t localhost:5000/hello:${env.BUILD_TAG} -f Dockerfile ."
            } 
        }
        stage('Deliver') {
            steps {
                // Push the container into the specified registry
                bat "docker push localhost:5000/hello:${env.BUILD_TAG}"
               
            } 
        }
        stage('Clean') {
            // Remove the image from the local image cache
            bat "docker image rm localhost:5000/hello:${env.BUILD_TAG}"
        }
        stage('Deploy') {
            when {
                environment name: 'DEPLOY', value: 'YES'
            }
            steps {
               // If we are deploying, we will pull the image from the local registry
               bat "docker run -d -p 80:5000 localhost:5000/hello:${env.BUILD_TAG}"
            } 
        }
    }
    post {
        always {
            // Shut down the registry until we need it again.
            bat "docker stop registry"
        }
    }
}