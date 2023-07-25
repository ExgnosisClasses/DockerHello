pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
               echo  env.BUILD_ID
               bat "docker build -t localhost:5000/hello:${env.BUILD_TAG} -f Dockerfile ."
            } 
        }
        stage('Store') {
            steps {
               echo 'Hello World'
            } 
        }
    }
}