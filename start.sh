docker compose down
docker rmi -f $(docker images -aq)
cd flask_service_1/
docker build -t flask_service_1 .
cd ../flask_service_2/
docker build -t flask_service_2 .
cd ../flask_service_UI_standin/
docker build -t flask_service_ui_standin .
cd ../
docker-compose up -d