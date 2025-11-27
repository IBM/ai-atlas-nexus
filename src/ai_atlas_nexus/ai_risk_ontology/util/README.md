## Helper scripts for LinkML conversion

The following scripts are available to convert some of the source data to LinkML instance data YAML files:

- `mitriskrepo2linkml.py`: Convert the MIT risk taxonomy data from CSV format (`resources\TheAIRiskRepositoryV1_16_8_24.csv`) to LinkML YAML
- `nistactions2linkml.py`: Convert the NIST AI RMF actions data from CSV format (`resources\actions_extracted_from_nist.csv`) to LinkML YAML
- `nistUpdateLinkmlWithActions.py`: Updates the existing NIST RMF data YAML by adding the related actions to each risk entity
- `importRiskMappings.py`: Reads the SSSOM TSV files describing the risk-to-risk mappings and converts those into LinkML YAML
