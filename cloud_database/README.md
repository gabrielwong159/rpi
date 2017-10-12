# Cloud Databases
Connecting to several online databases through Python. Can be useful for cross device communication.

## azure_sql
Accessing Azure hosted SQL server using PyODBC

### Installation
```
sudo apt-get install freetds-dev freetds-bin unixodbc-dev tdsodbc
pip install pyodbc
```

In ```/etc/odbcinst.ini```:
```
[FreeTDS]
Description=FreeTDS Driver
Driver=/usr/lib/arm-linux-gnueabihf/odbc/libtdsodbc.so
Setup=/usr/lib/arm-linux-gnueabihf/odbc/libtdsS.so
```
[Source](https://gist.github.com/rduplain/1293636)

## upload_ip
A combination of DHCP and school internet causes the IP address of the Raspberry Pi to change periodically. This script allows the Raspberry Pi to upload the IP addresses of all its network interfaces into Firebase, allowing me to ssh into it.

### Installation
```
pip install netifaces python-firebase
```
