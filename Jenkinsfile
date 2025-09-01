pipeline {
  agent any
  environment {
    GIT_SSH_COMMAND = 'ssh -o StrictHostKeyChecking=no'
  }
  stages {
    stage('Clone Repo') {
      steps {
        git url: 'git@github.com:abhilash07-10/simple-html-app.git', credentialsId: 'github-ssh'
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

