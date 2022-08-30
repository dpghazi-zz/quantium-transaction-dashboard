# Quantium Transaction Dashboard

## **Project Description**
- This transaction dashboard is a single-page application meant for one of Quantium’s largest supermarket clients, Soul Foods, who has recently increased the price of their most delicious candy bars, Pink Morsels.
- This web application uses Python and Dash that displays its sales data with a radio button, allowing the client to see how the change has affected the overall profits and analyze their product’s sales by region.

### **Overview**

- **Data Processing**
  - Converted CSV files containing Soul Food’s entire morsel line sales data into a single formatted output file for only Pink Morsel’s, containing three fields (sales, date, and region).
- **Building Dash Application**
  - Created a line chart with axis labels that displays the sales data generated in the output file, sorted by date.
  - Implemented a radio button with with five options to narrow which data appear in the line chart: north, east, south, west, and all.
  - Applied CSS to each element to make the application more visually appealing.
- **Application Testing**
    - Created a three tests using the Dash testing framework. The tests ensure the following:
      - The header is present.
      - The visualization is present.
      - The region picker is present.
    - Executed the test suite using PyTest to make sure each test passes.
- **Automating Tests**
  - Implemented a bash script which automatically runs the test suite and does the following:
    - Activate the project virtual environment.
    - Execute the test suite.
    - Return exit code 0 if all tests passed, or 1 if something went wrong.

## Result
![Kapture 2022-08-29 at 23 13 50](https://user-images.githubusercontent.com/94224903/187363392-509cf841-c2d1-42db-a468-249be0cd740c.gif)
![Screen Shot 2022-08-29 at 11.17.51 PM.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/14cf73fd-7583-42c4-add5-6d64d72012c1/Screen_Shot_2022-08-29_at_11.17.51_PM.jpg)
- Surprisingly, the sales were higher after the Pink Morsel price increase on 01/15/2021

### Language **& Tools**

- Python (Dash, Pandas, PyTest)
- CSS
- Bash




