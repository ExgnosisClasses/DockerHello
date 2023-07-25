pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
               echo  env.BUILD_ID
               bat "docker build -t hello:latest -f Dockerfile"
            } 
        }
        stage('Hello') {
            steps {
               echo 'Hello World'
            } 
        }
    }
}