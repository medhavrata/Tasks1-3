# To Fetch the meta-data of an AWS EC2 Instance
# SSH to the EC2 instance as this information is available to the OS only
# Run the below commands to fetch the meta-data


# To Fetch the meta-data

[ec2-user ~]$ curl http://169.254.169.254/latest/meta-data/

# To Fetch the meta-data for a particular attribute

[ec2-user ~]$ curl http://169.254.169.254/latest/meta-data/public-ipv4