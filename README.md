# Invoice Scraper
A Python-based scraper that navigates through a target folder of invoices, extracts client information, and saves it to an Excel sheet. Created for a truck dealership client.

<a id="readme-top"></a>

[![MIT license][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

---

## About The Project

This script was created to assist a truck dealership in organizing client data from their file system of invoices. It identifies PDF invoices, extracts client details such as names and addresses, and compiles the results into an easy-to-read Excel sheet.

### Features:
1. **File System Navigation**: Parses a structured directory of truck sales data.
2. **Invoice Processing**: Extracts relevant information from invoice PDFs.
3. **Data Compilation**: Saves the extracted client information to an Excel sheet.
4. **Duplication Prevention**: Avoids processing duplicate client data.

### Example File System
```plaintext
.
├── 2024
│   ├── truck70
│   │   ├── log.txt
│   │   ├── invoice.pdf
│   │   ├── truck.jpg
│   ├── truck65
│   │   ├── log.txt
│   │   ├── invoice1.pdf
│   │   ├── invoice2.pdf
│   │   ├── truck.jpg
│   └── notes.txt
├── 2023
├── 2022
└── year
    └── truck + number folder
        └── file.txt
```

---

## Getting Started

This project can be set up locally.
To get a local copy up and running, follow these steps:

### Prerequisites
- Python 3.8+
- Required Python packages:
  - `argparse`
  - `openpyxl`
  - `pypdf`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/eghosaohenhen/invoice-scraper.git
   ```

2. Navigate to the project directory:
   ```bash
   cd invoice-scraper
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Change the Git remote URL (optional):
   ```bash
   git remote -v # Check current remote
   git remote set-url origin <NEW_GIT_URL_HERE>
   git remote -v # Confirm the changes
   ```

---

## Usage

### Run the Script
Use the following command to run the script:
```bash
python main.py --root <ROOT_DIRECTORY> --output <OUTPUT_DIRECTORY> --name <OUTPUT_FILENAME>.xlsx
```

### Parameters:
- `--root`: The root directory containing invoice files.
- `--output`: The directory to save the Excel file and client data.
- `--name`: The name of the Excel file (must end in `.xlsx`).
- `--test` (optional): Run in test mode to process a limited number of invoices.

### Flags and Their Purposes:
- **`--root`**: Specifies the directory where the script will search for invoices.
- **`--output`**: Sets the directory where the resulting Excel file and client data will be saved.
- **`--name`**: Names the Excel file output, which must have a `.xlsx` extension.
- **`--test`**: Enables test mode, allowing the script to process a smaller subset of files for debugging or validation purposes.

### Example:
```bash
python main.py --root /path/to/files --output /path/to/output --name client_data.xlsx
```

For instance, to process invoices stored in `/home/user/invoices` and save the output to `/home/user/results` as `clients.xlsx`, run:
```bash
python main.py --root /home/user/invoices --output /home/user/results --name clients.xlsx
```

---

## Roadmap

- [ ] Add support for additional invoice formats.
- [ ] Implement advanced filtering options.
- [ ] Create a web-based UI for user interaction.
- [ ] Add automated unit tests for core functions.

---

## Built With

- **Python**: Primary language for scripting.
- **argparse**: For command-line argument parsing.
- **openpyxl**: For creating and managing Excel files.
- **pypdf**: For extracting data from PDF files.

---

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<!-- MARKDOWN LINKS & IMAGES -->
[license-shield]: https://img.shields.io/github/license/eghosaohenhen/invoice-scraper.svg?style=for-the-badge
[license-url]: https://github.com/eghosaohenhen/invoice-scraper/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
