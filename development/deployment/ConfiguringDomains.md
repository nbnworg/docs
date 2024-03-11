# Configuring Domains Wiki
This document aims to capture how we can configure domains for NBNW.org (for current and future projects)

It does not intend to be a dive deep into all the concepts but rather tries to explain why each component is required and how they link with each other to help in setting up a new domain for any future projects if necessary.

## 0. Prerequisite knowledge/work done
1. Existing knowledge of Amplify
2. Existing Website Prototype deployed in Cloudfront.

## 1. Prior Understanding
Before working on development you need to understand 3 main concepts - 
1. Hosted Zones in AWS Route 53
2. ACM Certificate
2. Cloudfront & Alias in Cloudfront

### 1.1  Hosted Zones
Currently, we have permissions setup for the name servers to be pointing to the hosted zone that is setup in AWS Route 53 for nbnw.org. This means that when a user is looking up for nbnw.org in the browser, they are redirected to the hosted zone for further resolution of DNS.


### 1.2 ACM Certificate
When using any domain, we need to prove that we are actually owning that domain and ACM certificate helps us prove that. We need to issue ACM Certificate for the domains we plan to use. As an example, say we want to use editors.nbnw.org, we will issue certificate for both editors.nbnw.org and www.editors.nbnw.org. (The process is explained in details in section 3.)

### 1.3 Cloudfront & Alias in Cloudfront
When creating a website using amplify and deploying it using cloudfront and s3, it creates a sample (rather random) domain for us to use with cloudfront. Cloudfront is basically a CDN that allows us to host website. When we want to use our custom domain, we need to set an alias for the same. Alias basically means the other domains that we want to use for deployment. e.g. editors.nbnw.org and www.editors.nbnw.org

## 2. Permissions
1. You will have to request NBNW Executive Office permission for subdomain that you would like to use.
2. You will need temp access to AWS Route 53, Cloudfront and Certificate Manager.

## 3. Steps involved
Note: For the sake of ease, we will be using editors.nbnw.org as an example. DO NOT USE/EDIT that.

1. Go to Cloudfront and select the website that you have deployed (and want domain registered for that website), open that.
2. In Settings section (where you see ```Alternate domain names```) click edit.
3. In Alternate domain name (CNAME) - optional section, add in the alternate domain that you got approval for - e.g. editors.nbnw.org, www.editors.nbnw.org.
4. Currently, we don't have the certificate yet. So in custom SSL certificate section, click on request certificate (which should open a different tab)
5. Select Request public certificate and click next.
6. In fully qualified domain name, add the approved domain name, e.g. editors.nbnw.org and also click add another domain name to this certificate to add www.editors.nbnw.org
7. Leave the rest as is and click request certificate. Now it show go to pending.
8. You should see a button like create records in Route 53, select that and create records. (It should get auto approved in a while).
9. Go back to cloudfront tab and select refresh next to SSL to refresh available certificates (after step 8 shows issued instead of pending)
10. Select the certificate for your domain (e.g. editors.nbnw.org in this case)
11. Click save changes.
12. Now that this is done, we need to add 2 records in hosted zone for nbnw.org, that will be for www.editors.nbnw.org and editors.nbnw.org (again, this is just an example, you will have to add your own ones which were approved)
13. Go to route 53 in aws
14. Select nbnw.org hosted zone and open it.
15. Click create record and add your subdomain there, e.g. editors.nbnw.org (note nbnw.org will be prefilled so you only need to add editors or www.editors instead of entire thing).
16. Click the Alias toggle to turn it on
17. Select cloudfront in first option selection
18. Select your cloudfront domain in next and click create records.
19. You need to repeat step 15 through 18 to create records for both www.editors and editors.


With these steps, you have created a domain that routes to the cloudfront website. Cheers!

## 4. Verifications
Once you have performed above steps, you have connected the 3 components, hosted zone, Certificate and the cloudfront domain with each other. After a few minutes, the website should be active. 

You might have to clear your cache to make sure it is working. 

1. To verify, go to both, editors.nbnw.org and www.editors.nbnw.org (make sure to replace this with your domains that you created!!!)

## Document Change History
- Sarvesh - Created Initial Document with steps
