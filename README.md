# GlassDoor-Company-Rating-Pull

In case you have ever wanted to pull a glassdoor rating of a company (or do so for a lot of companies, like the constituents of the S&P 500) you need something that can do so automatically.  Now you may think "Lets go get their API!"  The problem is, you have to apply for a token to use their API, and after attempting to do so unsuccessfully once or twice, I decided to write this instead.  This framework provides a function that will take a company name as input and spit back the first rating as a result of your input being used as a search query.

NOTE:  The first result may not be the correct result, if there is no result at all, the function may freeze (working on it.)

Having stated the bugs, if the company can be found on Glassdoor using your search query, it will report the right value.  Having tried this on ~300 queries, I would say its about 85-90% effective (definitely beats doing so one by one.)

Enjoy!!
