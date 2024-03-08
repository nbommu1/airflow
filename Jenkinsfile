pipeline {
    agent any
    tools {
    // a bit ugly because there is no `@Symbol` annotation for the DockerTool
    // see the discussion about this in PR 77 and PR 52: 
    // https://github.com/jenkinsci/docker-commons-plugin/pull/77#discussion_r280910822
    // https://github.com/jenkinsci/docker-commons-plugin/pull/52
    'org.jenkinsci.plugins.docker.commons.tools.DockerTool' '18.09'
    }
    stages {
        stage('Deploy to Astronomer') {
            when {
                expression {
                    return env.GIT_BRANCH == "origin/main"
                }
            }
            steps {
                checkout scm
                echo sh(script: 'env|sort', returnStdout: true)
                withCredentials([string(credentialsId: 'ASTRO_API_TOKEN', variable: 'ASTRO_API_TOKEN')]) {
                    sh '''
                    curl -LJO https://github.com/astronomer/astro-cli/releases/download/v1.24.1/astro_1.24.1_linux_amd64.tar.gz
                    tar -zxvf astro_1.24.1_linux_amd64.tar.gz astro && rm astro_1.24.1_linux_amd64.tar.gz
                    echo env.ASTRO_API_TOKEN
                    ./astro deploy --deployment-name Dev
                    '''
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}
