


$directory = "."

$dockerfile_traffic = "dockerfile.traffic"
$dockerfile_challenge = "dockerfile.challenge"
$dockerfile_hospital = "dockerfile.hospital"

$image_traffic = "traffic"
$image_challenge = "challenge"
$image_hospital = "hospital"


docker build -f $dockerfile_traffic -t $image_traffic .

docker build -f $dockerfile_challenge -t $image_challenge .

docker build -f $dockerfile_hospital -t $image_hospital .

docker run  $image_traffic
docker run  $image_challenge
docker run  $image_hospital


Write-Host "All containers are up and running." -ForegroundColor Green
