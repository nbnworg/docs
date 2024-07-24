# Migrating categories and sub categories in a dynamodb table

This document aims to map the categories and subcategories of articles present in dynamodb table with new categories and sub categories (whenever necessary) .

## 0. Prerequisite knowledge/work done

1. Each table stores what kind of data and what interface is used to store the article .
2. Knowledge about how to create APIs using NodeJs and how do they work .

## 1. Prior Understanding

Some important points :

1. when to use different dynamodb commands like getcommand,scancommand,putcommand .what is event object and how to use it .
2. how to write parameters object to pass in these different commands.
3. how to use get,put,get,del command from aws-amplify/api library and how to pass query parameters.

## API permissions

currently the APi nbnwreactfrontend does not have permission to update articles in NBNWNewsTable so use the nbnweditorfinal api to update the items of this particular table.

**Functions used in backend**
<br />

```


async function listTechArticlesWithoutSubcategory(dynamodb, event) {

const category = event['category'];

const scan_params = {

TableName: process.env.STORAGE_NBNWNEWSTABLE_NAME,

FilterExpression:

'category = :category AND attribute_not_exists(subcategory)',

ExpressionAttributeValues: {

':category': category,

},

};

const data = await dynamodb.send(new ScanCommand(scan_params));

return data.Items;

}

```

<br />
This function, **listTechArticlesWithoutSubcategory**, is written in JavaScript and is designed to interact with an Amazon DynamoDB database. The function scans a DynamoDB table for items that belong to a specified category and do not have a subcategory attribute. Let's break down the function in detail.<br />

**Components Involved**

1. dynamodb: This is an instance of an AWS DynamoDB client. It is used to interact with the DynamoDB service to perform operations such as scans, queries, inserts, and deletes.

2. event: This object typically contains the input parameters passed to the function, often from an API request or another service. In this context, event includes a key category, which specifies the category of articles we want to filter.

**Scan parameters**

1. TableName: The name of the DynamoDB table to scan. It is retrieved from environment variables.
2. FilterExpression: This is a condition that each item in the table must meet to be included in the result. Here, it checks that the item's category attribute equals the specified category and that the subcategory attribute does not exist.
3. ExpressionAttributeValues: This maps the placeholder :category in the filter expression to the actual value of the category.

**Environment Variables**
<br />
process.env.STORAGE_NBNWNEWSTABLE_NAME: This is an environment variable that stores the name of the DynamoDB table. Environment variables are used to pass configuration settings and sensitive data (like database table names) without hardcoding them in the source code.
<br />
Change the scan parameters and environment variables in the function according to your project.

**Steps Involved**

1. Copy this function and paste it in "amplify/backend/function/src/path/{RESOURCE_NAME}/get.js" this directory and then export this function using module.exports={listTechArticlesWithoutSubcategory}
   <br />

2. in the file where you need this function import it using import {listTechArticlesWithoutSubcategory}=require("file_path") .

3. Run amplify push in the terminal to update the backend .

```
amplify push

```

<br />

```
async function updateCategory(dynamodb, event) {

console.log('Event is - ', event);

const newsId = event['id'];

const status = event['status'];

const update_params = {

TableName: process.env.STORAGE_NBNWNEWSTABLE_NAME,

Key: { id: newsId },

UpdateExpression: 'SET category = :val,subcategory= :val',

ExpressionAttributeValues: {

':val': status,

},

};

const data = await dynamodb.send(new UpdateCommand(update_params));

return data.Items;

}
```

<br />

**Explanation of the Function**
The updateCategory function is designed to update the category and subcategory attributes of a specific item in a DynamoDB table. The item's key is specified by the id provided in the event object.

**Update Parameters:**
TableName: The name of the DynamoDB table to update. It is retrieved from environment variables.<br />
Key: This specifies the primary key of the item to update. The key is an object with the id attribute set to newsId.<br />

UpdateExpression: This is an expression that defines how to update the item's attributes. Here, it sets both the category and subcategory attributes to the value of :val.<br />

ExpressionAttributeValues: This maps the placeholder :val in the update expression to the actual value of status.
<br />

Change the scan parameters and environment variables in the function according to your project.

**Steps Involved**

1. Copy this function and paste it in "amplify/backend/function/src/path/{RESOURCE_NAME}/put.js" this directory and then export this function using module.exports={updateCategory}
   <br />

2. in the file where you need this function import it using import {updateCategory}=require("file_path") .

3. Run amplify push in the terminal to update the backend .
   <br />

```
amplify push

```

**Functions used in Frontend**

**Explanation of the Function**
The retrieveApprovedNews function is an asynchronous function designed to fetch approved news articles from an API. It returns a promise that resolves to an array of PostFrontend objects or an unknown type in case of an error.

<br />

**Components Involved**

1. category: A constant string that specifies the category of news articles to retrieve, which in this case is set to 'Business'.
2. try-catch block: This is used to handle errors that might occur during the API call.

<br />
This makes an asynchronous get request to an API:
<br />
apiName: The base API name, specified by the constant BASEAPI.<br />
path: The specific path for the news endpoint, specified by the constant ApiPath.NEWS.<br />
options: An object containing query parameters for the API call:<br />
queryType: A constant QueryType.APPROVED that specifies the type of query, in this case, to retrieve approved news articles.<br />
category: The category of news articles, set to the previously declared constant category.<br />

**TypeScript Types**

1. PostFrontend: This is a TypeScript interface or type that represents the structure of the news articles returned by the API. It is not defined in the provided code but would typically include properties such as id, title, content, category, etc.
2. Promise<PostFrontend[] | unknown>: The function returns a promise that resolves to an array of PostFrontend objects or an unknown type in case of an error.

<br />

This makes an asynchronous get request to an API:

apiName: The base API name, specified by the constant BASEAPI.
path: The specific path for the news endpoint, specified by the constant ApiPath.NEWS.
options: An object containing query parameters for the API call:
queryType: A constant QueryType.APPROVED that specifies the type of query, in this case, to retrieve approved news articles.
category: The category of news articles, set to the previously declared constant category.

```

export async function retrieveApprovedNews(): Promise<

PostFrontend[] | unknown
{

const category = 'Business';

try {

const response = await get({

apiName: BASEAPI,

path: ApiPath.NEWS,

options: {

queryParams: {

queryType: QueryType.APPROVED,

category: category,

},

},

}).response;

return response.body.json().then((data) => {

return data;

});

} catch (error) {

console.error('Error retrieving news:', error);

throw error;

}

}

```

<br />

**Explanation of the Function**

The ChangeCategory function is an asynchronous function designed to update the category of a news article in an API. It returns a promise that resolves to a PostFrontend object or an unknown type in case of an error. <br />

**Components Involved**

id: A string parameter representing the unique identifier of the news article whose category is to be changed.<br />
category: A constant string that specifies the new category for the news article, which in this case is set to 'Business'.<br />
try-catch block: This is used to handle errors that might occur during the API call.<br />

This makes an asynchronous put request to an API:

1. apiName: The base API name, specified by the constant BASEAPI.
2. path: The specific path for the news endpoint, specified by the constant ApiPath.NEWS.
3. options: An object containing query parameters for the API call:
4. id: The unique identifier of the news article to update.
5. queryType: A constant QueryType.CHANGE that specifies the type of query, in this case, to change the category of the news article.
6. status: The new category for the news article, set to the previously declared constant category.

to use this function pass the id of article in it as parameter

```

export async function ChangeCategory(

id: string

): Promise<PostFrontend | unknown> {

const category = 'Business';

try {

const response = await put({

apiName: BASEAPI,

path: ApiPath.NEWS,

options: {

queryParams: {

id: id,

queryType: QueryType.CHANGE,

status: category,

},

},

}).response;

return response;

} catch (error) {

console.error('Error updating category: ', error);

throw error;

}
}

```
