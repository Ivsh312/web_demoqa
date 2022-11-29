pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('git') {
            steps {
                git 'https://github.com/Ivsh312/web_demoqa.git'
            }
        }
        stage('Pip install') {
            steps {
                sh 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py'
                sh 'python3 get-pip.py --user'
                sh 'PATH=$WORKSPACE/venv/bin:$HOME/.local/bin:$PATH'
            }
        }
        stage('create venv'){
            steps {
                sh '''
                if [ ! -d "venv" ]; then
                        virtualenv venv
                fi'''
            }
        }
        stage('Remove and recreate config and reporting') {
            environment {
              credentials = credentials('defoult_parabank')
            }
            steps {
                sh '''if [ -d "config" ]; then
                                        rm -r config
                      fi'''
                sh '''if [ -d "reporting" ]; then
                                        rm -r reporting
                      fi'''
                sh 'mkdir reporting'
                sh 'mkdir config'
                sh 'touch config/config.txt'
                dir('config'){
                     writeFile file:'config.txt', text:"[CREDENTIALS]\nusername=${credentials_USR}\npassword=${credentials_PSW}"
                }
                sh 'cd config'
            }

        }
        stage('Install requirements') {
            steps {
                sh 'pip3 install -r requirements.txt'
                sh 'pip3 install allure-pytest'
                sh '. venv/bin/activate'
            }
        }
        stage('Run testing') {
            steps {
                sh 'python3 -m pytest tests --alluredir="./reporting"|| true'
            }
        }
        stage('allure'){
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'reporting']]
            }
        }
    }
    post {
        always {archiveArtifacts artifacts: 'reporting/**', followSymlinks: false}

        }
}