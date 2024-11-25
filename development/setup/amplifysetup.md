# Setting Up CLI:

## To set up the Amplify CLI, follow these steps:
### 1.Install the Amplify CLI:
Open a terminal window and run the following command:

npm install -g @aws-amplify/cli

### 2.Configure Amplify:

For the configuration of the amplify you need to first accept the invitation that you will recevied onto your mail from the administrator. You need to have an authenticator pre installed into your mobile as it will be required once once.

After accepting the invitation you will be redirected to your AWS access portal in case if you don't then you can also open that from the Access Portal URL that will be present in your mail recevied.

Once you open the portal you can see aws account assigned to you mostly it will be (sarvesh-bhatnagar) or (NBNW_Old_Permissions). You need to click on the access keys then choose your operating system and follow the steps mentioned

  

As a first step you need to configure AWS CLI by setting up the AWS IAM Identity Center Credentials and for that there is command mentiond `aws configure sso` Once you excute this command on terminal it will ask for following things:-

- SSO session name (Recommended): NBNW
- SSO start URL [None]: https://d-9067f4a8a8.awsapps.com/start/#
- SSO region [None]: us-east-1
- SSO registration scopes [sso:account:access]: (Enter)

After this SSO Authorization page will open in your default browser you just need to accept that after that move back to terminal and continue the process:

- There are 2 AWS accounts available to you. Choose the accound of Sarvesh Bhatnagar
- Using the account ID 747136956388
- The only role available to you is: NBNW_Old_permissions (Enter)
- Using the role name "NBNW_Old_permissions"
- CLI default client Region [us-east-1]: (Enter)
- CLI default output format [None]: json
- CLI profile name [NBNW_Old_permissions-747136956388]: (Enter)

After completing the above steps run the command `aws configure list-profiles` to see your recent profile created. If you can see NBNW_Old_permissions-747136956388 then you have successfully created the profile for further use.

Now you need to open the .aws folder into your VSCode or any editor you are using and in that file you need to modify the config file. You need to paste `credential_process = aws configure export-credentials --profile NBNW_Old_permissions-747136956388` just after the output = json line. Following is just an example how your config file will look like

    [default]
	region=us-east-1
	
	[profile NBNW_Old_permissions-747136956388]
	sso_session = test
	sso_account_id = 747136956388
	sso_role_name = NBNW_Old_permissions
	region = us-east-1
	output = json
	credential_process = aws configure export-credentials --profile NBNW_Old_permissions-747136956388
	
	[sso-session NBNWOld]
	sso_start_url = https://d-9067f4a8a8.awsapps.com/start/#
	sso_region = us-east-1
	sso_registration_scopes = sso:account:access

This is all you need to setup Amplify CLI for further use now you can follow the steps how to pull the amplify changes into your repo from the onboarding documentation

An important point to note here is that you always need to login amplify whenever your are pulling changes from amplify or pushing changes from amplify and for that you need to execute the command  `aws sso login --profile NBNW_Old_permissions-747136956388` after this only you can work with the amplify and it get auto expired after 12 hours


# Setting Up a New Project:
## To initialize a new project with Amplify, follow these steps:

### 1.Navigate to Your Project Directory:
Open a terminal and navigate to your desired project directory.

### 2.Initialize a New Amplify Project:
Run the following command:

amplify init
Follow the prompts to choose a project type (e.g., web app) and configure authentication settings if applicable.

### 3.Define Your App Structure:
Amplify uses a directory structure to manage your project. It creates essential folders for your backend (API), frontend (client), and cloud resources.

### 4.Configure Your Backend (API):
Use the Amplify CLI to define your backend schema:

amplify add schema

### 5.Configure Authentication (Optional):
If your app requires user authentication, integrate a suitable service using:

amplify add auth
Choose your preferred authentication method (e.g., Cognito) and configure its settings.

### 6.Develop Your Frontend:
Amplify generates a basic frontend application based on your chosen framework (e.g., React, Vue.js). Customize and build upon this foundation to implement your app's functionalities.

### 7.Connect Frontend and Backend:
Use Amplify libraries to connect your frontend code to your backend API. Integrate these libraries and configure them to interact with your data models seamlessly.

### 8.Push Your App to the Cloud:
Once your app is ready, provision and deploy your backend and frontend resources to the cloud:

amplify push

### 9.Test and Access Your App:
After successful deployment, Amplify provides you with the URL to access your hosted application. Test its functionality to ensure everything works as expected.

# Setting Up an Existing Project:
To set up Amplify in an existing project, you need to navigate to your project directory in the terminal and run the following commands:

## 1.Pull the Backend Environment:

amplify pull

Select the authentication method you want to use (e.g., AWS profile) and choose the appropriate profile. Follow the prompts to select your app name and specify project details like the JavaScript framework you're using, source directory path, distribution directory path, build command, and start command.

## 2.Configure Authentication (Optional):
If authentication is required, you can add it using:

amplify add auth
Choose your preferred authentication method and configure its settings.

## 3.Develop Your Frontend:
Continue developing your frontend as needed.

## 4.Connect Frontend and Backend:
Integrate Amplify libraries to connect your frontend code to your backend API.

## 5.Push Your App to the Cloud:
After making necessary changes, push your app to the cloud:
amplify push

## 6.Test and Access Your App:
Once deployment is successful, test your application's functionality and access it using the provided URL.

**refer the official Amplify documentation for detailed instructions and advanced configuration options.**
