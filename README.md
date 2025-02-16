## How to run in local env
> You should intalled Docker/Docker Desktop first. If you install the docker extension in your VScode, things would be easier.

1. clone/pull the repo to a local address
2. If you have docker extension in your VScode:
  - open the file `docker-compose.yml`
  - click `Run Service` of the db service first, wait for several seconds, then click `Run Service` of the django service.
3. If you don't have docker extension in your VScode:
  - input `docker-compose up -d db` in your terminal first and wait for the message of the start of the Container dw_db, then input `docker-compose up -d django` in your terminal.
4. After tests, please don't forget to shut down the services by inputing command `docker-compose down -v` in your terminal. This command will deletec everything including all the data in the databases. Or you could just input `docker-compose down` to just shut shwon the docker without deleting anything.

If there is no error, you should see a composed container called **django** in your Docker Desktop. Just click the ports of the container **dw_django**, the local web should open directly.