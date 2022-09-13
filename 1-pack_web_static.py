#!/usr/bin/python3
"""
Script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """ Makes a packs """
    try:
        now = datetime.now()
        date_create = now.strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        do_tgz = "web_static_{}.tgz".format(date_create)
        local("tar -cvzf versions/{} web_static".format(do_tgz))
        return do_tgz
    except:
        return None
