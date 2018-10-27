# Notes and scripts to demo Rabbitmq and Hashicorp Vault 
## Context

- [RabbitMQ](https://www.rabbitmq.com/) is an open source message broker software implementing several message queuing protocols: AMQP, STOMP, MQTT, etc.

- [Hashicorp Vault](https://www.vaultproject.io/) is an open source tool for managing secrets.

## Content

This repo contains some notes demo Vault with a RabbitMQ setup:

It also contains two simple Python scripts to interact with the RabbitMQ broker with simple messages

- Publisher.py
- Consumer.py

## Demo set up

### Requirements

Carry out this demo on an Ubuntu 18.04 box with the Pika library (Python3) and with the RabbitMQ server running:

- sudo apt-get install rabbitmq-server
- sudo apt-get install python3-amqp 
- sudo apt-get install python3-pika python3-pika-pool

### RabbitMQ server

Check that the rabbitmq server is running:

Enable the RabbitMQ management plugin:

- sudo rabbitmq-plugins enable rabbitmq_management

### Vault

This demo assumes you have vault up and running. If you need help deployin Vault, check https://learn.hashicorp.com/vault/getting-started/deploy.

- vault secrets enable rabbitmq

Now, vault needs to know the credentials to communicate with RabbitMQ. By default are guest/guest, but use yours.

- vault write rabbitmq/config/connection connection_uri="http://localhost:15672" username="guest" password="guest"

And finally configure a role that maps a name in Vault to virtual host permissions.

- vault write rabbitmq/roles/my-role vhosts='{"/":{"write": ".*", "read": ".*"}}'

Done!

## Demo

### Generating credentials:

- vault read rabbitmq/creds/my-role

```css
your_user@your_hostname:~/$ vault read rabbitmq/creds/my-role
Key                Value
---                -----
lease_id           rabbitmq/creds/my-role/84d86cc4-8503-6ccf-9de2-b40xxxxedbfe
lease_duration     768h
lease_renewable    true
password           0c895f65-58b0-3bf0-cc56-f09xxxx05b32
username           root-3ecb4570-0387-269f-1895-55c2decb6cef 
```

Listing the RabbitMQ users:

```css
your_user@your_hostname:~/$ sudo rabbitmqctl list_users
Listing users ...
admin	[administrator]
root-3ecb4570-0387-269f-1895-55c2decb6cef       []
```
### Revoking credentials:


## Messaging

## Troubleshooting:

If you try to config vault using the port 5672 you might get this error:
failed to validate the connection: Get http://localhost:5672/api/users/: net/http: HTTP/1.x transport connection broken: malformed HTTP response "AMQP\x00\x00\t\x01"

The Port 5672 is used by AMQP 0-9-1 and 1.0, not the HTTP API. In order to communicate with the HTTP API use the port 15672 and the plugin rabbitmqadmin.
## Addittional resources
