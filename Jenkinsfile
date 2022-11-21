pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
       steps {
        sh 'py.test tests/test_main_page.py'
    }
    }
  }
}
