pipeline {
  agent any
  stages {
    stage('Clone Repo') {
      steps {
        git 'https://github.com/your-username/simple-html-app.git'
      }
    }
    stage('Build Docker Image') {
      steps {
        sh 'docker build -t simple-html-app .'
      }
    }
    stage('Run Container') {
      steps {
        sh 'docker run -d -p 5000:5000 simple-html-app'
      }
    }
  }
}
