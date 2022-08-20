# File-Submission-App

https://gabrielchua-file-submission-app-app-fvf9oi.streamlitapp.com/

*Problem Statement:* You send out an excel report template requesting for data (e.g. more than 50 rows), but the data comes back dirty
*Proposed Solution:* A report submission portal that validates the files (first part) and is easily configurable by the data requester (second part)

This is a simple toy example to test the first part of the proposed solution i.e. a report submission portal. 

You can try it using these 3 files:
- “success.xlsx” - where the user correctly fills up the given template 
- “error_1.xlsx” - where the user changed the template by changing the name of the columns
- “error_2.xlsx” - where the user added a duplicate row

To prove that these logics are not hardcoded to the 3 examples, you can change any of these 3 files by:
- adding more duplicates
- changing the names of the columns
- adding extra columns 

and the appropriate error message will appear.

For now:
- The portal conducts 2 checks (whether the headers of the file match the given template, and whether there are duplicate rows). Other checks can be easily built too.
- The portal validates the uploaded file only and doesn’t do anything further. In concept, this can be extended to then transmit the uploaded file to to our emails.

Lastly, it’s worth stressing that this was all built and deployed within one hour

“IT systems” don’t have to be expensive nor slow to build ;)