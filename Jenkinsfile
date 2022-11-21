pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
   stage('Run pytest'){
       sh "pytest test_main_page.py"
    }    
  }
}
