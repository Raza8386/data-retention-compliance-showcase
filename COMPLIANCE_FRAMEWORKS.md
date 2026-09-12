# Compliance Frameworks Guide - Saudi Arabia & Regional Focus

## Overview

This document provides detailed information about the major compliance frameworks relevant to data retention and destruction, with focus on Saudi Arabia's regulatory environment. Each framework has specific requirements for how long data must be retained and how it should be securely deleted.

---

## 1. PDPL (Personal Data Protection Law) - Saudi Arabia

### Jurisdiction
- Kingdom of Saudi Arabia
- Applies to any organization processing personal data of Saudi residents or conducting business in KSA
- Enforced by the National Data Management Authority (NDMA)

### Key Retention Principles

**Data Minimization Principle:**
- Organizations must retain personal data only for the purposes specified
- Data collection must be necessary, relevant, and limited
- Regular review of data necessity required

**Storage Limitation:**
- Personal data must be kept in a form which permits identification no longer than necessary
- Organizations must document the retention period for each data type
- Retention periods must be justified by business or legal requirements

### Typical Retention Periods

| Data Type | Retention Period | Rationale |
|-----------|------------------|-----------|
| Customer contact info (active relationship) | Duration of relationship + 1 year | Contractual obligations |
| Customer identity verification (KYC) | Duration of relationship + 5 years | AML/KYC compliance |
| Transaction records | 5 years minimum | Financial audit/legal |
| Employee records | During employment + 3 years | Labor law requirements |
| Marketing consent data | Until consent withdrawn + 1 year | Privacy compliance |
| Website analytics data | 12 months | Service optimization |
| Customer complaint records | 3 years | Dispute resolution |
| Financial transaction logs | 7 years | Regulatory requirement |

### Deletion Requirements

**Right to Deletion:**
- Data subject can request deletion of personal data
- Organizations must respond within 30 days
- Must notify third parties of deletion request (where feasible)
- Cannot delete data subject to legal hold or legal obligation

**Secure Deletion Methods:**
- Cryptographic erasure (recommended)
- Overwrite with random data (minimum 1 pass, AES encryption preferred)
- Physical destruction with certification
- Degaussing for magnetic media
- Destruction certificate required

### Compliance Checkpoints

- [ ] Document lawful basis for data processing
- [ ] Maintain data processing records (Data Register)
- [ ] Implement privacy by design
- [ ] Train staff on PDPL requirements (annual training)
- [ ] Maintain deletion logs and audit trails with timestamps
- [ ] Have documented deletion request procedures
- [ ] Notify NDMA of any data breaches within 30 days
- [ ] Appoint Data Protection Officer (DPO) for large organizations
- [ ] Conduct Data Impact Assessments (DIA)
- [ ] Have deletion request response templates

### PDPL Penalties
- Financial penalties up to 5 million SAR
- Suspension of operations
- Public warning notices
- Compensation to affected individuals

---

## 2. NCA-ECC (National Cybersecurity Authority - Essential Cybersecurity Controls)

### Jurisdiction
- Kingdom of Saudi Arabia
- Applies to all critical infrastructure operators and essential services
- Enforced by the National Cybersecurity Authority (NCA)

### Key Retention Principles

**Data Security Framework:**
- All data must be classified and protected according to sensitivity
- Retention must align with cybersecurity requirements
- Data lifecycle management must be documented

**Security Controls:**
- Data at rest must be encrypted
- Data in transit must be encrypted
- Access to data must be logged and monitored
- Deletion must be auditable and verified

### Typical Retention Periods

| Data Type | Retention Period | Rationale |
|-----------|------------------|-----------|
| Security incident logs | Minimum 1 year | Security investigation |
| Access control logs | Minimum 1 year | Audit trail |
| Authentication records | 90 days minimum | Security compliance |
| System configuration backups | Until replaced + 30 days | Recovery capability |
| Security event logs | 12-24 months | Forensic investigation |
| Vulnerability assessment reports | 2 years | Remediation tracking |
| Network traffic logs | 90 days (sample) | Intrusion detection |
| User access audit logs | 1 year minimum | Compliance verification |

### Deletion Requirements

**Secure Deletion (NCA Control 4.4):**
- Must use cryptographically secure deletion methods
- Deletion must be logged with timestamp and user ID
- Verification of successful deletion required
- Backup copies must also be securely deleted

**Approved Deletion Methods:**
- AES 256-bit encryption with key destruction
- NIST SP 800-88 compliant degaussing
- DOD 5220.22-M (3-pass) overwrite minimum
- Certified destruction vendor with chain of custody

### Compliance Checkpoints

- [ ] Data classification policy implemented
- [ ] Encryption protocols for data at rest (AES-256 minimum)
- [ ] Encryption protocols for data in transit (TLS 1.2+)
- [ ] Access control logs maintained (minimum 1 year)
- [ ] Security incident response plan documented
- [ ] Deletion audit trails maintained
- [ ] Regular security assessments conducted
- [ ] Incident reporting to NCA within 24 hours
- [ ] Cybersecurity training for all staff
- [ ] Third-party security assessments

### NCA-ECC Monitoring
- Continuous monitoring of compliance status
- Regular audits and assessments
- Breach notification requirements
- Security controls verification

---

## 3. SAMA CSF (Saudi Arabian Monetary Authority - Cybersecurity Framework)

### Jurisdiction
- Kingdom of Saudi Arabia
- Applies to all financial institutions (banks, insurers, fintech)
- Enforced by the Saudi Arabian Monetary Authority (SAMA)

### Key Retention Principles

**Financial Data Protection:**
- Personal financial data must be retained for regulatory compliance
- Retention periods tied to financial audit requirements
- Consumer financial records must be protected to highest standard

**Regulatory Compliance:**
- Financial institutions must maintain records per SAMA requirements
- Anti-Money Laundering (AML) compliance mandatory
- Know Your Customer (KYC) requirements

### Typical Retention Periods

| Data Type | Retention Period | Rationale |
|-----------|------------------|-----------|
| Customer financial records | 7 years | SAMA regulatory requirement |
| Customer KYC documents | 7 years | AML compliance |
| Transaction records | 7 years | Audit trail |
| Customer identification | 7 years after account closure | Legal requirement |
| Account statements | 7 years | Customer service |
| Loan documents | Life of loan + 7 years | Legal enforceability |
| Compliance audit records | 7 years | Internal audit |
| Suspicious transaction reports | 10 years | AML investigation |
| Communications with customers | 5 years | Dispute resolution |
| Authorization records | 7 years | Control verification |

### Deletion Requirements

**Secure Disposal (SAMA CSF Control 5.3):**
- Must implement secure disposal procedures
- Financial data cannot be deleted if under legal hold
- Deletion must be verified and documented

**Approved Methods:**
- Cryptographic key destruction (primary method)
- AES 256-bit encryption with key secure deletion
- Certified destruction vendor with certificate of destruction
- Physical destruction with witness verification
- Degaussing with certification

**Special Considerations:**
- Deleted customer data must not be recoverable
- Deletion must not interfere with regulatory holds
- Audit trail of deletions must be maintained
- Third-party service providers must follow same standards

### Compliance Checkpoints

- [ ] 7-year retention policy documented
- [ ] AML/KYC procedures implemented
- [ ] Customer identification program (CIP) in place
- [ ] Transaction monitoring system active
- [ ] Deletion procedures comply with SAMA standards
- [ ] Encryption of customer financial data (AES-256 minimum)
- [ ] Access controls to financial data documented
- [ ] Annual compliance assessment by SAMA
- [ ] Incident reporting to SAMA (within 24 hours for critical)
- [ ] Third-party vendor contracts include data protection clauses
- [ ] Cybersecurity training for financial staff
- [ ] Audit logs of all data access (7-year retention)

### SAMA CSF Compliance Levels
- **Level 1:** Basic compliance (small institutions)
- **Level 2:** Enhanced compliance (medium institutions)
- **Level 3:** Advanced compliance (large/systemically important institutions)
- Each level requires higher security and retention standards

### SAMA Oversight
- Regular compliance examinations
- On-site assessments
- Breach notification requirements
- Financial penalties for non-compliance (up to 10M SAR)

---

## Comparison Matrix - KSA Focus

| Aspect | PDPL | NCA-ECC | SAMA CSF |
|--------|------|---------|----------|
| **Jurisdiction** | All organizations in KSA | Critical infrastructure/essential services | Financial institutions |
| **Primary Focus** | Personal data privacy | Cybersecurity | Financial security & AML |
| **Retention Philosophy** | Minimal necessary | Audit trail focused | 7-year regulatory standard |
| **Encryption Standard** | AES-256 recommended | AES-256 minimum | AES-256 minimum |
| **Deletion Right** | Yes (with limitations) | Limited (by retention period) | Limited (by AML/KYC) |
| **Breach Notification** | 30 days to NDMA | 24 hours to NCA | 24 hours to SAMA |
| **Audit Frequency** | Ad-hoc investigations | Continuous monitoring | Annual + ad-hoc |
| **Penalties** | Up to 5M SAR | Up to 50M SAR (severe cases) | Up to 10M SAR |
| **Applicable To** | Everyone in KSA | Critical infrastructure | Banks, insurers, fintech |

---

## Multi-Framework Alignment Strategy for KSA

When your organization operates under multiple KSA frameworks:

### Step 1: Create a Data Classification Matrix
```
Example: Customer transaction data
├── PDPL: Personal data = Delete after relationship + 1 year
├── SAMA CSF: Financial data = Retain 7 years (if financial institution)
├── NCA-ECC: Transaction logs = Retain 12 months for security audit
└── Business need: Keep transaction history = 5 years for customer service

DECISION: Retain for 7 years (longest requirement), 
          honor deletion requests where legally permissible
```

### Step 2: Apply the Longest Retention Period
When frameworks conflict, retain for the longest period required:

```
Financial Institution Scenario:
- PDPL requires: Minimal necessary (but unclear)
- SAMA CSF requires: 7 years for financial records
- NCA-ECC requires: 1 year for security logs
→ Retain for 7 years, then securely delete with audit trail
```

### Step 3: Document Everything Comprehensively

Maintain clear documentation of:
- Data classification per framework
- Retention periods for each data type
- Deletion procedures (PDPL compliance + encryption)
- Audit logs of all deletions (per NCA-ECC/SAMA requirements)
- Risk assessments for each framework
- Third-party vendor compliance requirements

### Step 4: Implement Technical Controls

- Automated retention schedules (by data type, not blanket)
- Encryption enforcement (AES-256 minimum)
- Role-based deletion approval (separation of duties)
- Audit trails of all deletions (immutable logs)
- Verification of successful deletion (verification reports)
- Regular backup testing (for recovery capability)

---

## Implementation Roadmap for KSA Organizations

### Phase 1: Assessment (Months 1-2)
- [ ] Determine applicable frameworks (PDPL mandatory, others if applicable)
- [ ] Audit current data retention practices
- [ ] Identify gaps in compliance
- [ ] Create data inventory per PDPL requirements

### Phase 2: Policy Development (Months 2-3)
- [ ] Create/update data retention policy (PDPL compliant)
- [ ] Define retention periods for each data type
- [ ] Create deletion procedures (AES-256 encryption)
- [ ] Develop incident response procedure
- [ ] Create DPO role (if required by size)

### Phase 3: Technical Implementation (Months 3-6)
- [ ] Deploy encryption solutions (AES-256)
- [ ] Implement automated retention schedules
- [ ] Deploy deletion tools (cryptographic erasure)
- [ ] Establish audit logging (1-year minimum)
- [ ] Test disaster recovery procedures

### Phase 4: Operationalization (Months 6-9)
- [ ] Train staff on PDPL/framework requirements
- [ ] Document procedures in operations manual
- [ ] Conduct mock deletion exercises
- [ ] Test breach notification procedures
- [ ] Establish vendor compliance monitoring

### Phase 5: Ongoing Compliance (Months 9+)
- [ ] Monthly deletion audits
- [ ] Quarterly policy review
- [ ] Annual PDPL/framework assessment
- [ ] Continuous security training
- [ ] Vendor compliance checks

---

## Audit and Verification Procedures

### Annual Compliance Review

```
1. Data Inventory Audit (PDPL Requirement)
   - Identify all personal data collections
   - Verify each data type has documented retention period
   - Confirm business/legal justification for retention
   - Audit for data older than retention period

2. Retention Schedule Audit
   - Confirm retention schedules are activated
   - Verify data is being retained correctly
   - Identify data scheduled for deletion
   - Check for expired holds/exceptions

3. Deletion Verification (NCA-ECC/SAMA CSF)
   - Sample check: verify deleted data cannot be recovered
   - Audit logs show deletion timestamp + authorized user
   - Verify encryption keys destroyed (if using crypto-erasure)
   - Confirm third-party deletions completed

4. Policy Review & Updates
   - Update for new PDPL guidance/interpretations
   - Adjust retention periods if business needs change
   - Update encryption standards (if higher required)
   - Train staff on any changes
```

### Quarterly Compliance Checklist

- [ ] No personal data retained beyond documented period
- [ ] All deletions logged with timestamp and user ID
- [ ] Encryption protocols being enforced
- [ ] No unauthorized access to personal data
- [ ] Data classification is current
- [ ] Third-party vendors remain compliant
- [ ] Backup systems also follow deletion policy
- [ ] No data in unauthorized locations

### Red Flags 🚩

- Personal data retained beyond documented period
- No audit trail for deleted data
- Encryption not enforced on sensitive data
- Missing data inventory or classification
- Third-party vendors not aligned with policy
- Inability to demonstrate deletion
- Unencrypted backups retained beyond policy
- Staff untrained on PDPL requirements

---

## Key Differences from Western Standards

| Aspect | Western (GDPR) | KSA Standards |
|--------|---|---|
| **Right to Deletion** | Strong/immediate | Subject to legal holds & AML |
| **Retention Philosophy** | Minimal | Purpose-based with minimums |
| **Regulatory Notification** | 72 hours (GDPR) | 30 days (PDPL), 24 hrs (NCA/SAMA) |
| **Encryption Mandate** | Recommended | Required (AES-256 minimum) |
| **Penalties** | % of revenue | Fixed SAR amounts |
| **DPO Requirement** | Mandatory for many | Mandatory for large organizations |
| **AML/KYC Focus** | Limited | Strong (SAMA CSF) |
| **Audit Frequency** | Event-based | Continuous monitoring (NCA) |

---

## Resources & References

### Saudi Arabia Regulatory Bodies
- [National Data Management Authority (NDMA)](https://www.ndma.gov.sa) - PDPL enforcement
- [National Cybersecurity Authority (NCA)](https://www.nca.gov.sa) - Cybersecurity standards
- [Saudi Arabian Monetary Authority (SAMA)](https://www.sama.gov.sa) - Financial sector oversight

### Official Documents
- [PDPL Law Text](https://www.ndma.gov.sa)
- [NCA-ECC Controls](https://www.nca.gov.sa/en/regulatory)
- [SAMA Cybersecurity Framework](https://www.sama.gov.sa/en/regulations)
- [AML/KYC Guidelines](https://www.sama.gov.sa/en/regulations)

### Implementation Standards
- [NIST SP 800-88 (Secure Deletion Guidelines)](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-88.pdf)
- [ISO/IEC 27001 (Information Security Management)](https://www.iso.org/standard/27001)
- [AES Encryption Standard (FIPS 197)](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197.pdf)

---

## Contact & Support

For PDPL questions: Contact your organization's Data Protection Officer or NDMA
For NCA-ECC compliance: Submit inquiries to your cybersecurity officer
For SAMA CSF compliance: Work with your institution's compliance officer

