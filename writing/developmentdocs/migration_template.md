# Migrating categories and sub categories in a dynamodb table

This document aims to map the categories and subcategories of articles present in dynamodb table with new categories and sub categories (whenever necessary) .

## 0. Prerequisite knowledge/work done

1. Each table stores what kind of data and what interface is used to store the article .
2. Knowledge about how to create APIs using NodeJs and how do they work .

## 1. Prior Understanding

Some important points :

1. when to use different dynamodb commands like getcommand,scancommand,putcommand .what is event object and how to use it .
2. how to write parameters object to pass in these different commands.
3. how to use get,put,get,post command from aws-amplify/api library and how to pass query parameters.

## API permissions

currently the APi nbnwreactfrontend does not have permission to update articles in NBNWNewsTable so use the nbnweditorfinal api to update the items of this particular table.

**Functions used in backend**
<br />
Steps involved
<br />
1 Use these functions defined here in your api change the tablename,filterexpression,expressionattributevalues depending on table attributes.
<br />
2 Run this command to update backend in cloud

```
amplify push

```

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
This was the function used in backend to retrieve articles of a particular category  replace the tablename with the appropriate table name in your case.
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
This was the function used in backend to update category of each article and replace it with new category. replace the tablename with the appropriate table name in your case.

**Functions used in Frontend**
Steps involved
<br />
Use these functions defined here in your frontend.
<br />

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
This function is used in frontend to retrieve articles of a particular category (in this case it is business) ..Change the apiName,path and options depending on your project .
<br />

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

<br />
This function is used in frontend to change category of each article with the new category (in this case it is business).
<br />Change the apiName,path and options depending on your project .
```
