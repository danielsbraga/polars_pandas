# Polars vs Pandas: Boost Your ETL Performance

Handling large volumes of data in real-time presents significant challenges in terms of productivity and time management. Efficient solutions are crucial for data scientists working with BIG DATA, especially in complex ETL (Extract, Transform, Load) processes. This repository provides a comprehensive comparison between Polars and Pandas and some important funstions of both libraries, demonstrating how Polars can enhance data processing efficiency by up to 95%.

## Table of Contents
1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Detailed Test Results and Usage](#detailed-test-results-and-usage)
4. [File Descriptions](#file-descriptions)
5. [Contributing](#contributing)
6. [License](#license)
7. [Connect](#connect)

## Introduction

As a data scientist working with Python, managing BIG DATA can be daunting. The large volumes of data involved required a more efficient and less complicated solution.

**🤔 Just Use Pandas! Right?**

Many data scientists rely on Pandas for data processing and manipulation. While it's an essential tool, it can struggle with BIG DATA in complex ETL pipelines.

**🐻‍❄️ Discovering Polars**

That's when I found Polars. Despite its similar name, Polars is incredibly powerful and efficient, [claiming up to 30x better performance in data querying and manipulation]([url](https://pola.rs/posts/benchmarks/)).
I'm not sure about this results, so i dicided to create a repository that i could text both Pnadas and Polars in my machine.

## Getting Started

To get started with Polars and see the performance comparisons yourself, follow these steps:

1. **Clone the Repository**
    ```sh
    git clone https://github.com/danielsbraga/polars_pandas.git
    ```

2. **Install Dependencies**
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the Comparison Tests**
    ```sh
    python compare_polars_pandas.py
    ```

## Detailed Test Results and Usage

💪 **How Powerful is Polars? Here's What I Found**

I conducted several tests to compare Polars and Pandas, and here are the key findings:

- **Code Similarity**: Methods like `read_csv()`, `head()`, etc., are very similar between the two libraries, making it easy for Pandas users to transition to Polars.
- **Data Visualization**: The visualization of tables (DataFrame and Series) is almost the same, but Polars offers a clearer representation in some cases.
- **Ease of Transformation**: You can transform a DataFrame from Pandas to Polars and vice-versa with a single command.
- **Performance**: Polars outperformed Pandas in all performance-related tasks involving data queries:
  - Data Loading: 83% faster
  - Filtering: 72% faster
  - Aggregation: 45% faster
  - JOIN operations: 93% faster
  - Data Transformation: 95% faster
  - Sorting: 63% faster
  - Window Functions: 94% faster

🔎 Check the detailed test results and learn how to use the basic commands of Polars in the [notebooks](notebooks/) directory.

## File Descriptions

- **CrimeDataFetcherETL.py**: Script for fetching and processing crime data in the ETL pipeline.
- **CrimeDataProcessing.ipynb**: Jupyter notebook for processing crime data and performing various data analysis tasks.
- **LICENSE**: The MIT license file for the project.
- **PandasAndPolarsPerformanceEvaluation.ipynb**: Jupyter notebook containing the performance evaluation tests between Pandas and Polars.
- **PerformanceEvaluator.py**: Script to evaluate and compare the performance of data processing tasks between Pandas and Polars.
- **README.md**: This README file.

## Contributing

Contributions are welcome! If you have any improvements or suggestions, please submit a pull request or open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Connect

❓ Have you used Polars before? Do you think it will eventually replace Pandas? Share your thoughts!

---

Feel free to reach out if you have any questions or need further assistance!
