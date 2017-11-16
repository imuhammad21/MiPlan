# Vantage Points

## Questions

5.1. CSV files are easier to parse because they store data much more simply than a JSON document, and generally take up less space.

5.2. JSON is better at storing heirarchical data than CSV because it has more syntax to make subgroups more clearly defined.

5.3. I could download Netflix’s latest close price (among other values) from Alpha Vantage’s TIME_SERIES_INTRADAY API in CSV format,
using an interval of 1min, via the URL
https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=NFLX&interval=1min&apikey=NAJXWIA8D6VN6A3K&datatype=csv.

5.4. If the number "1." corresponds to "open", the number "2" corresponds to "close", and so on and so forth, there is no reason to
have both of these identifiers repeated over and over again.  A separate table could relate "1" to "open", "2" to "close", etc and
eliminate the redundancy of having two identifiers which mean the same thing listed over and over and over again.

## Debrief

a. I found the website https://www.alphavantage.co/documentation/#intraday helpful in answering this problem's questions.

b. I spent about 1 hour on this problem's questions.
