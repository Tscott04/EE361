Trenton Scott
#0967241
Computer Engineer
4/16/25

The model was trained using KNN (K-Nearest Neighbors) This takes the data given from our users swipe actions and filters the data to remove any severe outliers.
Current users are labeled as 1 (genuine data or matched to a user) and others are 0.
This is determined by a prediction done using the sklearn package.

As shown in the slides given on ML we are using X train (features) and Y train (labels). 80% of data is used to train and the other 20% to test the models fit.
We have our K value set to 3 as for our data set size (between 5 to infinity) this made most sense.
Enrollment for verification takes a minimum of 50 swipes as given by the android studio files constraints.
Once trained it is then saved to my models folder as a .pkl.

The accuracy of my model is not tested directly but instead reliant on the proper filtering of data in my FrontEnd.py and through the minimum enrollment for data sets.

Authentication is tested as the IP sent over flask confirmed connection to the android studio was made and when an error occurs prompts are sent via the run terminal to inform
the user of most possible error cases. Plus it confirms a match of data if the prediction fires as true upon the starting of training.

These were all tested through trials of running and training 4 data sets all over the enrollment data set quantity.
All test were scrolled by myself in the android studio virtual phone.

To run inside of PyCharm ensure to pip install requirements.txt to have every package installed at once.
Then run android studio app and start app.py. To train models and check for authentication run BackEnd.py.