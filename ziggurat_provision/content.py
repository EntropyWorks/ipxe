rhel71_os_base = "/ziggurat-rhel-7/os/7.1/x86_64"

rhel71_base_options = [
    'inst.text',
    'inst.geoloc=0',
    'ks.sendmac',
    'ks.device=bootif',

]

zg_hardware_profile = ""

dell_r630_bom1_config_a = {
    'zg_disk_layout': 'physical_120',
    'zg_boot_disk_a': '',
    'zg_boot_disk_b': '',
    'zg_hardware': '',
}

states = ('IN_USE', 'MAINTENANCE', 'REBUILD')

profiles = {
    "dell.r630.bom1.config_a": None,
    "dell.r630.bom2.config_a": None,
    "dell.r630.bom3.config_a": None,
    "dell.r730xd.bom1.config_a": None,
    "dell.r730xd.bom1.config_b": None,
    "hp.dl360.bom1.config_a": None,
    "hp.dl360.bom2.config_a": None,
    "hp.dl360.bom3.config_a": None,
}
