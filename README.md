# Aviation Cybersecurity Assessment Tool

This is a straightforward guide for a cybersecurity assessment tool for aviation businesses. It examines flight operations, passenger data, and ground operations for identified operational, health and safety, and cybersecurity risks.

## Areas assessed

- **Flight Operations** - GPS spoofing, flight plan encryption, ATC security
- **Passenger Data** - personally identifiable information protections, access control; data retention
- **Aircraft systems** - WiFi isolation; avionics security; maintenance ports
- **Ground Operations** - physical security, mobile device management
- **Communications** - pilot communications encryption, satellite security

## Setup is easy

```bash
# Install requirements
pip install pandas openpyxl

# Assessment
python aviation_security_assessment.py
```

## Outcome

An excel report is generated identifying:
- Overall security score
- Items for immediate action
- Summary of findings and associated actions

Example outcome:
```
Report saved: aviation_security_assessment_20250903_143022.xlsx
Overall Security Score: 71.4%

6 items for action:
   Passenger WiFi Isolation: URGENT - WiFi extends into flight operations
   Access Control: Too many administrative accounts
```

## Why is it aviation specific?

Most cybersecurity tools ignore aviation specificities such as:
- GPS spoofing attacks on navigation of aircraft
- Passenger WiFi traffic infiltrating flight controls
- Aircraft maintenance port access
- Unsecured interface with air traffic control

## Limitations

- It is only a simulated tool (no actual network assessment)
- Educational/assessment only
- You should always consult an aviation-specific cybersecurity professional before arriving at any decisions about intended use

## Files

- `aviation_security_assessment.py` : The tool to conduct the assessment
- `README.md` : This ReadMe

The tool is designed for cybersecurity students and aviation security teams that need a rapid overview of risk.