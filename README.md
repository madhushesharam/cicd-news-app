# cicd-sample app

[![Build Status](https://travis-ci.org/madhushesharam/cicd-news-app.svg)](https://travis-ci.org/madhushesharam/cicd-news-app)


Sample APP Running at 
https://radiant-ridge-25486.herokuapp.com/

### Continuous Integration and Continuous Deployment, or CI/CD, pipeline:
   
   1) Write a little Python APP
   2) Add  automated tests 
   3) Push  code to GitHub
   4) Setup Travis CI to continuously tests
   5) Create a Docker image for the  app
   6) Containerize your web app with docker
   7) Deploy to Docker Hub
   8) In Travis Set 
         '''-Environment Variables''' 
         -DOCKER_EMAIL  
         -DOCKER_PASS  
          DOCKER_USER  
 

    9) Push the Docker image to Docker Hub
   10) Deploy the Docker image to Heroku (Part of Delivery )

   ## heroku Deployment
      heroku login
      heroku create
      Creating app… done, ⬢ fXXXXNAME
      https://XXXNAMEherokuapp.com/ | https://git.heroku.com/fXXXXX.git
      heroku plugins:install @heroku-cli/plugin-container-registry
      heroku container:login
      heroku container:push web
      heroku container:release web

   To automate the process of deploying each build of master branch of  project, is taken care by  file  ‘deploy_heroku.sh’ in the directory ‘.travis’:

   Heroku API key u The Heroku App name Need to be added in Travis
   HEROKU_API_KEY  
   HEROKU_APP_NAME  






## Built With
   1) Python/Flask
   2) Travis CI
   3) Docker
   4) Heroku
   


