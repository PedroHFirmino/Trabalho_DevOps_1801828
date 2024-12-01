pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/usuario/Trabalho_DevOps_RA.1801828'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest test_app.py'
            }
        }
        stage('Build and Deploy') {
            steps {
                sh 'docker-compose up --build -d'
            }
        }
    }
}
