pipeline {
    agent any
    stages {
        stage('Deploy to Astronomer') {
            when {
                expression {
                    return env.GIT_BRANCH == "origin/main"
                }
            }
            steps {
                checkout scm
                sh '''
                astro deploy --deployment-name Dev 
                '''
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}
