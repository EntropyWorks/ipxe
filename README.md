kickstart |

boot_disk_a:
boot_disk_b:
cloud_init: true|false
disk_layout:
efi: true|false
hardware_type: kvm|physical|vmware
os_url -> the url to the base path containing os media
repo_urls -> the repository urls to render
  name: blended-ziggurat, baseurl
  name: jpmc-lrh7-current, baseurl
  name: jpmc-lrh7-mandatory, baseurl
  name: latest, baseurl
root_password -> sha512 hashed password string

profiles ->
  name -> copy kickstart_default

profile.get(name, kickstart_default)
