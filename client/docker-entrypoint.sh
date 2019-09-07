#!/bin/sh

echo SERVER_HOST=$SERVER_HOST

python3.7 client.py --host $SERVER_HOST
