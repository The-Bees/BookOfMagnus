Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.network :forwarded_port, guest: 8000, host: 4567
  config.vm.provision :shell, path: "config/vagrant_startup/startup.sh"

end
