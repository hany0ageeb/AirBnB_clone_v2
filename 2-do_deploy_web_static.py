#!/usr/bin/python3
"""
 Fabric script (based on the file 1-pack_web_static.py) that
 distributes an archive to your web servers
 Returns False if the file at the path archive_path doesn’t exist
"""
from fabric.api import *


env.hosts = ['100.26.241.78', '100.26.215.50']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """
    distributes an archive to your web servers
    """
    import os.path
    if not os.path.isfile(archive_path):
        return False
    result = put(archive_path, "/tmp/")
    remote_archive = "/tmp/" + os.path.basename(archive_path)
    if result.failed:
        return False
    dest_dir = "/data/web_static/releases/{}/".format(
        archive_path[:archive_path.rindex('.')])
    result = run("mkdir -p {}".format(dest_dir))
    if result.failed:
        return False
    result = sudo("tar -xzf {} -C {}".format(remote_archive, dest_dir))
    if result.failed:
        return False
    result = run("rm {}".format(remote_archive))
    ret_val = result.succeeded
    result = run("unlink /data/web_static/current")
    if ret_val and result.failed:
        ret_val = False
    result = run("ln -s {} /data/web_static/current".format(dest_dir))
    if ret_val and result.failed:
        ret_val = False
    return ret_val
