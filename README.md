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