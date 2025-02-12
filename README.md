## How to run in local env
> You should intalled Docker/Docker Desktop first. If you install the docker extension in your VScode, things would be easier.

1. clone/pull the repo to a local address
2. If you have docker extension in your VScode:
  - open the file `docker-compose.yml`
  - click the `Run All Services` under the first sentence.
3. If you don't have docker extension in your VScode:
  - input `docker-compose up` in your terminal

If there is no error, you should see a composed container called **django** in your Docker Desktop. Just click the ports of the container **dw_django**, the local web should open directly.