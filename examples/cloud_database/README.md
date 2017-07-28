## azure_sql
Accessing Azure hosted SQL server using PyODBC

#### Installation
```sudo apt-get install freetds-dev freetds-bin unixodbc-dev tdsodbc
pip install pyodbc```

In ```/etc/odbcinst.ini```:
```[FreeTDS]
Description=FreeTDS Driver
Driver=/usr/lib/arm-linux-gnueabihf/odbc/libtdsodbc.so
Setup=/usr/lib/arm-linux-gnueabihf/odbc/libtdsS.so```
[Source](https://gist.github.com/rduplain/1293636)

## upload_ip
Uploads IP addresses of all network interfaces into Firebase

#### Installation
```pip install netifaces python-firebase```