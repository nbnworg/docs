# Onboarding Guide for developers
This document aims to get you up and running when you are getting started to develop on nbnw.org. Please take all the training mentioned below regardless if you are aware about the topic or not.

## Tools
This section talks about the tools we use for developing nbnw.org. Please go to the mentioned link for learning about the topic.


### HTML and CSS [Must]
Before starting anything, this should be your first go to video where you get a brief of HTML and CSS. We assume that you know basics of HTML and CSS and this course is meant to be a refresher for the same. Watch it at 2x speed to make sure that each of your concepts are fresh. It should take about 5 hours to complete this course.


[HTML and CSS Crash Course](https://www.youtube.com/watch?v=hu-q2zYwEYs&list=PL4cUxeGkcC9ivBf_eKCPIAYXWzLlPAm6G)


### Tailwind CSS [Must]
This is important as you will be working mainly with Tailwind CSS when you will be updating the UI. We have observed that a lot of times if you don't have proper understanding of tailwind css or css in general, individuals tend to write redundant utility class just to make things work. This should be a good refresher about what exactly is tailwind css and some of the core concepts for the same.

[Tailwind CSS Playlist](https://www.youtube.com/playlist?list=PL4cUxeGkcC9gpXORlEHjc5bgnIi5HEGhw)

### Amplify Tutorial [Must]
We work with Amplify for both Frontend and Backend, to be able to work effectively you will need a brief about what amplify is and how we are using the same. To that end, please go through amplify docs and read each section once. (Make sure to read each section, for API you can skip graphql as we are using REST API!)

[Amplify Docs](https://docs.amplify.aws/gen1/react/start/getting-started/introduction/)

### AWS Tutorial [MUST]

[AWS Lambda Tutorial](https://www.youtube.com/watch?v=RtiWU1DrMaM)

[Dynamodb Tutorial](https://www.youtube.com/watch?v=2k2GINpO308)

[API Gateway Overview](https://www.youtube.com/watch?v=pgpWyn_6zlA)

[AWS S3 Overview](https://www.youtube.com/watch?v=WNmkgz9yOp0)

[AWS Cognito Overview](https://www.youtube.com/watch?v=QEGo6ZoN-ao)

### Git [Required!]

[Github Tutorial](https://www.youtube.com/watch?v=zTjRZNkhiEU)

[Github CLI](https://www.youtube.com/watch?v=BRAG1Kj4-Ss)


### React JS [Optional, if you already know~]

For React JS refresher, use the following - [React Course - Youtube](https://www.youtube.com/watch?v=Ke90Tje7VS0).

## Knowledge Transfers

### Must Watch

[Importance of Code Review](https://youtu.be/fLotOp2v8r8)

[Debug Session - How to debug](https://youtu.be/EMxJIj7HHcM)

[Finding NBNW Data Schema and how data flows](https://youtu.be/lLCAt1dUTMY)

### Optional

[Notification Service Deep Dive](https://youtu.be/eVJ_olhiTEk)

[Notification Service Demo](https://youtu.be/bX5_F75SkYM)

[End to End flow - onboarding to development](https://youtu.be/gOVUywvEDNc)

## Readouts

### Must Read
[Coding Practices at NBNW](https://github.com/nbnw-org/docs/blob/main/development/learning/codingPractices.md)

Note - for below, you will have to request for Access Key to your manager.
[Amplify CLI setup](https://github.com/nbnw-org/docs/blob/main/development/setup/amplifysetup.md)


## NBNW Website
Currently, NBNW website is using React.js framework for frontend, AWS Lambda as backend and Dynamodb + S3 as storage.

To get started, please install github cli. Once done, follow the below steps to get started!

1. Clone the repository and cd into the directory

```
gh repo clone nbnw-org/nbnw-react-frontend && cd nbnw-react-frontend
```

2. Install node packages

```
npm i
```


3. Do amplify pull [You should have amplify cli already setup!]

```
amplify pull
```

```
1. Select the authentication method you want to use: AWS profile
2. Please choose the profile you want to use: default
3. Which app are you working on? nbnwreactfrontend (NOTE the name of the app here)
4. Pick a backend environment: dev (NOTE That you have to select dev)
5. Choose your default editor: Visual Studio Code
6. Choose the type of app that you're building · javascript
7. What javascript framework are you using react
8. Source Directory Path:  src
9. Distribution Directory Path: dist (NOTE THAT WE CHANGED IT TO dist here)
10. Build Command:  npm run-script build
11. Start Command: npm run-script start
12. Do you plan on modifying this backend? Yes

```


4. Change to your feature branch `git branch yourfeature`
5. Switch branch `git switch yourfeature`
6. Run the application `npm run dev`
7. Make changes
8. Commit ON FEATURE BRANCH
9. Build and see if build works, `npm run build`
9. Create pull request `gh pr create`


## Editor Portal

Currently, Editor Portal Website is using React.js framework for frontend, AWS Lambda as backend and Dynamodb + S3 as storage.

To get started, please install github cli. Once done, follow the below steps to get started!

1. Clone the repository and cd into the directory

```
gh repo clone nbnw-org/nbnw-editor-final && cd nbnw-editor-final
```

2. Install node packages

```
npm i
```


3. Do amplify pull [You should have amplify cli already setup!]

```
amplify pull
```

```
1. Select the authentication method you want to use: AWS profile
2. Please choose the profile you want to use: default
3. Which app are you working on? nbnweditorfinal (NOTE the name of the app here)
4. Pick a backend environment: dev (NOTE That you have to select dev)
5. Choose your default editor: Visual Studio Code
6. Choose the type of app that you're building · javascript
7. What javascript framework are you using react
8. Source Directory Path:  src
9. Distribution Directory Path: dist (NOTE THAT WE CHANGED IT TO dist here)
10. Build Command:  npm run-script build
11. Start Command: npm run-script start
12. Do you plan on modifying this backend? Yes

```


4. Change to your feature branch `git branch yourfeature`
5. Switch branch `git switch yourfeature`
6. Run the application `npm run dev`
7. Make changes
8. Commit ON FEATURE BRANCH
9. Build and see if build works, `npm run build`
9. Create pull request `gh pr create`
