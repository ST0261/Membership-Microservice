echo "Checking if docker is installed"
if ! [ -x "$(command -v docker)" ]; then
    echo "Install and start docker"
    yum update -y
    yum install -y docker
    service docker start
    usermod -a -G docker ec2-user
    echo "Done..."
else
    echo 'Docker is installed'
fi

docker image build -t membership-img .

docker stop membership-container
docker rm membership-container

docker run -d --name membership-container -p 5000:5000 membership-img


