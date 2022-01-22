# -*- coding: utf-8 -*-
import paramiko
import requests 
import json
import time
import signal
from getpass import getpass
from functools import wraps
import os

import errno


# 라즈베리파이 
HOST = "192.168.0.6"
TOR_PORT = "9050"
URL = f"{HOST}:{TOR_PORT}"

import time
import signal

def get_tor_session():
    session = requests.session()
    session.proxies = {
        'http' : f'socks5h://{URL}',
        'https' : f'socks5h://{URL}',
    }    
    return session

def get_rasberry_access(password):
    cli = paramiko.SSHClient()
    cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    cli.connect(HOST, port="22", username="pi", password=password)
    return cli

def main(connection):
    while(1):
        now = time.time()
        session = get_tor_session()
        connection.exec_command("sudo service tor reload")
        print("Current Ip : ", session.get("http://httpbin.org/ip").json()["origin"], "\t > takes", round(time.time() - now,3) , "sec")

password = getpass("라즈베리파이 루트 비밀번호 입력 : ")
connection = get_rasberry_access(password=password)
main(connection)