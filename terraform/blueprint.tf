resource "hyperfabric_fabric" "terraform_fabric" {
  name = "Terraform-Fabric"
  description = "Fabric created by Terraform"
}

resource "hyperfabric_node" "node1" {
  fabric_id  = hyperfabric_fabric.terraform_fabric.id
  name       = var.node1.name
  model_name = var.node1.model
  roles      = [var.node1.role]
}

resource "hyperfabric_node" "node2" {
  fabric_id  = hyperfabric_fabric.terraform_fabric.id
  name       = var.node2.name
  model_name = var.node2.model
  roles      = [var.node2.role]
}

resource "hyperfabric_node" "node3" {
  fabric_id  = hyperfabric_fabric.terraform_fabric.id
  name       = var.node3.name
  model_name = var.node3.model
  roles      = [var.node3.role]
}

resource "hyperfabric_node" "node4" {
  fabric_id  = hyperfabric_fabric.terraform_fabric.id
  name       = var.node4.name
  model_name = var.node4.model
  roles      = [var.node4.role]
}

resource "hyperfabric_node_management_port" "node1" {
  node_id          = hyperfabric_node.node1.id
  ipv4_config_type = "CONFIG_TYPE_STATIC"
  ipv4_address     = var.node1.mgmt
  ipv4_gateway     = "10.0.0.254"
  dns_addresses    = ["8.8.8.8", "1.1.1.1"]
  proxy_address    = "https://proxy.esl.cisco.com:80"
}

resource "hyperfabric_node_management_port" "node2" {
  node_id          = hyperfabric_node.node2.id
  ipv4_config_type = "CONFIG_TYPE_STATIC"
  ipv4_address     = var.node2.mgmt
  ipv4_gateway     = "10.0.0.254"
  dns_addresses    = ["8.8.8.8", "1.1.1.1"]
  proxy_address    = "https://proxy.esl.cisco.com:80"
}

resource "hyperfabric_node_management_port" "node3_mgmt" {
  node_id          = hyperfabric_node.node3.id
  ipv4_config_type = "CONFIG_TYPE_STATIC"
  ipv4_address     = var.node3.mgmt
  ipv4_gateway     = "10.0.0.254"
  dns_addresses    = ["8.8.8.8", "1.1.1.1"]
  proxy_address    = "https://proxy.esl.cisco.com:80"
}

resource "hyperfabric_node_management_port" "node4_mgmt" {
  node_id          = hyperfabric_node.node4.id
  ipv4_config_type = "CONFIG_TYPE_STATIC"
  ipv4_address     = var.node4.mgmt
  ipv4_gateway     = "10.0.0.254"
  dns_addresses    = ["8.8.8.8", "1.1.1.1"]
  proxy_address    = "https://proxy.esl.cisco.com:80"
}

resource "hyperfabric_connection" "spine1_leaf1" {
  fabric_id = hyperfabric_fabric.terraform_fabric.id
  local = {
    node_id   = hyperfabric_node.node1.node_id
    port_name = "Ethernet1_31"
  }
  remote = {
    node_id   = hyperfabric_node.node3.node_id
    port_name = "Ethernet1_31"
  }
  pluggable = "QDD-400-AOC3M"
}

resource "hyperfabric_connection" "spine1_leaf2" {
  fabric_id = hyperfabric_fabric.terraform_fabric.id
  local = {
    node_id   = hyperfabric_node.node1.node_id
    port_name = "Ethernet1_32"
  }
  remote = {
    node_id   = hyperfabric_node.node4.node_id
    port_name = "Ethernet1_31"
  }
  pluggable = "QDD-400-AOC3M"
}

resource "hyperfabric_connection" "spine2_leaf1" {
  fabric_id = hyperfabric_fabric.terraform_fabric.id
  local = {
    node_id   = hyperfabric_node.node2.node_id
    port_name = "Ethernet1_31"
  }
  remote = {
    node_id   = hyperfabric_node.node3.node_id
    port_name = "Ethernet1_32"
  }
  pluggable = "QDD-400-AOC3M"
}

resource "hyperfabric_connection" "spine2_leaf2" {
  fabric_id = hyperfabric_fabric.terraform_fabric.id
  local = {
    node_id   = hyperfabric_node.node2.node_id
    port_name = "Ethernet1_32"
  }
  remote = {
    node_id   = hyperfabric_node.node4.node_id
    port_name = "Ethernet1_32"
  }
  pluggable = "QDD-400-AOC3M"
}

resource "hyperfabric_vrf" "example_vrf" {
  fabric_id = hyperfabric_fabric.terraform_fabric.id
  name      = "Vrf-example"
}

resource "hyperfabric_vni" "net1" {
  fabric_id   = hyperfabric_fabric.terraform_fabric.id
  name        = "net1"
  svi = {
    enabled        = true
    ipv4_addresses = ["192.168.1.254/24"]
  }
}