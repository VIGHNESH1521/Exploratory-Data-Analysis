Exploratory data analysis popularly known as EDA is a process of performing some initial investigations on the dataset to discover the structure and the content of the given dataset. It is often known as Data Profiling. It is an unavoidable step in the entire journey of data analysis right from the business understanding part to the deployment of the models created.

In this laptop price dataset, I have made use of the following libraries.

- SWEETVIZ

![image](https://user-images.githubusercontent.com/90493668/174609457-4c94ffc4-63ab-49da-bff5-b0ecd0bf0cdb.png)

SweetViz Library is an open-source Python library that generates beautiful, high-density visualizations to kickstart EDA with just two lines of code. Output is a fully self-contained HTML application. The system is built around quickly visualizing target values and comparing datasets. Its goal is to help quick analysis of target characteristics, training vs testing data, and other such data characterization tasks.

- PANDAS PROFILING

![image](https://user-images.githubusercontent.com/90493668/174610086-d6b7ef39-f036-4bb4-81e7-661503d26d09.png)

The Overview section, the first section within the Pandas Profiling Report, shows summarised statistics for the dataset as a whole. It returns the number of variables, which is the number of columns that were included in the passed DataFrame. The number of observations is the number of rows that were received. The Overview also provides the number of missing cells or duplicate rows and a percentage of total records that were impacted. The missing cells and duplicate row statistics are quite important as a data scientist as these may indicate broader data quality issues or issues with the code used to extract the data. The overview section also includes data around the size of the dataset in memory, the average record size in memory and any data types that are recognised.

Pandas Profiling offers an incredibly in-depth analysis of numerical variables covering quantile and descriptive statistics. It returns the minimum and maximum values within the dataset and the range between. It displays quartile values which measure the distribution of the ordered values in the dataset above and below the median by dividing the set into four bins. When considering the quartile values, if there is a greater distance between quartile one and the median verse the median and quartile three then we interpret this as meaning a greater scatter of smaller values than the larger values. The interquartile range is simply the results of quartile three minus quartile one.
