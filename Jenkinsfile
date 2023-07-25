pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
               echo  env.BUILD_ID
              // bat 'docker build -t hello:{env.BUILD_ID} -f Dockerfile'
            } 
        }
        stage('Hello') {
            steps {
               echo 'Hello World'
            } 
        }
    }
}