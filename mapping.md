## Document Mapping

**overview**
My goal is generally to have a serachable document on which I can also aggregate labeled fields. I keep a copy of the original document as I recieved it for reproducibility. Searching often means augmenting the document such as having a mapping for normalization or a text representation without markup.

**observations**
Mapping a complex documents is work. Even having a visually styled document to work from is only so helpful. Additionally, if the data is similar to existing data, but from a different source, it should be mapped to a common standard for that domain.
Preping the document for strorage has additional considerations. However, a variety of data is repeated for readability in documents I've worked with. Choices about what to include in a key-value redering.

### Bucks County
Bucks County data begins as HTML. It is designed with tables, so HTML tools like python's BeautifulSoup and lxml are wonderful resources.
Even with these resources, the data in the documents was not so consistent that extracting it is was a one command process.
I used Beatiful soup to review the tables of the document and the contents of each table. I made a basic outline to help me keep track of the documents. I maked the tables that I would parse with an "o" and then labeled the content. From there, I created a class to extract the text. The object included methods to step through various stages of extracting data so that the HTML document could become a representative JSON document. 
I decomposed the document into summary, client, and compliance data. I didn't work toward including comments. I used a similar process to gather summary and client information. 

<<<<<<< HEAD

num |  basic | outline |
=======
<<<<<<< HEAD
### |  basic | outline |
>>>>>>> 0ead4664395d22f6d78cbeb7cbd206b3922d6754
--- | ------ | ------- |
0   |    x   | includes all   |
1 | o        | header         |
2 | o | summary        |
3 | o | client         |
4 | x | label info     |
5 | x | label info     |
6 | o | compliance     |
7 | o | compliance     |
8 | o | compliance     |
9 | x | retail practice|
10| o | compliance     |
11| o | compliance     |
12| o | compliance    |
13| x | signature      |
14| x | signature      |
15| x | signature      |
16|   |                |
17| x | summary on page 2 |
18| x | client on page 2 |
19| o | temperature observation |
20| o | observeration |
21| x | signature     |
<<<<<<< HEAD
22| x | signature     |
=======
22| x | signature     |
=======
### |  basic | outline
--- | ------ | -------
0 | x | includes all
1 | o | header
2 | o | summary
3 | o | client
4 | x | label info
5 | x | label info
6 | o | compliance
7 | o | compliance
8 | o | compliance
9 | x | retail practice
10| o | compliance
11| o | compliance
12| o | compliance 
13| x | signature
14| x | signature
15| x | signature
16|   |
17| x | summary on page 2
18| x | client on page 2
19| o | temperature observation
20| o | observeration
21| x | signature
22| x | signature
>>>>>>> refs/remotes/origin/master
>>>>>>> 0ead4664395d22f6d78cbeb7cbd206b3922d6754
