# SQLite Music

## Questions

2.1. ArtistId is said to be a foreign key in the Album Table beause it refers to a primary key in another table, the Artist Table.
ArtistId defines a relationship between the Artist table and the Album Table.

2.2. We can already link each AlbumId to an ArtistId by having ArtistId in both the album table and artist table, so having both AlbumId and ArtistId
in the Artist table as well would be redundant.

2.3. SQL can auto-increment a primary key that is an integer, which makes it easier to distingish between each separate entry.  Also,
ensuring that the primary key is a function of the database itself and not based on the user's input protects against someone trying to
infiltrate the database.

2.4. SELECT SUM(total) AS "Total Cash From 2010" FROM invoice WHERE invoiceid >83 AND invoiceid < 167

2.5. SELECT Name FROM Track JOIN InvoiceLine JOIN Invoice ON InvoiceLine.InvoiceId = Invoice.InvoiceID AND Track.TrackId =
InvoiceLine.TrackId WHERE CustomerId = 50

2.6. One could use the GROUP BY clause by which they only have separate rows for each new composer and prevent duplicates.  They
could then use COUNT(TrackId) to then show how many songs each composer has associated with them, should they ever want to access
each individual song.

## Debrief

a. I found problem set 7, lecture.DB, and the website http://www.sqlitetutorial.net helpful in answer this problem's questions.

b. I spent about 2.5 hours on this problem's questions.
