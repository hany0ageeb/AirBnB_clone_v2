#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to your web servers,
using  the function deploy
"""
from fabric.api import *


env.hosts = ['100.26.215.50', '100.26.241.78']
env.user = 'ubuntu'
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


def deploy():
    """
    creates and distributes an archive
    """
    created_archive_path = do_pack()
    if created_archive_path:
        return do_deploy(created_archive_path)
    else:
        return False
