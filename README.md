# Azure Serverless Data Processing Pipeline

This repository contains a serverless data processing pipeline built using Azure Functions and Azure SQL Database. The pipeline ingests JSON data from an HTTP endpoint, processes it, and stores the results in an Azure SQL Database.

## Table of Contents

- [About](#about)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Deployment](#deployment)
- [Usage](#usage)
  - [Testing Locally](#testing-locally)
  - [Testing on Azure](#testing-on-azure)
- [Contributing](#contributing)
- [License](#license)

## About

This project demonstrates a serverless approach to building data processing pipelines. It is designed to handle JSON data, process it, and store the results in an Azure SQL Database.

### Key Features

- **Serverless Architecture**: Powered by Azure Functions for a scalable and cost-efficient solution.
- **Real-time Data Ingestion**: Receives data via HTTP POST requests, making it suitable for various integrations.
- **Data Processing**: Includes logic to transform and clean the data before storage.
- **Azure SQL Database**: Stores the processed data for further analysis and reporting.

## Project Structure

```plaintext
azure-serverless-data-pipeline/
├── .funcignore                # Files and directories to ignore during Azure Function deployments
├── .gitignore                 # Files and directories to ignore in Git
├── README.md                  # Project documentation
├── function_app.py            # Main Azure Function script
├── host.json                  # Global configuration options for all functions
├── local.settings.json        # Local settings for running the function locally
└── requirements.txt           # Python dependencies
```

## Getting Started

### Prerequisites

- **Python 3.8+**: Ensure Python is installed on your machine.
- **Azure Account**: You need an Azure account to deploy resources.
- **Azure CLI**: Install the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) for deploying and managing Azure resources.
- **Azure Functions Core Tools**: Install the [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local) for local development and testing.

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/azure-serverless-data-pipeline.git
   cd azure-serverless-data-pipeline
   ```

2. **Install Python dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. **Azure SQL Database**: 
   - Create an Azure SQL Database through the Azure Portal.
   - Set up the required tables for storing processed data.

2. **Azure Function Configuration**:
   - Update the `function_app.py` file with your Azure SQL Database connection details.

   ```python
   conn_str = (
       "Driver={ODBC Driver 17 for SQL Server};"
       "Server=tcp:<your_server>.database.windows.net,1433;"
       "Database=<your_database>;"
       "Uid=<your_username>;"
       "Pwd=<your_password>;"
       "Encrypt=yes;"
       "TrustServerCertificate=no;"
       "Connection Timeout=30;"
   )
   ```

3. **Local Settings**:
   - The `local.settings.json` file is used for running the Azure Function locally. Update it with your storage connection string if needed.

## Deployment

### Deploying to Azure

1. **Login to Azure**:

   ```bash
   az login
   ```

2. **Deploy the Function App**:

   ```bash
   az functionapp create --resource-group <your-resource-group> --consumption-plan-location <your-location> --runtime python --functions-version 3 --name <your-function-name> --storage-account <your-storage-account>
   ```

3. **Deploy the code**:

   ```bash
   func azure functionapp publish <your-function-name>
   ```

## Usage

### Testing Locally

1. **Start the Azure Function locally**:

   ```bash
   func start
   ```

2. **Send a POST request with JSON data**:

   Use a tool like [Postman](https://www.postman.com/) or `curl`:

   ```bash
   curl -X POST http://localhost:7071/api/<your-function-name> -H "Content-Type: application/json" -d @sample_input.json
   ```

3. **Check the output**:
   - The function should process the data and insert it into your local or remote Azure SQL Database.

### Testing on Azure

1. **Send a POST request to the deployed function**:

   ```bash
   curl -X POST https://<your-function-name>.azurewebsites.net/api/<your-function-name> -H "Content-Type: application/json" -d @sample_input.json
   ```

2. **Monitor the Function**:
   - Use Azure Monitor or Application Insights to monitor the execution and performance of the deployed function.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
