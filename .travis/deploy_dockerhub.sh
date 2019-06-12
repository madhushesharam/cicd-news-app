#!/bin/sh
docker login -u $DOCKER_USER -p $DOCKER_PASS
if [ "$TRAVIS_BRANCH" = "master" ]; then
    TAG="latest"
else
    TAG="$TRAVIS_BRANCH"
fi
echo "\n BEGIN  travis repo slug data \n "

echo "\n \n "
echo $TRAVIS_REPO_SLUG:$TAG

echo "\n END OF  travis repo slug data \n "

docker build -f Dockerfile -t $TRAVIS_REPO_SLUG:$TAG .
docker push $TRAVIS_REPO_SLUG:$TAG
