variable "region" {
    description = "Region in which resources are deployed"
    type = string
    default = "ap-southeast-2"
}

variable "instance_name" {
    description = "Name of the EC2 instance in which the server lives"
    type = string
    default = "all-image-instance"
}