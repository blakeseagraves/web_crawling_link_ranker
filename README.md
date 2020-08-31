
\# Web crawler/link ranker

This python script takes a list of websites and iterates throught the list, grabbing every link on each page. 
Then it takes that data and sorts it into two groups, links that occur more often than the median, and links that occur less often than the median.

I also added a feature to strip the scraped links, removing everything after ".com" because it gave more repetition to the data, making the results more interesting
