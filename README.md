# NFe Downloader

This is a Python script that automates the download of electronic invoices (NF-e) from the Brazilian government's website. The script uses Selenium to navigate the website and download the invoices in PDF format.

## Requirements

- Python 3.x
- Selenium
- ChromeDriverManager
- Google Chrome

## Installation

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/matheustkaczyk/bot_nf_integrated_csharp.git
   ```

2. Install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

3. Install Google Chrome if it is not already installed on your machine.
   
4. Set the following environment variables with the appropriate values for your company:
  - CPF: Your CPF (Brazilian individual taxpayer registry) number.
  - SENHA: Your password for the government's website.
  - CEP: The ZIP code of your company's address.
  - NCM: The NCM (Nomenclature of the Mercosur Common Market) code for your products.
  - CFOP: The CFOP (Tax Code for Operations and Services) code for your products.
  - UNIDADE: The unit of measurement for your products.
  - URL: The URL of the government's website for downloading invoices.
  - RUA: The name of the street where your company is located.
  - BAIRRO: The name of the neighborhood where your company is located.
  - NUMERO: The number of the address where your company is located.
  - DESCRICAO3KG: The description of your 3kg product.
  - CODIGO3KG: The code of your 3kg product.
  - DESCRICAO5KG: The description of your 5kg product.
  - CODIGO5KG: The code of your 5kg product.
  - PAGAMENTO: The payment method for your invoices.
  - FORMAPAGAMENTO: The payment form for your invoices.

  For example, you can set the envorinment variables in a .env file like this:
  ```
    CPF=12345678900
    SENHA=mysecretpassword
    CEP=12345678
    NCM=12345678
    CFOP=123456
    UNIDADE=UN
    URL=https://www.nfe.fazenda.gov.br/portal/consulta.aspx?tipoConsulta=completa&tipoConteudo=XbSeqxE8pl8=
    RUA=MyStreet
    BAIRRO=MyNeighborhood
    NUMERO=123
    DESCRICAO3KG=My 3kg Product
    CODIGO3KG=123456
    DESCRICAO5KG=My 5kg Product
    CODIGO5KG=789012
    PAGAMENTO=My Payment Method
    FORMAPAGAMENTO=My Payment Form
  ```

## Usage

1. Open a terminal or command prompt and navigate to the directory where you cloned the repository.

2. Run the script with the following command:

   ```
   python main.py <CNPJ-FANTASY_NAME-IE-ADDRESS_NAME-ADDRESS_NUMBER-ADDRESS_NEIGHBORHOOD-QUANTITY3-VALUE3-QUANTITY5-VALUE5>
   ```

   Replace the `<CNPJ>`, `<FANTASY_NAME>`, `<IE>`, `<ADDRESS_NAME>`, `<ADDRESS_NUMBER>`, `<ADDRESS_NEIGHBORHOOD>`, `<QUANTITY3>`, `<VALUE3>`, `<QUANTITY5>`, and `<VALUE5>` placeholders with the appropriate values for your company.

   For example:

   ```
   python main.py 12.345.678/0001-90-MyCompany-123456789-MyStreet-123-MyNeighborhood-1-100.00-2-200.00
   ```

3. The script will open a headless Chrome browser and navigate to the government's website to download the invoices.

4. The downloaded invoices will be saved in the Downloads folder with a custom file name based on the company name and the current date and time.

5. If you want to call the script from a C# application, you can use the following `startProcess()` method as an example:

   ```csharp
   private void startProcess()
   {
       ProcessStartInfo processInfo = new ProcessStartInfo();
       processInfo.FileName = scriptName;
       processInfo.Arguments = $"\"{textBoxCnpj.Text}-{textBoxNomeFantasia.Text}-{textBoxInscricaoEstadual.Text}-{textBoxLogradouro.Text}-{textBoxNumero.Text}-{textBoxBairro.Text}-{textBoxQuantidade3.Text}-{textBoxValor3.Text}-{textBoxQuantidade5.Text}-{textBoxValor5.Text}\"";
       Process process = Process.Start(processInfo);
   }
   ```

   This method creates a new `ProcessStartInfo` object and sets the `FileName` property to the name of the Python script. It then sets the `Arguments` property to a string that includes the values of the text boxes in your C# application. Finally, it starts the process using the `Process.Start()` method.

## UI
If you prefer to use a visual interface to pass the arguments to the Python script, you can use the following GitHub repository:

https://github.com/matheustkaczyk/GELO_SAO_MATEUS_EMISSOR_NF.git

This repository contains a C# Windows Forms application that provides a visual interface for passing the arguments to the main.py script. To use the UI, you will need to clone the repository and build the application and link the following script as explained inside the application:

1. Create a .bash file:
```
@echo off

CD C:\path_to_python_script

for /f "tokens=* delims= " %%a in ("%*") do ( python src/main.py %%a )
```

2. Link the bash script inside the UI application (Default directory: Documents/Scripts/emit_c#.bat)
