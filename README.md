# CS 6350 - Machine Learning - Mid Report

## Progress Towards the Goal

### The Data Space

I'll be brief in this segment, but I believe it is important to the understanding the type of data gathered. 

I am currently involved in a research project dedicated to finding bugs in web browser layout engines in an automated fashion. This process involves three steps. The first is to generate randomized webpages, the second step is to make randomized changes to the styles on those pages, and the third is to detect if there is consistency in the way those changes have been applied. As output to this process, there are many bugs found in the web browser layout engines. Each of the bugs found has a list of styles attributed to this bug. Some of the styles attributed are from initial page generation, and some of the styles attributed are from randomized changes.

I began by cleaning the data. From each bug I extracted the list of styles attributed to the bug. I created a complete list of all styles used in any of the bugs and used this to generate an array for each bug with Boolean values indicating which styles are attributed to that bug. This is the data that was used in the clustering algorithms outlined below.

### KMeans Algorithm

I initially tried the key means algorithm. This algorithm is an unsupervised clustering algorithm which allows the data to be put into piles. The number of piles used depends on the number of clusters indicated at the beginning of the process. One of the problems I ran into quickly was deciding the number of clusters to choose for my data set.

I hoped to see the rows in my data set grouped into clusters that would indicate similarities in the cause of the bugs. Due to the fact that I don't know how many bugs are in a particular web browser layout engine, and there seems to be no good way to find this information, determining the number of clusters to use in the K means algorithm proves difficult.

#### KMeans Algorithm - Number of Clusters

While searching for the right number of clusters to use for the K means algorithm, I attempted to run the experiment in a loop. I used a variable number of clusters from 3 to 100. With this approach, I was hoping to find a lot of separate clusters where highly related. One of the side effects of using this approach was that I found that several of the bugs had the exact same set of styles. A few of the bugs that I found had extremely long lists of styles used. These bugs were categorized into their own clusters in the experiments were the number of clusters was greater than or equal to 20.

One of the heuristics that I used to judge whether this algorithm was performing as expected has to do with specific styles. In web frameworks, the styles often come in pairs. For example, "margin–right" will set the right margin on a container while "margin-left" will set the left margin on a container. I expected that bugs which include "margin-right" could also be found using an inverse set of properties where "margin-left" is substituted for that style. This hypothesis proved to be correct as the number of clusters used in this algorithm exceeded 30. In one such case, "inset-block-end" and "inset-block-start" proved to be near interchangeable. Seeing this would go well with the expectation that this algorithm is clustering bugs into sets of bugs that have the same root cause. This observation confirmed my expectations and showed value obtained from this approach already.

#### The "Display" Attribute

One of the observations I've made at this point is that the "display" attribute tends to have a consistent value throughout the bugs within a cluster. This is especially true as the number of clusters grows. The "display" attribute is the styling attribute that tells the browser what mode HTML elements are in when they are displayed. For example, "display:block" treates every HTML element as it's own block structure with no overlap, while "display:absolute" treats the web page as a canvas where every element has an absolute position relative to the top-left of the page. You can see how this "display" property vastly changes the layout of the page.

The interesting part here is that, within clusters of bugs, the display attribute value tends to be consistent. This would suggest that similar bugs are caused by maladies in a piece of the code. This would also suggest that sections of the code base are likely broken up based on the value of this display attribute.

## Detailed plan for the rest of the project

One of the questions that remains to ask about the kmeans algorithm is "How many clusters are ideal?". This is a difficult question to answer because it requires us to know the answer to this research project before answering it. If we knew how many layout bugs are in a web browser's code base, we would know how many clusters to use but we also wouldn't need to complete this project.

### Unsupervised Hierarchical Clustering

In order to do more exploratory learning about the dataset, I'd like to try a number of different unsupervised clustering algorithms. For example, hierarchical clustering will allow me to see bugs which are most similar and then to elucidate bugs which may have an overarching cause. In the context of finding bugs to fix, this hierarchy will be helpful in determining what other bugs may be most similar. In the simplest case, fixing a single bug will fix any duplicates of that bug. In a slightly more complicated case, two bugs may be caused by similar, but not identical, edge cases. If this is the case, fixing the two edge cases at the same time will save time and money for browser developers by save the cost of context switching and retesting that area of the code.

### Extra Feature Extraction

In this early stage of the project, I relied on the overall set of styles used in the creation of the bug. One improvement could be made is to separate these styles into initial styles and styles which are applied later. This would give the algorithm extra leverage in clustering the groups of bugs correctly.

Other data could also be extracted from the initial bug reports. The two main pieces in the bug reports are the styles used and the HTML element structure. The HTML structure could be mined for features and extra data, such as the number of HTML element used or the depth of the nested HTML tree. These extra features with it would further help to categorize the bugs found.

## References

- https://builtin.com/data-science/unsupervised-learning-python
- https://realpython.com/k-means-clustering-python/
- https://www.w3schools.com/cssref/pr_class_display.asp
- https://www.guru99.com/unsupervised-machine-learning.html
- https://towardsdatascience.com/unsupervised-learning-and-data-clustering-eeecb78b422a





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



# CS 6350 - Machine Learning - Final Report


# References
- https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html
