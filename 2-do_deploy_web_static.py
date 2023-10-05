#!/usr/bin/python3
"""Compress before sending"""
from fabric.api import local, env, put, run
from datetime import datetime
import os
import os.path as path

env.hosts = ['35.175.64.173', '54.158.205.17']
now = datetime.now()
dt_string = now.strftime("%Y%m%d%H%M%S")


def do_pack():
    """script that generates a .tgz archive"""
    try:
        local('mkdir -p versions/')
        filename = "web_static_" + dt_string + ".tgz"
        local('tar -cvzf versions/{} web_static/'.format(filename))
        path = './versions/{}'.format(filename)
        print("web_static packed: {} ->{}Bytes"
              .format(path, os.path.getsize(path)))
    except:
        return None


def do_deploy(archive_path):
    """deploy to server"""
    try:
        if not os.path.exists(archive_path):
            return False
        fn_with_ext = os.path.basename(archive_path)
        fn_no_ext, ext = os.path.splitext(fn_with_ext)
        dpath = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("rm -rf {}{}/".format(dpath, fn_no_ext))
        run("mkdir -p {}{}/".format(dpath, fn_no_ext))
        run("tar -xzf /tmp/{} -C {}{}/".format(fn_with_ext, dpath, fn_no_ext))
        run("rm /tmp/{}".format(fn_with_ext))
        run("mv {0}{1}/web_static/* {0}{1}/".format(dpath, fn_no_ext))
        run("rm -rf {}{}/web_static".format(dpath, fn_no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(dpath, fn_no_ext))
        print("New version deployed!")
        return True
    except Exception:
        return False
