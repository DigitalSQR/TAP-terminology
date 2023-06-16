# Managing Terminology: Process

This document elucidates a process for creating, onboarding, modifying, using, and distributing terminologies. This includes technical artifacts such as code systems, code system supplements, and value sets. Implementing a robust process is crucial to ensure consistency, traceability, and data quality.

## Glossary:
**Code Systems** are context-independent sets that provide a comprehensive list of standardized codes and meanings. Examples include SNOMED, LOINC, ATC, and ICD. 

**Code System Supplements** can contain extensions or translations of code displays. They provide additional context or localised meanings to existing codes in the Code Systems.

**Value Sets** are context-specific sets of values drawn from one or more Code Systems. They are used to specify a particular set of codes that are valid in a specific context.


## Processes
### Creation / Onboarding of Terminologies, Code Systems, Code System Supplements, or Value Sets

The journey of terminology or value sets begins with their creation or onboarding. A meticulous and robust process is crucial for effectively addressing any request or need for new terms, code systems, code system supplements, or value sets.

#### Roles and Responsibilities

Several key roles contribute to this process:

1. **Requester**: This role can be filled by anyone within the system. They can request the creation or onboarding of a new term, code system, code system supplement, or value set as per business needs.

2. **Terminology Owner**: The terminology owner oversees the process of deciding whether to onboard or create a new code system, code system supplement, or value set. They assess potential benefits, feasibility, and alignment with the organization's goals.

3. **Terminology Author**: This role is responsible for updating the terminology assets - code systems, code system supplements, or value sets. This includes adding metadata and adding/removing values.

4. **Terminology Maintainer**: This role involves the continual monitoring of terminology against the defined criteria. It involves adhering to a specified process for identifying and rectifying any inaccuracies in terminologies, based on the pre-set criteria.

### Changing Terminologies, Code Systems, Code System Supplements, or Value Sets

Terminologies, code systems, code system supplements, or value sets may need modifications or enhancements over time due to evolving business requirements or regulatory changes.

#### Roles and Responsibilities

1. **Requester**: Anyone in the group/organization can request changes to the existing terminologies, code systems, code system supplements, or value sets as per business or regulatory needs. A process should be in place for this.

2. **Terminology Owner**: As defined above, the terminology owner oversees the process of handling changes and validating them to ensure they meet the criteria.

### Usage

Effective usage and management of terminologies, code systems, code system supplements, or value sets are facilitated by having a well-maintained inventory or catalog.

1. **Artifact-Terminology Relation**: It's crucial to track which terminologies are associated with which artifacts (including their versions). This enhances traceability and helps maintain version control.
2. **Artifact-System Relation**: Understanding which systems are consuming the terminology artifacts helps manage dependencies and forecast the impact of any changes.





## Terminology Architecture

Identifying the systems involved in the creation and distribution of terminology artifacts is key. 



## Managing and Distributing Terminologies in FHIR Artifacts

Adopting FHIR artifacts for managing and distributing terminologies, code systems, code system supplements, and value sets offers numerous benefits. FHIR is a standard for health care data exchange, published by HL7.

### Advantages of Standardization

FHIR standards enable easier data sharing between healthcare applications. This allows various systems to understand and use the exchanged information without requiring extensive custom integration work.

### Terminology Servers and FHIR

Terminology servers are software tools that understand how to deal with terminologies, code systems, value sets, and concept maps in various operations, some of which are listed below:

1. **Validate-Code**: Given a code, a system, and a value set, this operation checks whether the code is in the value set.
2. **Expansion**: This operation takes a value set as input and returns a fully expanded version of it. This is especially useful for complex value sets that include large code systems or that are based on filters.
3. **Translation**: Given a code and its system (source), and a target system, this operation returns a matching code in the target system.
4. **Subsumption**: Given a pair of codes in the same system, this operation returns information about how the codes relate to each other.

These operations are standardized across different compatible terminology servers, allowing for interoperability. This not only makes managing complex terminologies more straightforward but also enables consistency and traceability across different systems and organizations.

In conclusion, the use of FHIR artifacts in managing and distributing terminologies, code systems, code system supplements, and value sets offers interoperability, flexibility, and scalability. The incorporation of terminology servers ensures effective and efficient handling of various terminology operations, leading to improved healthcare data management.
