pipeline {
    agent any

    environment {
        GITHUB_REPO = 'Suheab1995/microservices-in-python'
        GITHUB_TOKEN = credentials('githubtoken')
    }

    stages {
        stage('Trigger GitHub Actions Workflow') {
            steps {
                script {
                    def curlCommand = "curl -X POST \
                        -H 'Authorization: token ${env.GITHUB_TOKEN}' \
                        -H 'Accept: application/vnd.github.everest-preview+json' \
                        -H 'Content-Type: application/json' \
                        -d '{\"event_type\": \"sampleevent\"}' \
                        https://api.github.com/repos/${env.GITHUB_REPO}/dispatches"
                    def response = sh(script: curlCommand, returnStdout: true).trim()
                    echo "Response: ${response}"

                }
            }
        }
    }
}
