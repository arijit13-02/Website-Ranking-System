Website Ranking System using Python, beautiful soap, tkinter, requests and mysql (python mysql connector).

=====================================================================================================================================

PreRequisities:
Install the requirements.txt by using "pip install -r requirements.txt"
Otherwise, one can obviously individually install the packages.

=====================================================================================================================================

Overview:
First websites need to be hosted under users. Keywords need to be added each time new websites are hosted. 
Keywords can also be changed for previously hosted websites. Hosted websites can themselves by deleted when logged 
through the user details who hosted it.

The personal search engine provides options for searching using keywords. The system matches with the keywords already assosciated
with the websites, and ranks them according to the count of keyword hits. Top Websites' Link are displayed in the window.

=====================================================================================================================================

The ranking management system is started with login.py, which can be run by "py login.py". Users first need to create an account, 
only then will they be allowed to host websites. User dashboard provides with multiple options. After working with them, close the window.

The search engine is started with search.py, which can be run by "py search.py". Space is provided for searching, and it displays the websites best suited accoriding to the keywords used for searching in a ranked manner.

=====================================================================================================================================