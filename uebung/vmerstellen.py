import boto3

# Erstelle ein EC2-Client-Objekt
ec2 = boto3.client('ec2')

# Erstellen der EC2-Instanz
response = ec2.run_instances(
    ImageId='ami-0182f373e66f89c85',  # Beispiel-AMI-ID (Ubuntu)
    InstanceType='t2.micro',          # Instanztyp (z.B. t2.micro für die kostenlose Stufe)
    MinCount=1,                       # Minimale Anzahl an Instanzen
    MaxCount=1,                       # Maximale Anzahl an Instanzen
    KeyName='vockey',            # Name des SSH-Schlüsselpaares
    SecurityGroupIds=['sg-0bfe77ab3f5cfa930'],  # Sicherheitsgruppe
    SubnetId='subnet-0e3422e72361733f'
             '8',        # Subnet-ID
)

# Ausgabe der ID der neu erstellten Instanz
instance_id = response['Instances'][0]['InstanceId']
print(f"EC2-Instanz {instance_id} wurde erstellt.")