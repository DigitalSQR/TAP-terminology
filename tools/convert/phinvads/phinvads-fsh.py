import csv
import json
import sys
from collections import defaultdict

def convert_to_fsh_and_fhir(input_file):
    fsh_output = []
    fhir_output = {}

    with open(input_file, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        lines = list(reader)

    # Extract value set info
    value_set_info = lines[0]
    value_set_data = lines[1]

    # Alias mapping to URL needs to be predefined or needs a logic to generate it
    alias_url_mapping = {
        "LOINC": "http://loinc.org"
        # Add more if needed
        # "CodeSystemName": "CodeSystemURL"
    }

    fsh_output.append("Alias: {} = {}\n".format(value_set_data[5], alias_url_mapping.get(value_set_data[5], "")))
    fsh_output.append("ValueSet: {}\n".format(value_set_data[1]))
    fsh_output.append("Id: {}\n".format(value_set_data[1]))
    fsh_output.append('Title: "{}"\n'.format(value_set_data[0]))
    fsh_output.append('Description: "{}."\n'.format(value_set_data[4]))
    fsh_output.append("* ^copyright = \"{}\"\n".format(value_set_data[5]))

    # Init FHIR ValueSet
    fhir_output = {
        "resourceType": "ValueSet",
        "id": value_set_data[1],
        "url": "http://example.com/ValueSet/{}".format(value_set_data[1]),
        "name": value_set_data[0],
        "status": "active",
        "description": value_set_data[4],
        "compose": {
            "include": []
        }
    }

    # Create a dict to group concepts by their code system
    concepts_by_system = defaultdict(list)

    # Skip empty lines and header
    lines = lines[4:]

    for line in lines:
        if line[0] != '':
            if line[5] not in alias_url_mapping:
                raise ValueError(f'Error: Code System {line[5]} not found in alias mapping.')
            fsh_output.append("* {}#{}\n".format(line[5], line[0]))

            # Add to the group
            concepts_by_system[line[5]].append({
                "code": line[0],
                "display": line[2]
            })

    # Add grouped concepts to FHIR ValueSet
    for system, concepts in concepts_by_system.items():
        fhir_output["compose"]["include"].append({
            "system": alias_url_mapping[system],
            "concept": concepts
        })

    # Write the outputs
    output_base = input_file.rsplit('.', 1)[0]
    with open(output_base + '.fsh', 'w') as f:
        for line in fsh_output:
            f.write(line)
    with open(output_base + '.json', 'w') as f:
        f.write(json.dumps(fhir_output, indent=2))

    print("FSH and FHIR conversion complete!")

# Get input filename from command line arguments, default to provided filename
input_file = sys.argv[1] if len(sys.argv) > 1 else 'PHVS_MicrobiologyLabTestResultName_CDC_V5.txt'
convert_to_fsh_and_fhir(input_file)
