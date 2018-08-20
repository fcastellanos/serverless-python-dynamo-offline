## Serverless with Python + DynamoDB offline

### Create
If you want to create a brand new serverless python 3 service you type...
```
$ serverless create --template aws-python3 --name myproject --path myproject
```

### Install
```
$ sls plugin install -n serverless-python-requirements
$ npm install --save serverless-dynamodb-local
$ sls dynamodb install
$ npm install serverless-offline-python --save-dev
```

### Deploy

```
export AWS_SDK_LOAD_CONFIG=1

sls deploy --aws-profile [aws profile]
```

### Offline mode

```
$ sls offline start
```

Then you can access DynamoDB web shell at http://localhost:8000/shell/

### Issues

At the time of this writing 08-20-2018 there's an issue with the `serverless-dynamodb-local` plugin with version `0.2.31`, seems like downgrading to `0.2.30` fixes the issue, refer to this [issue](https://github.com/99xt/serverless-dynamodb-local/issues/181) to see how to fix it.
