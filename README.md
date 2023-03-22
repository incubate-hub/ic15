# code-complexity-visualizer
The Time Complexity Visualizer is a Python application that visualizes the time complexity of a Python program using various metrics. The application uses several libraries, including time, timeit, matplotlib.pyplot, streamlit, radon, and cProfile. The application allows developers to understand how much time their code takes to execute, and to identify areas that can be optimized.
## Installation
To use the Time Complexity Visualizer, you need to install the required libraries. You can install them using the following command:
pip install time<br>
pip install timeit<br>
pip install radon<br>
pip install matplotlib.pyplot<br>
pip intall stramlit<br>
pip install radon<br>
pip install cprofile<br>

## Usage
To use the Time Complexity Visualizer, follow the steps below:

1.Navigate to the directory where your Python code is located.<br>
2.Open the command prompt or terminal.<br>
3.Run the streamlit run command followed by the path to the main.py file. <br>For example:<br>
4The application will start running in your browser. You can upload your Python file using the upload button.<br>
5.Once the file is uploaded, the application will generate several metrics that measure the time complexity of your code.<br>
6.The metrics are displayed using graphs and charts, making it easy to identify areas of the code that take the most time to execute.<br>
7.You can also use the application to profile your code using cProfile. This will allow you to identify which functions are taking the most time to execute.<br>
8.The application also allows you to generate a report that summarizes the time complexity of your code.<br>
streamlit run main.py <br>

## Metrics
The Time Complexity Visualizer generates several metrics that measure the time complexity of your code. These metrics include:

## Execution Time
The Execution Time metric measures how long it takes for your code to execute. This is measured in seconds. A higher Execution Time indicates that your code is taking longer to execute.

## Timeit
The Timeit metric measures the average time it takes to execute a piece of code. This is useful for measuring the time complexity of specific functions or code blocks.

## cProfile
The cProfile metric measures the amount of time each function takes to execute. This is useful for identifying which functions are taking the most time to execute.
### Example
To illustrate how the Time Complexity Visualizer works, consider the following Python code:
![image](https://user-images.githubusercontent.com/125199089/226817500-ac4e020e-48d9-4e06-948e-4aef8ac4b9ed.png)
This code implements the Fibonacci sequence, which is a sequence of numbers where each number is the sum of the previous two numbers.

To visualize the time complexity of this code, we can use the Time Complexity Visualizer. We can upload the fibonacci function to the application and analyze the metrics that it generates.
The application generates the following metrics:
### Execution Time
The Execution Time of the fibonacci function is 1.230 seconds when n=35. This indicates that the function takes a considerable amount of time to execute.

### Timeit
The Timeit metric measures the time it takes to execute a piece of code. We can use it to measure the time it takes to execute the fibonacci function with different values of n. For example, the Timeit metric tells us that the fibonacci function takes approximately 1.3 microseconds to execute when n=1.

### cProfile
The cProfile metric measures the amount of time each function takes to execute. We can use it to identify which functions are taking the most time to execute. In this case, the fibonacci function is the only function in the code, so it is the only function that will be profiled
 

