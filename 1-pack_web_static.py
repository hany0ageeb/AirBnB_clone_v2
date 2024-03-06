#!/usr/bin/python3
"""
 Fabric script that generates a .tgz archive from
 the contents of the web_static folder
 1. Prototype: def do_pack():
 2. All files in the folder web_static must be
 added to the final archive
 3. all archives must be stored in the folder versions
 (your function should create this folder if it doesn’t exist)
 4. The name of the archive created must be
 web_static_<year><month><day><hour><minute><second>.tgz
 5. The function do_pack must return the archive path
 if the archive has been correctly generated. Otherwise, it should return None
"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """
    generates a .tgz archive from the contents of the web_static folder
    """
    local("[ -d versions ] || mkdir versions")
    now = datetime.now()
    archive_path = "versions/web_static_{}.tgz".format(
            now.strftime('%y%m%d%H%M%S'))
    result = local("tar -cvzf  {} web_static".format(archive_path))
    if result.succeeded:
        return archive_path
