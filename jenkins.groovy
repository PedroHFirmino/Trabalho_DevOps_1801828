pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/usuario/Trabalho_DevOps_1801828.git'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest test_aluno.py'
            }
        }
        stage('Build Docker Images') {
            steps {
                sh 'docker-compose build'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }

    post {
        always {
            echo 'Pipeline complete!'
        }
    }
}