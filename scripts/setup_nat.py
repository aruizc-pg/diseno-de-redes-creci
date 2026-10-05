import boto3

def create_nat_gateway(subnet_id):
    ec2 = boto3.client('ec2')
    nat_gateway = ec2.create_nat_gateway(
        SubnetId=subnet_id,
        AllocationId='eipalloc-0123456789abcdef0'
    )
    return nat_gateway

if __name__ == '__main__':
    nat_gateway = create_nat_gateway('subnet-0123456789abcdef0')
    print(f"NAT Gateway created with ID: {nat_gateway['NatGateway']['NatGatewayId']}")