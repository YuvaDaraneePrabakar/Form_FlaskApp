pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/YuvaDaraneePrabakar/Form_FlaskApp.git'
            }
        }
        stage('Docker Build') {
            steps {
                script {
                    sh 'docker build -t webapp .'
                }
            }
        }
        stage('Docker Login') {
            steps {
                script {
                    //withCredentials([string(credentialsId: 'docker', variable: 'dockerhub')]) {}
                    sh 'docker login -u yuvadaranee -p Success@143'
                    
                }
            }
        }
        stage('Docker Test') {
            steps {
                script {
                    sh 'docker tag webapp myrepository/webapp'
                    sh 'docker push myrepository/webapp:latest'
                }
            }
        }
        stage('Run Docker App') {
            steps {
                script {
                    sh 'docker pull myrepository/webapp:latest'
                    sh 'docker run -d -p 5000:5000 myrepository/webapp:latest'
                }
            }
        }
    }
}
