import boto3

# Initialize the ELB client
elbv2 = boto3.client('elbv2', region_name='us-west-1')  # Replace with your desired region

# Specify the ALB configuration
alb_name = 'MyALB'  # Replace with your desired ALB name
subnets = ['subnet-xxxxxxxxxx', 'subnet-yyyyyyyyyy']  # Replace with your desired subnet IDs
security_groups = ['sg-0123456789abcdef0']  # Replace with your desired security group IDs

# Create the ALB
alb = elbv2.create_load_balancer(
    Name=alb_name,
    Subnets=subnets,
    SecurityGroups=security_groups,
    Scheme='internet-facing',  # Set to 'internal' for internal ALB
    Tags=[
        {
            'Key': 'Name',
            'Value': alb_name
        }
    ]
)

print(f"ALB created: {alb['LoadBalancers'][0]['LoadBalancerName']}")