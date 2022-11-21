pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage("test PythonEnv") {

    withPythonEnv('python3') {
        sh 'pip install pytest'
        sh 'pytest mytest.py'
      }
    }
  }
}
