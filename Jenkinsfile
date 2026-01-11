pipeline {
  agent any
  options { timestamps() }

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Prepare .env') {
      steps {
        withCredentials([
          string(credentialsId: 'ECI_ID', variable: 'ID'),
          string(credentialsId: 'ECI_PASSWORD', variable: 'PW'),
          string(credentialsId: 'ZONE_ID', variable: 'ZONE_ID'),
          string(credentialsId: 'API_BASE_URL', variable: 'API_BASE_URL'),
        ]) {
          script {
            writeFile file: '.env',
            text: """ECI_ID=${ID}
ECI_PASSWORD=${PW}
ZONE_ID=${ZONE_ID}
API_BASE_URL=${API_BASE_URL}
"""
          }
        }
      }
    }

    stage('Run API Test') {
      steps {
        catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
          // docker-compose.yml에 정의된 api-test 서비스를 실행
          // --build: 코드가 바뀌었을 수 있으니 새로 빌드
          // --abort-on-container-exit: 테스트 끝나면 컨테이너 종료
          sh 'docker-compose up --build --abort-on-container-exit api-test'
        }
      }
    }
    
    stage('Run E2E Test') {
      steps {
        catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
          sh 'rm -rf allure-results/*'
          sh 'docker-compose up --build --abort-on-container-exit e2e-test'
        }
      }
    }
  }

  post {
    always {
        allure([
            includeProperties: false,
            jdk: '',
            results: [[path: 'allure-results']]
        ])

        publishHTML(target: [
            reportDir: 'reports',
            reportFiles: 'api-report.html, e2e-report.html',
            reportName: 'Pytest HTML Report',
            allowMissing: true,
            alwaysLinkToLastBuild: true,
            keepAll: true
        ])

      archiveArtifacts artifacts: 'reports/**, screenshots/**, logs/**',
                       fingerprint: true,
                       allowEmptyArchive: true
      
      // 실행이 끝난 후 컨테이너들 정리
      sh 'docker-compose down'
    }
  }
}