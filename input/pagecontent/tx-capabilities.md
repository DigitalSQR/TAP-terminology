Terminology services and servers

An overview of the technical capabilities of several servers is available in this link:

https://confluence.ihtsdotools.org/display/FHIR/Features+of+Known+Servers


There are several other terminology servers. Some servers designed for healthcare usage:

| Terminology Server | Organization | License | Open Source | Source URL | Usage | Description |
|----------------------|-----------------------|-----------------|--------------|--------------------------------------------------|---------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Snowstorm | Apelon | Apache 2.0 | Yes | [GitHub](https://github.com/IHTSDO/snowstorm) | N/A | Snowstorm is a SNOMED CT terminology server, designed for managing and distributing SNOMED CT content.|
| CTS2 | HL7 | Apache 2.0 | Yes | [GitHub](https://github.com/cts2/cts2-framework) | N/A | CTS2 (Common Terminology Services 2) is a standard for representing and accessing terminologies. |
| HAPI FHIR | Smile CDR | Apache 2.0 | Yes | [GitHub](https://github.com/smart-on-fhir/hapi-fhir) | N/A | HAPI FHIR is a FHIR terminology server built on the HAPI framework, supporting HL7 FHIR standard for healthcare data exchange. |
| FHIR Terminology Server | Health Intersections | Apache 2.0 | Yes | [GitHub](https://github.com/HealthIntersections/fhirserver) | Mostly in FHIR tooling | FHIR Terminology Server is a FHIR-centric terminology server supporting FHIR's ValueSet, CodeSystem, and ConceptMap resources. |
| Ontoserver | Monash University | Apache 2.0 | Yes | [GitHub](https://github.com/ontoserver/ontoserver) | N/A | Ontoserver provides a standards-based way of accessing, authoring, and managing healthcare terminologies and code systems.|
| UTG| U.S. National Library of Medicine | Public Domain | Yes | [GitHub](https://github.com/UnofficialTermGap/UTG) | N/A | The Unified Medical Language System (UMLS) Terminology Services (UTS) provides APIs to access UMLS content and Metathesaurus data.|
| BioPortal | Stanford University | Apache 2.0 | Yes | [GitHub](https://github.com/NCBO/ncbo_annotator) | N/A | BioPortal is an open repository of biomedical ontologies and terminologies, offering web services and APIs for terminology access. |
| TermMed | TermMed | Proprietary | No | N/A | N/A | TermMed offers medical terminology services and tools for managing clinical and administrative healthcare terminologies.|




### Terminology Servers and Services

Terminology servers are software tools that understand how to deal with terminologies, code systems, value sets, and concept maps in various operations, some of which are listed below:

1. **Validate-Code**: Given a code, a system, and a value set, this operation checks whether the code is in the value set.
2. **Expansion**: This operation takes a value set as input and returns a fully expanded version of it. This is especially useful for complex value sets that include large code systems or that are based on filters.
3. **Translation**: Given a code and its system (source), and a target system, this operation returns a matching code in the target system.
4. **Subsumption**: Given a pair of codes in the same system, this operation returns information about how the codes relate to each other.

These operations are standardized across different compatible terminology servers, allowing for interoperability. This not only makes managing complex terminologies more straightforward but also enables consistency and traceability across different systems and organizations.

In conclusion, the use of FHIR artifacts in managing and distributing terminologies, code systems, code system supplements, and value sets offers interoperability, flexibility, and scalability. The incorporation of terminology servers ensures effective and efficient handling of various terminology operations, leading to improved healthcare data management.
