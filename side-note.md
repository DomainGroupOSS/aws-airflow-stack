# Steps

```bash
export AIRFLOW_NAME=airflow-dataprod
export AWS_DEFAULT_REGION=ap-southeast-2
pipenv install awscli
# aws s3 mb s3://$AIRFLOW_NAME-deployments
# make deploy stack-name=$AIRFLOW_NAME
# aws deploy create-application --application-name $AIRFLOW_NAME-deployment-application
# aws deploy create-deployment-group --deployment-group-name $AIRFLOW_NAME-deployment-group --application-name $AIRFLOW_NAME-deployment-application


aws cloudformation create-stack --stack-name $AIRFLOW_NAME --template-body file://aws/cloud-formation-template.yml --capabilities CAPABILITY_IAM --parameters '
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
'
make deploy stack-name=$AIRFLOW_NAME

```

```bash
docker run -it --rm -u 0:0 node:8.9.4-alpine 'npm -g'



```
