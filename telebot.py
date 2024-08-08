[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "pyTelegramBotAPI"
version = "4.22.0"
description = "Python Telegram bot api."
authors = [{name = "eternnoir", email = "eternnoir@gmail.com"}]
license = {text = "GPL2"}
readme = "README.md"
requires-python = ">=3.8"
keywords = ["telegram", "bot", "api", "tools"]
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Environment :: Console",
    "License :: OSI Approved :: GNU General Public License v2 (GPLv2)"
]
dependencies = ["requests"]

[project.urls]
Homepage = "https://github.com/eternnoir/pyTelegramBotAPI"
Documentation = "https://pytba.readthedocs.org"
Repository = "https://github.com/eternnoir/pyTelegramBotAPI"
Issues = "https://github.com/eternnoir/pyTelegramBotAPI/issues"


[project.optional-dependencies]
json = ["ujson"]
PIL = ["Pillow"]
redis = ["redis>=3.4.1"]
aioredis = ["aioredis"]
aiohttp = ["aiohttp"]
fastapi = ["fastapi"]
uvicorn = ["uvicorn"]
psutil = ["psutil"]
coloredlogs = ["coloredlogs"]
watchdog = ["watchdog"]


[tool.hatch.build.targets.wheel]
include = ["telebot/*"]
