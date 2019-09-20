# this is a POC and needs be properly written
import boto3
def lambda_handler(event, context): 
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
  best_size = int(size)//3
  client = boto3.client('autoscaling')
  response = client.describe_auto_scaling_groups(
      AutoScalingGroupNames=[
          'airflow-stage-worker-scaling-group',
      ],
  )['AutoScalingGroups']
  asg = response[0]
  if best_size > int(asg['MaxSize']):
    best_size =  int(asg['MaxSize'])
  current_size = int(asg['DesiredCapacity'])
  if best_size != 0 and best_size < current_size: # need to scale in
    if current_size - best_size < 2: # only scale in more than 1 instance. This is to make the  scale down more stable
      print("Won't scale in simply for one instances. Current:", asg['DesiredCapacity'], "Desired:", size)
      return {}
  print("Adjusting desired ASG size to: ", best_size)
  client.set_desired_capacity(
      AutoScalingGroupName='airflow-stage-worker-scaling-group',
      DesiredCapacity=best_size,
      HonorCooldown=False
  )
  return {}
