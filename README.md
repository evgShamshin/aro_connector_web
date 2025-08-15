## "ARO Connector" Website
![This is an alt text.](https://github.com/evgShamshin/aro_connector_web/blob/master/aro_web/media/aro_app/image/CeilingByRoomWhite_32.svg "This is a sample image.")
![This is an alt text.](https://github.com/evgShamshin/aro_connector_web/blob/master/aro_web/media/aro_app/image/CherryPickerWhite_32.svg "This is a sample image.")
![This is an alt text.](https://github.com/evgShamshin/aro_connector_web/blob/master/aro_web/media/aro_app/image/ElementIndexerWhite_32.svg "This is a sample image.")
![This is an alt text.](https://github.com/evgShamshin/aro_connector_web/blob/master/aro_web/media/aro_app/image/FloorByRoomWhite_32.svg "This is a sample image.")
![This is an alt text.](https://github.com/evgShamshin/aro_connector_web/blob/master/aro_web/media/aro_app/image/LocationSitesExportWhite_32.svg "This is a sample image.")
![This is an alt text.](https://github.com/evgShamshin/aro_connector_web/blob/master/aro_web/media/aro_app/image/NotionSyncWhite_32.svg "This is a sample image.")
![This is an alt text.](https://github.com/evgShamshin/aro_connector_web/blob/master/aro_web/media/aro_app/image/RenameElementsWhite_32.svg "This is a sample image.")
![This is an alt text.](https://github.com/evgShamshin/aro_connector_web/blob/master/aro_web/media/aro_app/image/ReplaceDimsToAnnotateFamsWhite_32.svg "This is a sample image.")
![This is an alt text.](https://github.com/evgShamshin/aro_connector_web/blob/master/aro_web/media/aro_app/image/SetValueParameterByLinkElementWhite_32.svg "This is a sample image.")
![This is an alt text.](https://github.com/evgShamshin/aro_connector_web/blob/master/aro_web/media/aro_app/image/SlabEdgesByRoomWhite_32.svg "This is a sample image.")
![This is an alt text.](https://github.com/evgShamshin/aro_connector_web/blob/master/aro_web/media/aro_app/image/UnloaderWhite_32.svg "This is a sample image.")
![This is an alt text.](https://github.com/evgShamshin/aro_connector_web/blob/master/aro_web/media/aro_app/image/ViewExceptionKeysWhite_32.svg "This is a sample image.")
![This is an alt text.](https://github.com/evgShamshin/aro_connector_web/blob/master/aro_web/media/aro_app/image/WallsByRoomWhite_32.svg "This is a sample image.")
![This is an alt text.](https://github.com/evgShamshin/aro_connector_web/blob/master/aro_web/media/aro_app/image/FasadeUnfolderWhite_32.svg "This is a sample image.")
![This is an alt text.](https://github.com/evgShamshin/aro_connector_web/blob/master/aro_web/media/aro_app/image/SetParameterWhite_32.svg "This is a sample image.")

Website that hosts the ARO Connector plug-in commands for Autodesk Revit software.


## Technologies
*  Python
*  Django
*  PostgreSQL
*  Redis
*  OAuth

## Installation and launch
1. Clone the repository from https://github.com/evgShamshin/aro_web_connector
3. Open the project in any IDE. For example, PyCharm has a built-in terminal.
4. Download PostgreSQL - https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
5. Create database and restore from https://github.com/evgShamshin/aro_connector_web/blob/master/aro_web/db_dump.sql
6. Download Redis - https://cloud.redis.io/#/rlec-downloads
7. Create and activate a virtual environment:
```
python -m venv aro_venv
aro_venv/Scripts/activate
```
8. Create a .env file and set the environment variables:
```
DB_NAME=aro_web_db
DB_USER=aro
DB_PASSWORD=12345
DB_HOST=localhost
DB_PORT=5432
```
9. Install dependencies and apply migrations:
```
pip install -r requirements.txt
python manage.py migrate
```
10. Create a superuser:
```
python manage.py createsuperuser
```
11. Start Redis:
```
sudo service redis-server start
```
12. Run the server:
```
cd aro_web
python manage.py runserver
```
13. Open your browser and navigate to `http://localhost:8000`
