#!/bin/bash
set -e  # 出错就退出
pip3 install -r requirements.txt
python3 manage.py collectstatic --noinput
python3 manage.py migrate