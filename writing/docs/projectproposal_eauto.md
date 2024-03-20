# 1. Project Name: AutoNews

# 2. Vision:
On 30th March, 2024 NBNW launched it's own news portal nbnw.org along with its E-Portal for editors to work on. Since then it's been over 3 months of NBNW operation but we currently only have 5 article publishing rate (apr)/week (w).

With 5 apr/w we were able to only 60 articles in total. This is not enough to bring NBNW anywhere close to 1M viewership by the end of this year. To be able to reach that scale we will have to increase our apr to atleast 40 apr/w.

To achieve this objective, NBNW is launching AutoNews. It allows us to generate news articles automatically while editors focus more on editing and ensuring our content quality stays high. This enables faster time to market, scale up and keep track of more articles to launch.


# 3. FAQ:
#### 1. What if editor wants to write their own article instead of relying on automated article?
Editors will be able to use Editor's portal like usual, we will be having an additional page called automated article which will have prepopulated content for editors to be able to edit and send for approval.

#### 2. What will be the role of editors?
Editors will have to Verify the content, find 3-4 similar source that covers all the things discussed in the articles and attach there. Editors will have to do more research and verification work than writing itself.

#### 3. How is it increasing editors apw?
This tool allows editors to focus more on research rather than focusing on the writing part itself. This essentially reduces the work required by atleast 50% as most of the time required is in conveying the information.

#### 4. How are we ensuring consistency in the type of article?
As with the case of Editor Portal, we will be having templates for which we will be using GPT to fill in the information based on the information collected.

#### 5. Will the template make the news article seem bland?
We will be having more than one template to avoid making content look "very alike".

#### 6. Are there other things that we are considering to make the content look less robotic?
Yes, we have plans to improve the model later to even consider the type of article we are generating automatically and make decisions for writing based on that. We might also involve a mix of models or look more into writing styles and ask the gpt to write in different writing styles depending on the article.

Having said that, that is for V2 and on V1, we do expect it to feel a bit robotic in nature.

#### 7. How are we eliminating this risk of robotic sounding article?
We will leave the responsibility to Editors to edit the article. Editors should not think the automated article as the final version but rather as a first draft for the same.

#### 8. What if editors use the AutoNews as is and keep posting directly instead of editing?
We will be setting a blocker to not allow direct posting. We need editors to do research and add the sources there. Furthermore, we will also be tracking it internally different metrics such as Time spent, changes done from first draft, etc. to ensure that editors are treating it as first draft and not the final product.

#### 9. What will be the responsibility of approvers?
Approvers will be responsible to check the sources that editors added which relates to the news and verify if all the content is covered in the attached sources.

#### 10. What if approvers skip their responsibility?
We will be performing automated checks on sources and the article content as well. If we see that sources and content does not match with each other but is still approved, the post will be flagged.

#### 11. What happens to the flagged posts?
Flagged posts will be reviewed by the leadership and leadership will decide if it was false positive or true positive. If it is true positive, Editor will be reached out for understanding the reasons.

#### 12. What is the expected apw after this solution goes live?
After this goes live, we expect the apw of editors to increase atleast by 200%. i.e. from 5apw to 20apw.

#### 13. What was the reasoning behind 200% apw increase estimation?
Assumption of 20apw is based on the following - 
1. Reading 5 articles (4 research and 1 automated) takes about 1 hour
2. Validating and editing takes about 30 minutes.
3. Based on the above estimates Editor is able to produce 3-4 article per day, i.e. 15-20 articles per week. (Note, review time of about 60 minutes per day is already counted in assumption of incoming articles)

#### 14. Is the assumption too optimistic?
Yes, it is. 20apw is a difficult target but we don't go for easy and always deliver above and beyond.

#### 15. What if editors are not able to meet 20apw after this?
We will have to work with them to see what additional things we can do to help them reach 20apw. We will not lower our target.

#### 16. What if the 20apw target makes editors lower the quality of articles?
We will not lower the quality of the articles either. It will be our responsibility to find ways on continually increase the quality of the articles.

#### 17. What measures will we take to ensure that quality of articles is not reduced?
We will introduce a role, article quality checker which will have 2 major responsibilities.
1. Review Article Queue.
2. Check quality of published articles and report low quality articles.

#### 18. Are there other metrics we are tracking?
We do plan to have user engagement with articles as well. Assumption is if article is of high quality, we will have high engagement.

#### 19. Won't trending topics have more engagement?
Yes, that is true. We will have to setup Diff-in-Diff model to compare the engagements using A/B testing but we won't be doing that currently. Leadership have to make assumptions and be right with their intuition for this.

#### 20. Can AutoNews generate duplicate articles?
Yes, with low probability.

#### 21. How are we keeping the probability low for duplicate articles?
We will be having following components in the system - 
1. Trending Topic Collector - Responsible to find N number of trending topic for the day.
2. Topic Queue Generator - Responsible for creating a topic queue which will be pushed to editors one by one.
3. Topic Checker - It will check queue (and past topics) to compare if we already talked about it.
4. Scrape and Article Generator - It will scrape relavent articles and generate new article based on the template.

In this, 3. Topic Checker might have a slight possibility to miss when we will be creating similar article.

#### 22. What will be the risks of posting similar articles?
Well, one main risk is customer trust. i.e. if we post article with two different conclusion due to model setting. We cannot loose customer trust at any cost, for this, quality checkers will be responsible as well to keep an eye for and flag any such cases.

#### 23. What will happen after quality checker flags?
We will see the reasoning and try to incorporate in model training or lessons learned.

#### 24. What will be 


# 4. Opportunities:
[Write down the opportunities that this product will generate in bullet points manner.]


# 5. References: 
[Include any references or sources of information]


# 6. Document History:
[Maintain a record of changes made to the document for transparency and accountability.]

