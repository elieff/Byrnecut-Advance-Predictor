![ima](images/king_county.jpg)

# Byrnecut Australia Advance Predictor

**Author**: [Blake Elieff](mailto:blakeelieff@hotmail.com)

## Project Overview

This project is to produce a model for Byrnecut Australia Pty Ltd. that is able to determine the expected development advance for a week period based on different features. Using this model Byrnecut is able to accurately predict weekly expectations which will help with forecasting and management of their workforce

### Business Problem

Byrnecut wants to gain a better understanding of expectations for their development based on manning levels and heading availability. Some questions to be answered:
* If we gain an extra heading, what effect will have on the expected advance
* What effect does replacing a frontliner with a trainee have on expected advance

### The Data

1 dataset is used. This data set is the JumboData.csv

#### Column Names and descriptions for Kings County Data Set

- **Equipment ID** - The equipment number for each jumbo used
- **Front Liner?** - Whether or not a front liner was operating the jumbo
- **Source Locations** - The location that the activity was taking place
- **Product Group** - Whether the blasted rock was Ore or Waste material
- **Face Hole Drilled** - The quantity of blast holes drilled in the face
- **Ream hole Drilled** - The quantity of reaming holes drilled in the face
- **Hole Length** - The length of the holes being drilled in the face
- **Charged Holes** - The quantity of holes that are filled with explosives for each cut
- **Advance** - The amount of advance gained in each cut
- **Wet Holes** - Not used in underground mining here.
- **Activity** - The type of advance, whether its for a main decline or small ore drives etc.
- **Shift Date** - The date of the advance
- **Shift Type** - The type of shift, either Day shift or Night Shift
- **Week** - The week from the beginning of our contract
- **Site ID** - Our site number

### Methods

In this project i used standard scaling, Train Test Splits, and One Hot Encoding.
I used a variety of functions based on functions imported from the sklearn library

### Results
Here is the function that i produced to determine advance using my final data model

![fnc](images/function.png)

From the model that i created i was able to answer the questions that were asked in the beginning

![res](images/results_bath.PNG)

Adding a bathroom could potentially add $35112 to the house sale price

![ress](images/results_sqft.PNG)

Per sqft adds approximately $195 to the sale price

![resss](images/results_grade.PNG)

A change in grade of the house could potentially increase the price by $276017

### Conclusions

From this analysis and model production. I can conclude that century 21 should use the size of the house, the grade, condition, number of bedrooms and number of bathrooms to determine a potential sale price. Grade is a strong determing factor in sale price, being an increase in approximately $276017 for the median sale in this dataset. 

This model isnt very accurate at determining an actual price. Its better used for calculating increase in value based on different changes in values of features for a house. My Model determines a mean average error of +- $164,000 hence why this shouldnt be used to determine the actual prices of the houses.

As i removed quite a few features from this analysis, i was not able to determine a lower mean average error. This may have been reduced by splitting up the sales into their date ranges aswell as location data. As usually closer to cities will produce a higher price per sqft. Going forward i would use these values in a future analysis.


### For more information

See the full analysis in the [Jupyter Notebook](./byrnecut_advance_predictor.ipynb) or review this [presentation](./byrnecut_advance_presentation.pdf).

### Repository Structure

```
├── images
├── data
├── functions
├── README.md
├── byrnecut_advance_predictor.ipynb
└── byrnecut_advance_presentation.pdf
```

