# Setup OpenVPN using Terraform & Ansible on DigitalOcean

![DigitalOcean Logo](images/digitalocean-logo.png)
![Terraform Logo](images/terraform-logo.png)
![Ansible Logo](images/ansible-logo.png)
![OpenVPN Logo](images/openvpn-logo.png)

This project demonstrates how to set up an OpenVPN server on DigitalOcean using Terraform for infrastructure provisioning and Ansible for server configuration management. With this setup, you can easily create and manage your own private VPN server in the cloud.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Instructions](#instructions)
  - [1. Provision Infrastructure with Terraform](#1-provision-infrastructure-with-terraform)
  - [2. Configure OpenVPN with Ansible](#2-configure-openvpn-with-ansible)
  - [3. Connect to Your VPN](#3-connect-to-your-vpn)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Setting up a VPN server provides a secure way to access your private network resources from anywhere in the world. This project uses Terraform to create the necessary cloud infrastructure on DigitalOcean, including the server instance, and Ansible to automate the OpenVPN server configuration.

## Prerequisites

Before you begin, make sure you have the following prerequisites:

- DigitalOcean account with API access tokens.
- Terraform installed on your local machine.
- Ansible installed on your local machine.
- SSH key pair for secure server access.

## Instructions

Follow these steps to set up your OpenVPN server:

### 1. Provision Infrastructure with Terraform

Use Terraform to provision the required resources on DigitalOcean:

```bash
cd terraform/
terraform init
terraform apply
