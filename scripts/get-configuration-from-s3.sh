# Grab configuration bucket name
BUCKET=$(aws --region=us-east-1 ssm get-parameter --name "GlobalConfigurationBucket" --with-decryption --output text --query Parameter.Value)

# All the configuration we need is under the folder "serverless"
KEY="serverless"

# Target directory should be the one who contains the serverless.yml (serverless.yml will refer to those files)
# The scripts works under the assumption we have COPY_TO defined as environment variable
FROM="s3://$BUCKET/$KEY/"
TO="../$COPY_TO"

# Copy all the files under the key path into the application folder
aws s3 cp $FROM $TO --recursive