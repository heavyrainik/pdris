docker build -t python_app . - cборка
 docker run -p 5000:5000 -it python_app /bin/bash - запуск для дебага
docker run -p 5000:5000 -d python_app - запуск аля прод
docker tag python_app sobolevas/python_app - тегнул
docker push sobolevas/python_app - пуш в хаб
https://hub.docker.com/repository/docker/sobolevas/python_app - репо

