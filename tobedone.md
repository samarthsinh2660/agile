1. create a git repo for an online food ordering application crreate a feature branch named feature add a cart realted funtion commit it and give me the cmd to checck the online git log 

2. create gitaction workflow that is triggered by a push to main rbanch and runs a python file contain basic order total calculation display the workflow result 

3. prepare docker for a given python based food ordering application build an image run the container with prot mapping and give the docker cmd to monitor 

4. given pthion funtion that claculation an order total far applying dicousnt write leastt four pytest cases for normal zero invalid  discount boundry input and use parametrization and assetion       

5. write seelenium for login with valid and invaldi cred 




Docker (build + run in one cmd)
docker build -t food-ordering-app . && docker run -d --name food-app -p 5000:5000 food-ordering-app


docker ps                       
docker logs -f food-app         
         
docker top food-app              

docker stop food-app && docker rm food-app  

venv/bin/pytest tests/test_order_total.py -v

Selenium 

.venv/bin/pytest tests/test_login_selenium.py -v
BASE_URL=http://localhost:5000 .venv/bin/pytest tests/test_login_selenium.py -v


