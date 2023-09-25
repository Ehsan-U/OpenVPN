

variable "do_token" {
    type = string
}

output "ipv4" {
    value = digitalocean_droplet.vpn.ipv4_address
}