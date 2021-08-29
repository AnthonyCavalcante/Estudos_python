all: run

BOT_SERVICE=bot.main

run: 
	docker-compose run --rm ${BOT_SERVICE} 

bash:
	docker-compose run --rm ${BOT_SERVICE} sh 

pip-install:
	docker-compose run --rm ${BOT_SERVICE} pip install -r requirements.txt

