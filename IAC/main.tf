

resource "digitalocean_ssh_key" "default" {
  name       = "sshkey"
  public_key = file("/home/hp/.ssh/id_ed25519.pub")
}

resource "digitalocean_droplet" "vpn" {
  image  = "ubuntu-20-04-x64"
  name   = "vpn-1"
  region = "blr1"
  size   = "s-1vcpu-1gb"
  ssh_keys = [digitalocean_ssh_key.default.fingerprint]
}