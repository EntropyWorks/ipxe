from . import app

### copy turns into a dict
_config = app.config.copy()
_media_server = _config.get('MEDIA_SERVER', 'NO_MEDIA_SERVER_PASSED')

kickstart_os_url = 'http://%s/ziggurat-rhel-7/os/7.1/x86_64' % _media_server

###
### lets rename to jpmc-mandatory and jpmc-current
###
kickstart_repo_urls = {
    'blended-ziggurat': 'http://%s/ziggurat-rhel-7/blended-ziggurat' % _media_server,
    'jpmc-lrh7-current': 'http://%s/ziggurat-rhel-7/jpmc-lrh7-current' % _media_server,
    'jpmc-lrh7-mandatory': 'http://%s/ziggurat-rhel-7/jpmc-lrh7-mandatory' % _media_server,
    'latest': 'http://%s/ziggurat-rhel-7/latest' % _media_server,
}

profiles = {}
states = []

DEFAULT_KICKSTART = {
    'boot_disk_a': 'sda',
    'boot_disk_b': 'sdb',
    'cloud_init': False,
    'disk_layout': 'physical_120',
    'efi': False,
    'hardware_type': 'physical',
    'os_url': kickstart_os_url,
    'repo_urls': kickstart_repo_urls,
    'root_password': '!!!',
}

default_kickstart = DEFAULT_KICKSTART
