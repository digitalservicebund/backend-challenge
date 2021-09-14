# GovData Dashboard

[GovData.de](https://www.govdata.de/) is the data portal for Germany. The federal, state and local governments can share their data. Although the "Open Data Act" makes it obligatory to share data, only about 52,000 data sets are online so far.

## Your Task

Create a small application that provides a dashboard showing how many data sets each federal ministry has made available on GovData. States, municipalities and other institutions should be ignored.

GovData provides two APIs. Use either the [CKAN Action API](https://www.govdata.de/ckan/api/3) ([documentation](https://docs.ckan.org/en/2.9/api/index.html#get-able-api-functions)) or the [SPARQL endpoint](https://www.govdata.de/web/guest/sparql-assistent) to solve this challenge. In `departments.json` you will find all federal ministries and their subordinated agencies that have published data on GovData.

Use a non-proprietary tech stack of your choice and explain in a readme how to run your solution. Please email your solution as a zip file to [challenge@4germany.org](mailto:challenge@4germany.org). If you're using
Git during building your application please make sure to include the Git history as well.

## Evaluation

You should turn in a complete and runnable solution, but do not gold-plate it: we don't expect you to spend more than a few hours on this exercise. We want to see that you know how to use APIs efficiently, how you structure and how you are testing your application. It should be easy to tell from the dashboard which ministries have provided the most data.

In the technical interview that follows we would like to discuss your approach, and that includes talking about areas you would want to improve if given more time.

Note that the UI won't be part of the evaluation (could be plain HTML for instance).

## Have fun! 🚀

We look forward to your submission! Please [let us know](mailto:challenge@4germany.org) if you have any questions or concerns.
