# Mass Pdf Downloader

## instalation

- Follow the steps below to install and run the Mass PDF Downloader:

### 1. Install Required Libraries
Run these scripts in the terminal one by one:
```shell
pip install requests tqdm
```

```shell
pip install pyinstaller
```

### 2. Build the Executable
Run this command to build the executable file:
```shell
pyinstaller --onefile download_pdfs.py
```

### 3. Running the Script Directly (Optional)
You can also run the Python script directly without building the executable:
```shell
python download_pdfs.py
```

### Post-Build Steps
- Once the build is finished, you will find the executable file in the ./dist folder.
- To run the app, you need to put a urls.json file in the same folder where the executable file is placed.
- Fill the urls.json file with PDF URLs and open the .exe file.
- After the download is completed, a folder with the PDFs will automatically open.

## Usage
### Creating the urls.json File
Create a file named urls.json in the same directory as the executable, with the following structure:

```json
{
  "urls": [
    "http://example.com/file1.pdf",
    "http://example.com/file2.pdf"
    // Add more URLs here
  ]
}
```
### Replace the URLs with the actual PDF URLs you want to download.

Running the Application
Simply double-click the executable file or run it from the terminal. The application will download all the PDFs specified in the urls.json file and then open the directory containing the downloaded files.
