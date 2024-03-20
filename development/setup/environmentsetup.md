# Environment Setup Wiki
> Note, it was made using https://github.com/nbnw-org/docs/blob/main/writing/developmentdocs/generic_template.md

We noticed that there were problems in properly running amplify cli commands due to different dependencies. Due to this reason, we are maintaining this doc.

The purpose of this document is to streamline the process of environment setup for everyone.

## 0. Prerequisite knowledge/work done
1. You should have docker installed on your system.
2. You should have Visual Studio Code installed on your system
3. You should have Dev Container extension installed on Visual Studio Code. (https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

## 1. Prior Understanding
This section talks about some basic concepts involving containers, dev containers and paths. It does not dive deep into any topic but skims over them to give you a feel of what is happening when you follow the steps.

### 1.1 What is the problem?
Before starting to dive into concepts, lets understand the problem first. Everyone has different development environment and different dependencies installed in their system. e.g. You might have python3.8 installed as default while I might have python3.11 installed. Similarly, you might have different version of other dependencies installed for other packages as well. This, becomes a problem when working in a team as something that works for you will work for you but it might not work for me.

This, in general is a huge pain to solve. Even if you have multiple versions of dependencies installed, sometimes, things are not in our control, e.g. if a CLI tool is using a specific dependency as priority.

To solve this, containers are introduced.

## 1.2 Containers
Containers, in lay man terms is a PC within a PC. When you spin up new container, imagine you are spinning up a new pc with fresh dependencies that you specify.

This helps in creating "PC"'s that have same dependency and share it with everyone.

Again, this is lay mans Container (it is much more, feel free to dive deep).

## 1.3 Docker
Docker is a tool, that allows us to create containers. We define a `Dockerfile` where we write what dependencies we want the Container (aka PC) to come preinstalled with.

(Think how when you buy new mobile phones, it comes pre-installed with certain apps, this is similar.)

## 1.4 Dev Container
Docker container are PC but you just get a CLI with it (and you may get an editor as well, but that is not very good UX).

To solve this, VS Code introduced a way to use VS Code with Docker Containers.

This, is Dev Container. Dev Container simply allows you to connect to Docker Container and have a UI to code on.

## 2. Permissions
1. You need to have AWS CLI configured on your machine (i.e. logged into AWS CLI).
2. You should know where AWS Credentials reside in your machine. (for me, it is in /Users/sarveshbhatnagar/.aws folder)

## 3. Steps involved
### 3.1 Setup
1. Create a fresh folder where you will be doing nbnw's development work in (for Web Development) (e.g. Frontend website, backend website, etc). Assuming `nbnw` in this case.
2. Open `nbnw` with VS Code.
3. In `nbnw` create a folder called `.devcontainer` (notice the . before devcontainer, it specifies that it is a hidden folder)
4. In `.devcontainer` folder, create a file called `devcontainer.json`, lets leave it empty for now, we will come back to it later.
5. In `.devcontainer` folder, create a file called `Dockerfile`. (make sure it is exactly named as mentioned, no extension).


#### 3.1.1 `Dockerfile`
Inside this file paste the below

```
FROM --platform=linux/amd64 public.ecr.aws/amazonlinux/amazonlinux:2023

USER root

# Installing Python 3.11 for Amplify
RUN dnf install python3.11 python3.11-pip poppler-cpp-devel gcc gnulib gnulib-devel gcc-c++ python3.11-devel -y
RUN pip3.11 install --upgrade pip
RUN pip3.11 install boto3

RUN pip3 install awscli --upgrade --user

# Install Node.js
RUN yum install nodejs -y
RUN yum install npm -y
RUN yum install awscli -y

# Post AWS
RUN yum install yum-utils -y
RUN yum-config-manager --add-repo https://cli.github.com/packages/rpm/gh-cli.repo
RUN yum install gh -y

# Required for Amplify
ENV AWS_SDK_LOAD_CONFIG=1

# AMPLIFY 
RUN npm install -g @aws-amplify/cli
RUN npm install -g typescript
```

#### 3.1.2 `devcontainer.json`
In this file paste the below code - 
```
{
	"name": "NBNW Common workspace",
	"build": {
		"dockerfile": "Dockerfile"
	},
	"mounts": [
		{
			"source": "/Users/sarveshbhatnagar/.aws",
			"target": "/root/.aws",
			"type": "bind"
		}
	]
}
```

Notice that in `mounts>source` I have added `/Users/sarveshbhatnagar/.aws` for you, this will be different. Please find where your aws cli's file is present and add it there.

You will also have to make sure that you have logged in to use AWS CLI otherwise it won't work.

### 3.2 Opening Dev Container
Now that you have done the setup, to use it, you will need to open the workspace using dev container.

For Macbook - 
1. In visual studio code, press `shift + cmd + P` and type `Dev Containers`.
2. From the options, select something like open in dev container or Rebuild and Open in dev container.

For Windows - 
[KAMAL fill this part]

After this step, it will build dev container (it will take time for the first time as it is installing everything for the first time) but next time should be quicker.

### 3.3 Using Dev Container
Now, let's first login to github. You will always have to do this as I don't know where github stores the credential. [Please feel free to update the instructions here if you find that].

1. write `gh auth login`
2. Select default https login method, you will be given a code, copy it press enter and it will open github on browser.
3. Paste the code there and enter.
4. Once done, you will have github installed.

Now we need to pull the repository - 
1. Use command like - `gh repo clone nbnw-org/nbnw-react-frontend` (change it based on what repository you will be using)
2. If everything is properly installed, it should work and pull the repository for you.

Now let's try amplify pull.
1. Use command like - `amplify pull` and select `dev` environment if asked.
2. If it pulled successfully, it means that setup is done properly otherwise there are issues in `mount` for credentials.

## 4. Verifications
1. Check Github CLI is working
2. Check `amplify pull` is working.


## Document Change History
Sarvesh - First Version
