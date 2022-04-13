run:
	echo "Starting database"
	sudo docker-compose up -d postgres
	echo "Starting database GUI"
	sudo docker-compose up -d pgadmin

	sleep 5
	echo "Starting application"
	sudo docker-compose up -d app
	echo "Migrating models to database"
	sudo docker-compose exec app alembic upgrade head