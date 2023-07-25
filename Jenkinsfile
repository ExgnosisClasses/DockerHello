pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
               echo  env.BUILD_ID
               bat "docker build -t localhost:5000/hello:${env.BUILD_TAG} -f Dockerfile ."
            } 
        }
        stage('Deliver') {
            steps {
               bat "docker push localhost:5000/hello:${env.BUILD_TAG}"
            } 
        }
        stage('Deploy') {
            steps {
               bat "docker run -d -p 80:5000 localhost:5000/hello:${env.BUILD_TAG} -name Hello-${env.BUILD_TAG}"
            } 
        }
    }
}