# 自己写的配置文件，管的是"测试跑的时候用什么参数"
import os

ENV = os.getenv("ENV", "test")

ENVIRONMENTS = {
    "dev": "https://dev.example.com",
    "test": "https://www.saucedemo.com",
    "prod": "https://www.saucedemo.com",
}

BASE_URL = ENVIRONMENTS.get(ENV, ENVIRONMENTS["test"])
