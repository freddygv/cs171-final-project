# Notes:
* apikey = 2282ac571e0b46b69bb7879f4de9b158

1. There is no sentiment analysis. Despite classifying bills by different keywords there is no visibility into the goal of the bill
  * To counter this it could be useful to display a column chart that shows how many times D vs R sponsored each type of bill. 
    * It might be unnecessary to go beyond showing simply D and R regardless of chamber. Yet chamber could be incorporated by having two columns per party: one column for each chamber and one group for each party
2. Upon highlighting a bar, a pie chart could appear that shows the number of bills passed vs failed for this query.
  * This could also be a vertical bar graph to the right
  * There could also be a second chart or graph that shows how many bills of this type were enacted vs vetoed
    * This could be efficiently displayed by using a stacked column chart where one column shows bills rejected and the other column is a stacked column that is composed of bills enacted and bills vetoed (with vetoed bills at the bottom?)
3. Bills:
  * Top Keywords: http://thomas.loc.gov/cgi-bin/bssQuery/?&Db=113&srch=/home/LegislativeData.php?n=BSS&Opt=f
  * List:
    * Agriculture and food, Animals, Armed forces and national security, "Arts, culture, religion", "Civil rights and liberties, minority issues", Commerce, Congress, Crime and law enforcement, Economics and public finance, Education, Emergency management, Energy, Environmental protection, Families, Finance and financial sector, Foreign trade and international finance, Government operations and politics, Health, Housing and community development, Immigration, International affairs, Labor and employment, Law, Native Americans, Private legislation, Public lands and natural resources, "Science, technology, communications", Social sciences and history, Social security and elderly assistance, Social welfare, Taxation, Transportation and public works, Water resources development

### Working query for vote breakdowns:
http://congress.api.sunlightfoundation.com/votes?vote_type=passage&result=Passed&fields=voted_at,chamber,bill_id,question,result,breakdown.party&apikey=2282ac571e0b46b69bb7879f4de9b158&per_page=50&page=1

1. Filters:
  * Vote Type = Passage
  * Result = Passed
2. Fields:
  * Chamber
  * Bill ID
  * Question
  * Result
  * Breakdown by party
  * Page 1

Needs to iterate through: 
http://congress.api.sunlightfoundation.com/votes?vote_type=passage&fields=voted_at,chamber,bill_id,question,result,breakdown.party&apikey=2282ac571e0b46b69bb7879f4de9b158&per_page=50&page=1&query=


### Working query for bills:
http://congress.api.sunlightfoundation.com/bills?actions.result=pass&fields=short_title,bill_id,history.vetoed,history.enacted&apikey=2282ac571e0b46b69bb7879f4de9b158&per_page=50&page=1&keywords=

1. Filters:
  * Keywords = [keyword]
  * Actions.result = pass 
2. Fields:
  * Short title
  * Bill ID
  * Was the bill vetoed?
  * Was the bill enacted?

## Data structure layout:
###Array
    [Keywords]:
        Bill_ID
        Voted at
        Chamber
        Question
        Result
        Breakdown:
          R:
            Yea
          D:
            Yea

