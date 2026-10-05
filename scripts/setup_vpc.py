import os
import boto3
import yaml

_CONFIG_PATH = os.path.join(os.path.dirname(__file__), '..', 'config', 'vpc_config.yaml')

with open(_CONFIG_PATH, 'r', encoding='utf-8') as _f:
    _config = yaml.safe_load(_f)

VPC = _config['VPC']
Subnets = _config['Subnets']

def create_vpc():
    ec2 = boto3.client('ec2')
    vpc = ec2.create_vpc(CidrBlock=VPC['CidrBlock'])
    ec2.modify_vpc_attribute(VpcId=vpc['Vpc']['VpcId'], EnableDnsSupport={'Value': True})
    ec2.modify_vpc_attribute(VpcId=vpc['Vpc']['VpcId'], EnableDnsHostnames={'Value': True})
    return vpc

def create_subnets(vpc_id):
    ec2 = boto3.client('ec2')
    subnets = []
    for subnet in Subnets:
        subnet_response = ec2.create_subnet(
            VpcId=vpc_id,
            CidrBlock=subnet['CidrBlock'],
            AvailabilityZone=subnet['AvailabilityZone']
        )
        subnets.append(subnet_response)
    return subnets

if __name__ == '__main__':
    vpc = create_vpc()
    print(f"VPC created with ID: {vpc['Vpc']['VpcId']}")
    subnets = create_subnets(vpc['Vpc']['VpcId'])
    for subnet in subnets:
        print(f"Subnet created with ID: {subnet['Subnet']['SubnetId']}")