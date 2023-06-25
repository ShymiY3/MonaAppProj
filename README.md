# projekt
## Distributed system for monitoring network services in cooperation with Samsung

Authors:
Kinga Górska,
Mikołaj Grzempa,
Szymon Jański,
Wojtek Kostowski,
Janek Karczewicz,
Thang Cao.

## My part in this project

I was in a two members team responsible for backend. Additionaly I wrote telegraf, influx and grafana containers from scratch.

## About app
In this project server collect from users urls of pages to monitor. Agent via telegraf-container collects status codes of all sites and sends via telegraf metrics to InfluxDB. User can see theirs requests on site via Grafana dashboard.  

## Initial setup
Project build on python version 3.10, you need to install all requirements and edit files listed below \
don't forget about django migrate before runserver \
to generate INFLUXDB_AUTH_TOKEN use:
```
python MonaApps_Project\MonaApps\token_generator.py
```
to generate SECRET_KEY use:
```
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
  
* Files to edit:
  *  grafana-container\docker-compose.yml
  *  InfluxDB-container\Influx\api_keys.txt
  *  MonaApps_Project\Download_content\telegraf-container\docker-compose.yml
  *  MonaApps_Project\MonaApps_Project\.env
  *  MonaApps_Project\MonaApps_Project\settings.py
      * LINE ~93 - GRAFANA_IFRAME_LINK - link to dashboard
      * LINE ~150 - smtp server config (part is in .env)

 More info about INFLUXDB SETUP in:  *InfluxDB-container\readme.txt*
