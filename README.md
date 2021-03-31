# CS 6350 - Machine Learning - Mid Report

## Progress Towards the Goal (50%)

### The Data Space

I'll be brief in this segment, but I believe it is important to the understanding the type of data gathered. 

I am currently involved in a research project dedicated to finding bugs in web browser layout engines in an automated fashion. This process involves three steps. The first is to generate randomized webpages, the second step is to make randomized changes to the styles on those pages, and the third is to detect if there is consistency in the way those changes have been applied. As output to this process, there are many bugs found in the web browser layout engines. Each of the bugs found has a list of styles attributed to this bug. Some of the styles attributed are from initial page generation, and some of the styles attributed are from randomized changes.

I began by cleaning the data. From each bug I extracted the list of styles attributed to the bug. I created a complete list of all styles used in any of the bugs and used this to generate an array for each bug with Boolean values indicating which styles are attributed to that bug. This is the data that was used in the clustering algorithms outlined below.

### KMeans Algorithm

I initially tried the key means algorithm. This algorithm is an unsupervised clustering algorithm which allows the data to be put into piles. The number of piles used depends on the number of clusters indicated at the beginning of the process. One of the problems I ran into quickly was deciding the number of clusters to choose for my data set.

I hoped to see the rows in my data set grouped into clusters that would indicate similarities in the cause of the bugs. Due to the fact that I don't know how many bugs are in a particular web browser layout engine, and there seems to be no good way to find this information, determining the number of clusters to use in the K means algorithm proves difficult.




## Detailed plan for the rest of the project (30%)

## References (20%)
- https://builtin.com/data-science/unsupervised-learning-python - O





# CS 6350 - Machine Learning - Project Proposal

## Who are in the project team?

I will be the only student working on this project. (Solo)

Preceding this machine learning project, I’ve been working with Professor Pavel Panchekha and I owe credit to him and the previous students he’s worked with for progress up to this point. No machine learning work has been done on the project previous to this class.

## What problem do you want to address?

Together with Pavel Panchekha, I’ve been working on a piece of software that automatically tests for and detects bugs in web browser layout engines. Each bug that is detected is tied to a list of CSS styles and an HTML structure.

For example, these CSS attributes (with certain values and organization) cause a bug in the reflow of Chrome’s layout engine: [margin-bottom, padding-inline-start, white-space]

We have thousands of bugs and each bug is associated with 2-50 style combinations. We believe that many of those bugs are unique manifestations of the same underlying issue. By using an unsupervised clustering algorithm, we hope to group similar bugs together and uncover patterns in the data.

## Why is it interesting? 

After finding bugs in Chrome, our initial plan was to submit them all to the Chromium team. However, the Chromium team has thousands of other bugs to comb through. By grouping similar bugs together, we assist the Chromium Team in faster triage and more complete bug fixing in the Chrome Layout Engine.

## Why do you want to use machine learning rather than traditional/existing methods?

Manually looking at these bugs is proving too tedious a process and creating a program to sort them would still require work directly proportional to the number of bugs we find. We’d like a sorting process that scales with our bug-finding capabilities.