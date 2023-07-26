pipeline {
    agent any

    environment {
        DEPLOY = "NO"
    }

    stages {
        stage("Registry") {
            // Ensure the registry is running
            steps {
                bat "docker start registry"
            }
        }
        stage('Build') {
            steps {
               bat "docker build -t localhost:5000/hello:${env.BUILD_TAG} -f Dockerfile ."
            } 
        }
        stage('Deliver') {
            steps {
               bat "docker push localhost:5000/hello:${env.BUILD_TAG}"
            } 
        }
        stage('Deploy') {
            when {
                environment name: 'DEPLOY', value: 'YES'
            }
            steps {
               bat "docker run -d -p 80:5000 localhost:5000/hello:${env.BUILD_TAG}"
            } 
        }
    }
    post {
        always {
            bat "docker stop registry"
        }
    }
}