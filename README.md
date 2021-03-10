How To Use RabbitMQ + Celery + Docker ?
---

***Docker Version:*** 

   - Docker-compose : `docker-compose version 1.28.5, build c4eb3a1f`
   
   - Docker : `Docker version 20.10.5, build 55c4c88`

***clone repo:***

```sh
cd ~/ 
mkdir workspace && cd workspace
git clone https://github.com/Parham-sagharchi/rabbitmqCeleryDocker.git && cd rabbitmqCeleryDocker
```

***run:*** 

   - Run command `sudo docker-compose up`
     
   - Above command will start 1 container for each worker and rabbit
    
   - Now go inside one worker container
   
        ```sh
        docker ps -a # get "CONTAINER ID" of one worker.
        docker exec -it {CONTAINER ID} bash
        ```
     
   - run this command inside container
   
        ```sh
        python -m celery_main.task_submitter
        ```

   - this will start pushing tasks in rabitmq and workers.
   
***Speedup the process:***

   - To run 5 workers and 1 rabbitmq
    
        ```sh
           sudo docker-compose up --scale worker=5
        ```

   - Do not increase concurrency to too much in dockerfile as machine might not be able to handle it
    
        ```sh
           ENTRYPOINT celery -A test_celery worker --concurrency=10 --loglevel=INFO
        ```

***Management UI:***

   - Manage UI is accssible using `localhost:15672` or `http://:15672` i.e in my case it is `http://192.168.100.126:15672`. You can find docker ip using docker network inspect network_name.
   
        ```sh
           docker inspect --format='{{.Name}} {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps -q)
        ```
     
   - Hint 1: Go to `http://127.0.0.1:15672` with USERNAME & PASSWORD `PARHAM`.
   - Hint 2: you can change username, password and local ip in `.env`.
     
***Caution:***

   - this will delete all your containers, images and networks:
    
        ```sh
           docker stop $(docker ps -aq)
           docker rm $(docker ps -aq)
           docker network prune -f
           docker rmi -f $(docker images --filter dangling=true -qa)
           docker volume rm $(docker volume ls --filter dangling=true -q)
        ```
    
