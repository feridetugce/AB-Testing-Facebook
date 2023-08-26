# A/B-Testing.py
### Analyze A/B Test Results

Facebook recently introduced a new bidding type, “average bidding”, as an alternative to its exisiting bidding type, called “maximum bidding”. One of our clients, bombabomba.com, has decided to test this new feature and wants to conduct an A/B test to understand if average bidding brings more conversions than maximum bidding.

In this A/B test, bombabomba.com randomly splits its audience into two equally sized groups, e.g. the test and the control group. A Facebook ad campaign with “maximum bidding” is served to “control group” and another campaign with “average bidding” is served to the “test group”.

The A/B test has run for 1 month and bombabomba.com now expects you to analyze the results of this A/B test.

* Facebook Ad: An advertisement created by a business on Facebook that's served up to Facebook users.
* Impressions: The number of times an ad is displayed.
* Reach: The number of unique people who saw an ad.
* Website Clicks: The number of clicks on ad links directed to Advertiser’s website.
* Website Click Through Rate: Number of Website Clicks / Number of Impressions x 100
* Cost per Action: Spend / Number of Actions
* Action: Can be any conversion event, such as Search, View Content, Add to Cart and Purchase.
* Conversion Rate: Number of Actions / Number of Website Clicks x 100
* The ultimate success metric for bombabomba.com is Number of Purchases.Therefore, we should focus on Purchase metrics for statistical testing.

How would we define the hypothesis of this A/B test?
H0 : There is no statistically significant difference between the Control group that was served “maximum bidding” campaign and Test group that was served “average bidding” campaign.

H1 : There is statistically significant difference between the Control group that was served “maximum bidding” campaign and Test group that was served “average bidding” campaign.

Warning!
I should point out that I cannot share the dataset because it is not open source.
