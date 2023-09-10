# Docker
```
unzip FlowerShop.zip
cd FlowerShop
sudo docker build -t flower_shop .
sudo docker run -it --rm -p 5000:80 -d flower_shop
```
You should now be able to go to http://localhost:5000 and see the web app.