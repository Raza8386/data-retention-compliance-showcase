# Quick Reference Guide - Data Retention & Destruction

## 🚀 Quick Start (5 Minutes)

### For Data Classification
```bash
python SCRIPTS/classify_data.py --input data_inventory.csv --output classified_data.csv --framework PDPL
```

### For Secure Deletion
```bash
python SCRIPTS/secure_deletion.py --file sensitive_data.txt --method dod_5220_22m --verify
```

### For Retention Management
```bash
python SCRIPTS/retention_manager.py --inventory data_inventory.csv --analyze --report compliance_report.html
```

---

## 📋 Retention Periods by Framework

### PDPL (Personal Data Protection Law)
| Data Type | Retention | Trigger |
|-----------|-----------|---------|
| Customer contact info | 1 year after relationship ends | Relationship termination |
| Customer KYC/Identity | 5 years | Regulatory requirement |
| Marketing data | Until opt-out + 1 year | Consent withdrawal |
| Employee records | 3 years after separation | Separation date |
| Financial records | 5-7 years | Tax/legal requirement |

### NCA-ECC (Cybersecurity Controls)
| Log Type | Retention | Purpose |
|----------|-----------|---------|
| Security logs | 12-24 months | Incident investigation |
| Access logs | 12 months | Audit trail |
| Audit logs | 2+ years | Compliance verification |
| Configuration backups | Until replaced + 30 days | Recovery capability |

### SAMA CSF (Financial Sector)
| Record Type | Retention | Framework |
|-------------|-----------|-----------|
| Customer KYC | 7 years | Non-negotiable |
| Transaction records | 7 years | Regulatory requirement |
| Financial data | 7 years | AML/KYC compliance |
| Suspicious activity reports | 10 years | Investigation purposes |

---

## 🔐 Encryption Standards

### Minimum Requirements
- **Data at Rest:** AES-256 encryption
- **Data in Transit:** TLS 1.2+ (minimum)
- **Key Management:** Secure HSM or Key Vault
- **Encryption Keys:** Rotate annually minimum

### Recommended Configuration
```sql
-- Enable database encryption
ALTER TABLE sensitive_data ENCRYPTION='AES-256';

-- For cloud storage (AWS example)
aws s3api put-bucket-encryption \
  --bucket my-bucket \
  --server-side-encryption-configuration '{...}'
```

---

## 🗑️ Deletion Methods Comparison

| Method | Passes | Time | Compliance | Best For |
|--------|--------|------|-----------|----------|
| Crypto Erase | 1 | Fast | ✅ All frameworks | Cloud, modern systems |
| DOD 5220.22-M | 3 | Medium | ✅ All frameworks | Standard compliance |
| Gutmann | 35 | Slow | ✅ All frameworks | Highly sensitive data |
| NIST SP 800-88 | 1 | Fast | ✅ All frameworks | NIST-compliant systems |

**Recommended:** Start with `crypto_erase` for most organizations, upgrade to `dod_5220_22m` for sensitive data.

---

## ✅ Compliance Checklist

### Monthly
- [ ] Data inventory audit (check for new data sources)
- [ ] Verify scheduled deletions executed
- [ ] Review deletion audit logs
- [ ] Check for overdue data

### Quarterly
- [ ] Compliance review meeting
- [ ] Update retention policy if needed
- [ ] Vendor compliance assessment
- [ ] Staff training refresher

### Annually
- [ ] External audit
- [ ] Policy review and update
- [ ] Encryption key rotation
- [ ] Disaster recovery testing

---

## 🚨 Red Flags (Immediate Action Required)

🔴 **CRITICAL:**
- Data retained beyond documented period
- No encryption on classified data
- Missing deletion audit logs
- Third-party vendors not compliant

🟠 **HIGH:**
- Low staff training completion
- Encryption keys not rotated
- No legal hold procedures
- Backup systems not following policy

🟡 **MEDIUM:**
- No automated retention schedules
- Incomplete data classification
- Staff turnover without handover
- Outdated policy documentation

---

## 📞 Key Contacts

| Role | Responsibility | Contact |
|------|-----------------|---------|
| Data Protection Officer | Overall compliance | [Email/Phone] |
| Compliance Officer | Policy enforcement | [Email/Phone] |
| IT Security Lead | Encryption/deletion tools | [Email/Phone] |
| Legal Advisor | Legal holds, litigation | [Email/Phone] |
| Department Heads | Data stewardship | [Email/Phone] |

---

## 🔍 Audit Log Format

Every deletion must be logged with:
```
Timestamp: 2026-09-12 02:15:00 UTC
User: admin@company.com
Action: DELETE
Table: customers
Records: 1,243
Method: crypto_erase
Verification: SUCCESS
Reason: Expired KYC records (5+ years)
```

---

## 📊 Dashboard Metrics

**Track These KPIs:**
- Compliance Score (target: 95%+)
- Data Classified %: (target: 100%)
- On-time Deletions %: (target: 100%)
- Incident Response Time: (target: <24 hours)
- Policy Update Frequency: (target: annual)

---

## 🎓 Training Checklist

**All Staff (Annual):**
- [ ] PDPL/NCA-ECC/SAMA CSF overview
- [ ] Why data retention matters
- [ ] Your role in compliance
- [ ] Quiz: 80% pass required

**Data Custodians (Quarterly):**
- [ ] Classification decision tree
- [ ] Retention policy details
- [ ] Deletion request process
- [ ] Audit log review

**IT/Security (Semi-Annual):**
- [ ] Encryption best practices
- [ ] Deletion tool operation
- [ ] Key management procedures
- [ ] Incident response

**Legal/Finance (Annual):**
- [ ] Legal hold procedures
- [ ] Litigation support
- [ ] eDiscovery requirements
- [ ] Record preservation

---

## 💾 Backup & Recovery

**Important:** Backups also follow retention policy!

```
Deletion Date: 2026-09-12
Data Deleted: Customer records
Backup Retention: 30 days after deletion (until 2026-10-12)
Then: Backup also securely deleted
```

---

## 🛠️ Troubleshooting

### Deletion Fails
1. Check if legal hold applied
2. Verify file permissions
3. Check disk space
4. Review deletion tool logs

**Solution:**
```bash
# Check legal hold status
SELECT * FROM legal_holds WHERE record_id = 'xxx';

# Remove if not needed
DELETE FROM legal_holds WHERE record_id = 'xxx';

# Retry deletion
python SCRIPTS/secure_deletion.py --file data.txt --method dod_5220_22m
```

### Data Not Classified
1. Run classification script
2. Manual review for edge cases
3. Update classification schema if needed

**Solution:**
```bash
python SCRIPTS/classify_data.py --input inventory.csv --output classified.csv
```

### Encryption Key Lost
⚠️ **CRITICAL:** Cannot recover encrypted data without key!

**Prevention:**
- Store keys in HSM (Hardware Security Module)
- Maintain key backup in secure vault
- Regular key access testing
- Document key recovery procedures

---

## 📈 Maturity Progression

### Level 1: Basic Compliance
- ✅ Written policy exists
- ✅ Manual deletion process
- ⚠️ Encryption partially implemented
- ⚠️ Audit logging manual

**Timeline:** Month 1

### Level 2: Automated Compliance
- ✅ Automated retention schedules
- ✅ Encryption enforced
- ✅ Deletion verification
- ⚠️ Limited audit capabilities

**Timeline:** Month 3

### Level 3: Advanced Compliance
- ✅ AI-powered classification
- ✅ Real-time monitoring
- ✅ Predictive deletion
- ✅ Comprehensive audit trails

**Timeline:** Month 6+

---

## 🔗 External Resources

### Regulatory Bodies
- **NDMA:** https://www.ndma.gov.sa (PDPL guidance)
- **NCA:** https://www.nca.gov.sa (Cybersecurity)
- **SAMA:** https://www.sama.gov.sa (Financial regulation)

### Technical Standards
- **NIST SP 800-88:** Secure deletion guidelines
- **ISO/IEC 27001:** Information security management
- **AES FIPS 197:** Encryption standard

### Tools & Software
- HashiCorp Vault: Key management
- AWS KMS: Cloud encryption
- BitLocker: Windows encryption
- LUKS: Linux encryption

---

## 📝 Common Questions

**Q: How long should I keep backups?**
A: Same as primary data + 30 days. Then securely delete.

**Q: Can I retain data longer if I encrypt it?**
A: No. Encryption doesn't change retention requirements.

**Q: What if there's litigation?**
A: Implement legal hold immediately. Pause deletion schedules.

**Q: How do I prove deletion happened?**
A: Maintain immutable audit logs with certificates of destruction.

**Q: What's the cost of non-compliance?**
A: PDPL: up to 5M SAR | NCA: up to 50M SAR | SAMA: up to 10M SAR

**Q: How often should I audit?**
A: Monthly (quick), Quarterly (deep), Annually (external)

---

## 🎯 Next Steps

1. **This Week:**
   - [ ] Read COMPLIANCE_FRAMEWORKS.md
   - [ ] Review IMPLEMENTATION_GUIDE.md
   - [ ] Generate policy template

2. **This Month:**
   - [ ] Create data inventory
   - [ ] Classify all data
   - [ ] Define retention periods

3. **This Quarter:**
   - [ ] Deploy encryption
   - [ ] Automate retention schedules
   - [ ] Train all staff

4. **This Year:**
   - [ ] Pass external audit
   - [ ] Establish continuous monitoring
   - [ ] Achieve Level 3 maturity

---

## 📞 Support

- **Questions?** Open an issue on GitHub
- **Updates?** Star this repository
- **Feedback?** Pull requests welcome
- **LinkedIn?** Share your compliance journey

---

**Last Updated:** 2026-09-12
**Version:** 1.0
**Status:** Production Ready ✅

