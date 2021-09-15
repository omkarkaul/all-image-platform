terraform {
    required_providers {
        aws = {
            source = "hashicorp/aws"
            version = "~> 3.27"
        }
    }

    required_version = ">= 0.14.9"

    backend "s3" {
        bucket = "all-image-bucket"
        key = "all_image-service.tfstate"
        region = "ap-southeast-2"
        dynamodb_table = "all-image-service-state-lock"
        encrypt = true
    }
}

provider "aws" {
    profile = "default"
    region = var.region
}

resource "aws_dynamodb_table" "terraform_state_lock" {
    name = "all-image-service-state-lock"
    billing_mode = "PAY_PER_REQUEST"
    hash_key = "LockID"

    attribute {
        name = "LockID"
        type = "S"
    }
}

resource "aws_instance" "app_server" {
    ami = "ami-04a9f190cb0fd4bad"
    instance_type = "t2.micro"
    key_name = "all-image"

    tags = {
        Name = var.instance_name
    }
} 