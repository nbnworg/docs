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

2. Go to domains->nbnw-domain
3. Choose Create repository.

4. In Repository name, enter repo-name

(Optional) In Repository Description, enter an optional description for your repository.

4. In Public upstream repositories, select npm-store to create a repository connected to npmjs that is upstream from your my-repo repository.

5. CodeArtifact assigns the name npm-store to this repository for you. All packages available in the upstream repository npm-store are also available to its downstream repository, repo-name.

6. Choose Next.

7. In AWS account, choose This AWS account.

8.

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
When you're ready, choose Create repository.
<br />
On the my-repo page, choose View connection instructions, and then choose npm.
<br />
Use the AWS CLI to run the login command shown under Configure your npm client using this AWS CLI CodeArtifact command.
<br />

```
aws codeartifact login --tool npm --repository nbnw-repo --domain nbnw-domain --domain-owner 215750026173 --region us-east-1
```

replace nbnw-repo with the name of your repo and replace 215750026173 with your 12 digit id

You should receive output confirming your login succeeded.

<br />
Successfully configured npm to use AWS CodeArtifact repository https://my-domain-111122223333.d.codeartifact.us-east-2.amazonaws.com/npm/my-repo/
<br />
Login expires in 12 hours at 2020-10-08 02:45:33-04:00
<br />

# Automate publishing of package to repo

1. Go to nbnworg and a create new repository their.
1. Go to github settings->secrets and variables->actions.
1. Set the variables like <br />
   AWS_REGION:us-east-1 <br />
   CODEARTIFACT_REPOSITORY:the name of your repo in codeartifact .<br />
   CODEARTIFACT_DOMAIN_OWNER :your 12-digit-id through which you log in to the console.<br />
   CODEARTIFACT_DOMAIN :the domain name .<br />
   AWS_ACCESS_KEY_ID : as provided to you .<br />
   AWS_SECRET_ACCESS_KEY : as provided to you .<br />
   Now create a folder **.github** in your project directory .inside it create a folder called **workflows** and inside create a file called publish.yml and copy paste the code provided below

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

Now create a package.json file <br />
Use the sample provided below :<br />

```
{
  "name": "nbnw-ui-constants",
  "version": "1.0.6",
  "main": "main.js",
  "types": "typeDeclaration.d.ts",
  "scripts": {
    "build": "tsc",
    "test": "jest"
  },
  "keywords": [],
  "author": "NBNW",
  "license": "MIT"
}

```

change the name of package to whatever name you like . Change the version to 1.0.0 and whenever you push changes to code update the version to 1.0.1 and on each subsequent update the version number should be changed to 1.0.2,1.0.3 and so on .The types field is used to specify the typedeclarations of functions ,objects,enums and interfaces if not provided error is thrown by typescript compiler .
Now create a main.js file beacuse it is the entry point for the package .<br />
The final export of code will be done from main.js file .Kindly check nbnw-ui-constants and nbnw-ui-components repo in nbnw org for better clarity.

# Updating the package
When you want to update your package i.e nbnw-ui-constant or nbnw-ui-components then you just need to make the changes that you required it can be change in categories, change in subcategories or some constants value and many more.
After this you will update the version of the current package in package.json
For Example:- If the current version of package is 1.0.6 and after you make changes it should become 1.0.7
After doing this you just need to create the PR. Once this PR is reviewed and merge into the main then github workflow have publish.yml file this is basically a scripting file which is responsible to compile, build and publish the updated package with the new version then you simply need to update your package whereever you are using it and you will be able to see the changes.