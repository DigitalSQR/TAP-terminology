# FSH and FHIR ValueSet Converter

This Python script converts a tab-separated value file into FSH (FHIR Shorthand) and FHIR ValueSet formats.

## Usage

```bash
python convert.py [input_file]
```

Replace `[input_file]` with the name of your input file. If you don't provide an input file, the script will default to 'PHVS_MicrobiologyLabTestResultName_CDC_V5.txt' for a demo.

The script will generate two output files: an `.fsh` file and a `.json` file. These files will have the same base name as the input file.

The script requires assumes that the input file has a specific format as per the current (July 2023) format used in [PHIN VADS value sets](https://phinvads.cdc.gov/vads/SearchVocab.action) download in .txt format. The first few lines should provide metadata about the ValueSet, including its name, code, and description. After a blank line, the rest of the file should list the concepts in the ValueSet, including their code, name, and the system they belong to.

## Note
The script currently only supports the LOINC code system. If you want to use other code systems, you'll need to add them to the alias_url_mapping dictionary in the script.
