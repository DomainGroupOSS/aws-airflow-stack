# Steps

```bash
export AIRFLOW_NAME=airflow-dataprod
export AWS_DEFAULT_REGION=ap-southeast-2
pipenv install awscli
# aws s3 mb s3://$AIRFLOW_NAME-deployments
# make deploy stack-name=$AIRFLOW_NAME
# aws deploy create-application --application-name $AIRFLOW_NAME-deployment-application
# aws deploy create-deployment-group --deployment-group-name $AIRFLOW_NAME-deployment-group --application-name $AIRFLOW_NAME-deployment-application


aws cloudformation create-stack --stack-name $AIRFLOW_NAME --template-body file://aws/cf.yml --capabilities CAPABILITY_IAM --parameters '
[
            {
              "ParameterKey": "KeyPair",
              "ParameterValue": "dataproduction-ap-southeast-2",
              "UsePreviousValue": true

            }
            ,{
              "ParameterKey": "DbMasterPassword",
              "ParameterValue": "cheneyBlob123",
              "UsePreviousValue": true

            }
          ]
' --tags '[
  {
    "Key": "Application",
    "Value": "Airflow"
  },{
    "Key": "Environment",
    "Value": "Staging"
  },{
    "Key": "Team",
    "Value": "Data Team"
  }
]'
# prod
aws cloudformation create-stack --stack-name $AIRFLOW_NAME --template-body file://aws/cf.yml --capabilities CAPABILITY_IAM --parameters '
[
            {
              "ParameterKey": "KeyPair",
              "ParameterValue": "dataproduction-ap-southeast-2",
              "UsePreviousValue": true
            },{
              "ParameterKey": "DbMasterPassword",
              "ParameterValue": "cheneyBlob456!!",
              "UsePreviousValue": true
            },{
              "ParameterKey": "VPC",
              "ParameterValue": "vpc-0a43d46c03c541975",
              "UsePreviousValue": true
            },{
              "ParameterKey": "VpcCidrBlock",
              "ParameterValue": "10.138.0.0/20",
              "UsePreviousValue": true
            },{
              "ParameterKey": "StackSubnet",
              "ParameterValue": "subnet-04310bfea2a0ed5f2",
              "UsePreviousValue": true
            },{
              "ParameterKey": "DBSubnets",
              "ParameterValue": "subnet-04310bfea2a0ed5f2,subnet-041b2df843e7d398c",
              "UsePreviousValue": true
            }
          ]
' --tags '[
  {
    "Key": "Application",
    "Value": "Airflow"
  },{
    "Key": "Environment",
    "Value": "Production"
  },{
    "Key": "Team",
    "Value": "Data Team"
  }
]'
------------------------------
aws cloudformation update-stack --stack-name $AIRFLOW_NAME --template-body file://aws/cf.yml --capabilities CAPABILITY_IAM --parameters '
[
            {
              "ParameterKey": "KeyPair",
              "UsePreviousValue": true

            }
            ,{
              "ParameterKey": "DbMasterPassword",
              "UsePreviousValue": true
            }
          ]
'

cd src
make deploy stack-name=$AIRFLOW_NAME

```


# Job queue message format

```json
{
  "body": "W1siYWlyZmxvdyBydW4gbXlfZGFnIHJ1bm1lXzQgMjAxOS0wMS0wMVQwMDowMDowMCswMDowMCAtLWxvY2FsIC1zZCAvYWlyZmxvdy9kYWdzL215X2RhZy5weSJdLCB7fSwgeyJjYWxsYmFja3MiOiBudWxsLCAiZXJyYmFja3MiOiBudWxsLCAiY2hhaW4iOiBudWxsLCAiY2hvcmQiOiBudWxsfV0=",
  "content-encoding": "utf-8",
  "content-type": "application/json",
  "headers": {
    "lang": "py",
    "task": "airflow.executors.celery_executor.execute_command",
    "id": "bf65caa0-bb1c-4f9a-bde7-4313d414d6ba",
    "shadow": null,
    "eta": null,
    "expires": null,
    "group": null,
    "retries": 0,
    "timelimit": [
      null,
      null
    ],
    "root_id": "bf65caa0-bb1c-4f9a-bde7-4313d414d6ba",
    "parent_id": null,
    "argsrepr": "['airflow run my_dag runme_4 2019-01-01T00:00:00+00:00 --local -sd /airflow/dags/my_dag.py']",
    "kwargsrepr": "{}",
    "origin": "gen13242@ip-10-138-40-125.ap-southeast-2.compute.internal"
  },
  "properties": {
    "correlation_id": "bf65caa0-bb1c-4f9a-bde7-4313d414d6ba",
    "reply_to": "af3091b5-7da5-37c0-8eb8-50037b4a88dc",
    "delivery_mode": 2,
    "delivery_info": {
      "exchange": "",
      "routing_key": "airflow-stage-Tasks-1SRC2B5YQV7KS"
    },
    "priority": 0,
    "body_encoding": "base64",
    "delivery_tag": "6a0c8de4-fe71-46a0-893d-9798b998580f"
  }
}


```
