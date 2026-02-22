# Cybersecurity Escape Rooms Portfolio - 1st Class Grade Achieved


# Executive Summary

This project consists of three practical cybersecurity tasks completed within a controlled academic lab environment:

- **Task 1 - Social Engineering Password Patterns**
- **Task 2 - Wiretap the Secret (Packet Capture Forensics)**
- **Task 3 - Membership Inference Attack**

Each task focused on a different area of cybersecurity:

- Authentication security and password weaknesses  
- Network traffic analysis and credential exposure  
- Machine learning privacy and data leakage  

Across all tasks, a structured investigative approach was taken, combining technical execution, documentation, analysis, and ethical reflection.

---

# Task 1 - Social Engineering Password Patterns

## Objective

To exploit predictable password patterns using personal information and automate credential discovery against a local authentication server.

## Lab Setup

- Environment: Local isolated lab  
- Server: Flask-based authentication server (`127.0.0.1:5000`)  
- APIs tested:
  - `/api/level1`
  - `/api/level2`
- Data source: `Employee Profile.txt`
- Tools used: Python, NLTK, Requests, Flask test server  

Testing was strictly limited to the provided environment.

---

## Methodology

### Term Extraction

Relevant words and numbers were extracted from the employee profile using a scripted NLP-based approach. English stopwords were removed to produce a refined list of meaningful terms.

### Credential Generation

Username and password combinations were generated according to the defined rules for both levels.

### Brute-Force Execution

A Python script iterated through valid combinations and submitted POST requests to the appropriate API endpoint until valid credentials were discovered.

### Result Analysis

Time taken, number of attempts, and password structure were analysed to evaluate attack feasibility.

---

## Key Findings

- Personal information significantly reduces password entropy.
- Predictable naming patterns increase vulnerability.
- Lack of rate limiting enables automated attacks.
- Password design decisions directly impact exploitability.

---

# Task 2 - Wiretap the Secret (Packet Capture Forensics)

## Objective

To analyse captured network traffic and extract sensitive information from unencrypted communications.

## Lab Setup

- Application: Fignal internal messaging platform  
- Traffic capture: Wireshark (loopback interface)  
- Server IP: `127.0.0.1`  
- Listening Port: `61441`  
- Tools used:
  - Wireshark
  - Display filters
  - Follow TCP Stream
  - Excel
  - PowerShell  

Analysis was restricted to the authorised lab environment.

---

## Methodology

- Captured live network traffic while the client generated authentication and messaging activity.
- Applied display filters to isolate HTTP traffic.
- Inspected packet payloads.
- Reassembled TCP streams.
- Extracted credentials and message contents.
- Documented observed vulnerabilities.
- Designed mitigation strategies.

---

# Task 3 – Membership Inference Attack

## Objective

To determine whether specific data records were part of a machine learning model’s training dataset.

## Lab Setup

- Environment: Python (Windows)
- Framework: PyTorch
- Dataset: CIFAR-10
- Tools used:
  - PyTorch
  - Torchvision
  - NumPy
  - scikit-learn
  - tqdm  

The experiment followed a standard:

Shadow model → Attack model → Evaluation pipeline

---

## Methodology

1. Trained shadow models to mimic the target model’s behaviour.
2. Extracted loss values and prediction correctness as features.
3. Trained an attack classifier to distinguish:
   - IN (training members)
   - OUT (non-members)
4. Identified dataset imbalance.
5. Balanced IN and OUT samples.
6. Re-evaluated attack performance.

---

# Conclusion

This portfolio integrates authentication attacks, network forensics, and machine learning privacy analysis within structured investigative workflows.

Across all tasks:

- Threat models were defined clearly.
- Methodologies were iterative and evidence-based.
- Failures informed refinement and improvement.
- Technical findings were documented systematically.
