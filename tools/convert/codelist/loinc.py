import requests
import json

base_url = "https://tx.fhir.org/r4/CodeSystem/$lookup"
value_set = {
    "resourceType": "ValueSet",
    "status": "active",
    "compose": {
        "include": [
            {
                "system": "http://loinc.org",
                "concept": []
            }
        ]
    }
}

# Read codes from file
with open("codes.txt", "r") as codes_file:
    codes = [line.strip() for line in codes_file]

not_found_codes = []

# Iterate through the codes and perform FHIR lookup
for code in codes:
    params = {
        "system": "http://loinc.org",
        "code": code,
        "_format": "json"  # Adding the _format parameter
    }

    response = requests.get(base_url, params=params)

    try:
        data = response.json()

        if response.status_code == 200:
            if data.get("parameter"):
                # Code found, add it to the value set
                value_set["compose"]["include"][0]["concept"].append({
                    "code": code
                })
                print(f"Code {code} found. Added to value set.")
            else:
                # Code not found
                not_found_codes.append(code)
                print(f"Code {code} not found.")
        else:
            # Error occurred during the request
            print(f"Error occurred while looking up code {code}. Status code: {response.status_code}")

    except requests.exceptions.JSONDecodeError:
        # Error decoding JSON response
        print(f"Error decoding JSON for code {code}. Response content: {response.content}")

# Save value set as JSON file
with open("valueset.json", "w") as valueset_file:
    json.dump(value_set, valueset_file, indent=2)

# Write not found codes to file
with open("notfound.txt", "w") as not_found_file:
    for code in not_found_codes:
        not_found_file.write(f"{code}\n")
