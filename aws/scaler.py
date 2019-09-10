# this is a POC and needs be properly written
import boto3
client = boto3.client('sqs')
queue_url = client.get_queue_url(
    QueueName='airflow-stage-Tasks-1SRC2B5YQV7KS',
)['QueueUrl']
# print(queue_url)
size = client.get_queue_attributes(
  AttributeNames=['ApproximateNumberOfMessages'],
  QueueUrl=queue_url
)['Attributes']['ApproximateNumberOfMessages']
# print(size)
size = int(size)
client = boto3.client('autoscaling')
response = client.describe_auto_scaling_groups(
    AutoScalingGroupNames=[
        'airflow-stage-worker-scaling-group',
    ],
)['AutoScalingGroups']
asg = response[0]
if size > asg['MaxSize']:
  size =  asg['MaxSize']

client.set_desired_capacity(
    AutoScalingGroupName='airflow-stage-worker-scaling-group',
    DesiredCapacity=size,
    HonorCooldown=False
)
