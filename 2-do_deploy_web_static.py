#!/usr/bin/python3
"""
 Fabric script (based on the file 1-pack_web_static.py) that
 distributes an archive to your web servers
 Returns False if the file at the path archive_path doesn’t exist
"""
from fabric.api import *


env.hosts = ['100.26.215.50', '100.26.241.78']
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
    ret_val = result.succeeded
    dest_dir = "/data/web_static/releases/{}/".format(
        archive_path[:archive_path.rindex('.')])
    result = sudo("mkdir -p {}".format(dest_dir))
    if ret_val and result.failed:
        ret_val = False
    result = sudo("tar -xzf {} -C {}".format(remote_archive, dest_dir))
    if ret_val and result.failed:
        ret_val = False
    result = run("rm {}".format(remote_archive))
    if ret_val and result.failed:
        ret_val = False
    result = sudo("mv {}web_static/* {}".format(dest_dir, dest_dir))
    if ret_val and result.failed:
        ret_val = False
    result = sudo("rm -rf {}web_static/".format(dest_dir))
    if ret_val and result.failed:
        ret_val = False
    result = run("rm -rf /data/web_static/current")
    if ret_val and result.failed:
        ret_val = False
    if ret_val and result.failed:
        ret_val = False
    result = sudo("ln -s {} /data/web_static/current".format(dest_dir))
    if ret_val and result.failed:
        ret_val = False
    return ret_val
