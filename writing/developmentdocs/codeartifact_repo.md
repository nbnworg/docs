# Prior Knowledge <br />

What are packages .

# Introduction to Codeartifact

AWS CodeArtifact is a secure , managed artifact repository service that helps organizations to store and share software packages for application development. we are using codeartifact with npm. CodeArtifact helps reduce the need for us to manage our own artifact storage system or worry about scaling its infrastructure. There are no limits on the number or total size of the packages that we can store in a CodeArtifact repository.
<br />
We can create a connection between our private CodeArtifact repository and an external, public repository, such as npmjs.com or Maven Central. CodeArtifact will then fetch and store packages on demand from the public repository when they're requested by a package manager. This makes it more convenient to consume open-source dependencies used by your application and helps ensure they're always available for builds and development. We can also publish private packages to a CodeArtifact repository. This helps us share proprietary software components between multiple applications and development teams in your organization.
<br />
CodeArtifact stores software packages in repositories. Repositories are polyglot—a single repository can contain packages of any supported type. Every CodeArtifact repository is a member of a single CodeArtifact domain .
<br />
CodeArtifact requires users to authenticate with the service in order to publish or consume package versions. You must authenticate to the CodeArtifact service by creating an authorization token using your AWS credentials. Packages in CodeArtifact repositories cannot be made publicly available.<br />

## 0. Domain

Repositories are aggregated into a higher-level entity known as a domain. All package assets and metadata are stored in the domain, but they are consumed through repositories. <br />
Each repository is a member of a single domain and can't be moved to a different domain.<br />

## 1.Repository

A CodeArtifact repository contains a set of package versions<br />

## 2. Upstream repository

<br />
One repository is upstream of another when the package versions in it can be accessed from the repository endpoint of the downstream repository. This approach effectively merges the contents of the two repositories from the point of view of a client. Using CodeArtifact, you can create an upstream relationship between two repositories.

# Permissions

Grant the IAM user access to CodeArtifact.<br />
Use the AWSCodeArtifactAdminAccess AWS managed policy. The following snippet shows the contents of this policy.<br />

```
{
   "Version": "2012-10-17",
   "Statement": [
      {
         "Action": [
            "codeartifact:*"
         ],
         "Effect": "Allow",
         "Resource": "*"
      },
      {
         "Effect": "Allow",
         "Action": "sts:GetServiceBearerToken",
         "Resource": "*",
            "Condition": {
               "StringEquals": {
                  "sts:AWSServiceName": "codeartifact.amazonaws.com"
               }
            }
      }
    ]
}
```

# Steps to create repository

1. Sign in to the AWS Management Console and open the AWS CodeArtifact console at https://console.aws.amazon.com/codesuite/codeartifact/start. For more information, see Setting up with AWS CodeArtifact.

2. Choose Create repository.

3. In Repository name, enter repo-name

(Optional) In Repository Description, enter an optional description for your repository.

4. In Public upstream repositories, select npm-store to create a repository connected to npmjs that is upstream from your my-repo repository.

5. CodeArtifact assigns the name npm-store to this repository for you. All packages available in the upstream repository npm-store are also available to its downstream repository, repo-name.

6. Choose Next.

7. In AWS account, choose This AWS account.

8. In Domain name, enter my-domain.

9. Expand Additional configuration.

10. You must use an AWS KMS key (KMS key) to encrypt all assets in your domain. You can use an AWS managed key or a KMS key that you manage:
    <br />
    Choose AWS managed key if you want to use the default AWS managed key.
    <br />
    Choose Customer managed key if you want to use a KMS key that you manage. To use a KMS key that you manage, in Customer managed key ARN, search for and choose the KMS key.
    <br />
    For more information, see AWS managed key and Customer managed key in the AWS Key Management Service Developer Guide.

11. Choose Next.

In Review and create, review what CodeArtifact is creating for you.
<br />
Package flow shows how my-domain, my-repo, and npm-store are related.
<br />
Step 1: Create repository shows details about my-repo and npm-store.
<br />
Step 2: Select domain shows details about my-domain.
<br />
When you're ready, choose Create repository.
<br />
On the my-repo page, choose View connection instructions, and then choose npm.
<br />
Use the AWS CLI to run the login command shown under Configure your npm client using this AWS CLI CodeArtifact command.
<br />

aws codeartifact login --tool npm --repository my-repo --domain my-domain --domain-owner 111122223333
You should receive output confirming your login succeeded.

<br />
Successfully configured npm to use AWS CodeArtifact repository https://my-domain-111122223333.d.codeartifact.us-east-2.amazonaws.com/npm/my-repo/
<br />
Login expires in 12 hours at 2020-10-08 02:45:33-04:00
<br />

# Automate publishing of package to repo

1. Go to github settings->secrets and variables->actions and set the variables like AWS_ACCESS_KEY_ID,AWS_REGION,AWS_SECRET_ACCESS_KEY ,CODEARTIFACT_DOMAIN, CODEARTIFACT_DOMAIN_OWNER , CODEARTIFACT_REPOSITORY .
   Using publish.yml file for publishing of package

```

name: Publish to CodeArtifact

on:
  push:
    branches:
      - main
    paths-ignore:
      - 'README.md'
jobs:
  publish:
    runs-on: windows-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v1
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ${{ secrets.AWS_REGION }}

      - name: Login to CodeArtifact
        run: |
          aws codeartifact login --tool npm --repository ${{ secrets.CODEARTIFACT_REPOSITORY }} --domain ${{ secrets.CODEARTIFACT_DOMAIN }} --domain-owner ${{ secrets.CODEARTIFACT_DOMAIN_OWNER }} --region ${{ secrets.AWS_REGION }}

      - name: Install npm dependencies
        run: npm install

      - name: Build the package
        run: npm run build

      - name: Publish to CodeArtifact
        run: npm publish

```

<br />
The provided YAML file is a GitHub Actions workflow configuration that automates the process of publishing an npm package to AWS CodeArtifact. Let's break down each section to understand how it works.<br />
Overview
<br />
The workflow is triggered whenever there is a push to the main branch, except when only the README.md file is modified. It runs on a Windows environment and performs the following steps:
<br />
Checks out the code.<br />
Configures AWS credentials.<br />
Logs in to AWS CodeArtifact.<br />
Installs npm dependencies.<br />
Builds the npm package.<br />
Publishes the package to AWS CodeArtifact.<br />
