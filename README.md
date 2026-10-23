# cancer_project

Project by Alan and Natalie

For this project, we were curious as to wether the type of therapy, or combination of therapies, a patient recieved could predict whether they are likely to survive. We trained a primitive model by sectioning the data in a random 80/20 ratio, in which we used the larger 80% of the data to "train" a model (save the proportion of survivability for all therapy treatments), and then attempted to predict the remaining 20% of the dataset based on the therapies. We then compared the models performance to the actual data on survival rate, and graphed the proportion of correct guesses vs actual data. our accuracy was baout 58%. This is likely because we have not accounted for additional factors such as age of onset and secondary infections. This would likely be the best variables to account for in the future if taking this project further. To run the code, just download the files and run python main.py. Seed is set at 42 and runs with that seed should match exactly to these graphs. 

![alt text](image-1.png)

![alt text](image-2.png)

<img width="1000" height="597" alt="image" src="https://github.com/user-attachments/assets/c3224f81-4793-46a9-9e2f-f710c950af88" />

<img width="492" height="488" alt="image" src="https://github.com/user-attachments/assets/548ff353-c7f4-4646-abfa-a2a3efb5276d" />
