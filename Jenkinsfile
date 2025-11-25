pipeline {
    agent any
    
    environment {
        // Update these values with your Docker Hub username and desired image name
        IMAGE = "pramatharao/sem5_calc_imt2023116:latest"
        VENV = ".venv"
        CONTAINER_NAME = "calculator-cli"
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from repository...'
                checkout([$class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/p-r-a-o/sem5_calc.git',
                        credentialsId: 'github-creds'
                    ]]
                ])
            }
        }
        
        stage('Create Virtual Environment') {
            steps {
                echo 'Setting up Python virtual environment...'
                sh '''
                    python3 -m venv $VENV
                    $VENV/bin/pip install --upgrade pip
                '''
            }
        }
        
        stage('Install Dependencies') {
            steps {
                echo 'Installing project dependencies...'
                sh '$VENV/bin/pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                echo 'Running unit tests...'
                sh '''
                    $VENV/bin/pytest -v --cov=calculator --cov-report=term-missing
                '''
            }
        }
        
        stage('Code Quality Check') {
            steps {
                echo 'Running code quality checks...'
                sh '''
                    $VENV/bin/pip install flake8
                    $VENV/bin/flake8 calculator.py --max-line-length=100 || true
                '''
            }
        }
        
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t $IMAGE .'
            }
        }
        
        stage('Push Docker Image') {
            steps {
                echo 'Pushing Docker image to Docker Hub...'
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'USER',
                    passwordVariable: 'PASS'
                )]) {
                    sh '''
                        echo $PASS | docker login -u $USER --password-stdin
                        docker push $IMAGE
                        docker logout
                    '''
                }
            }
        }
        
        stage('Deploy Container') {
            steps {
                echo 'Deploying calculator application...'
                sh '''
                    # Pull the latest image
                    docker pull $IMAGE
                    
                    # Stop and remove existing container if it exists
                    docker stop $CONTAINER_NAME || true
                    docker rm $CONTAINER_NAME || true
                    
                    # Run the new container in interactive mode
                    docker run -dit --name $CONTAINER_NAME $IMAGE
                    
                    echo "Calculator container deployed successfully!"
                    echo "To interact with calculator, run: docker attach $CONTAINER_NAME"
                '''
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline completed successfully!'
            echo 'Calculator application is deployed and ready to use.'
        }
        failure {
            echo 'Pipeline failed. Please check the logs for errors.'
        }
        always {
            echo 'Cleaning up workspace...'
            cleanWs()
        }
    }
}

