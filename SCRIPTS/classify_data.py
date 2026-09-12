#!/usr/bin/env python3
"""
Data Classification Automation Script
KSA PDPL, NCA-ECC, and SAMA CSF Compliant

This script automates the classification of data based on content analysis,
data location, and organizational policies.

Usage:
    python classify_data.py --input data_inventory.csv --output classified_data.csv
    python classify_data.py --input data_inventory.csv --framework pdpl
"""

import csv
import argparse
import logging
from datetime import datetime
from typing import Dict, List, Tuple
import re
import json

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('classification_audit.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class DataClassifier:
    """Classify data according to KSA compliance frameworks"""
    
    # Classification levels
    CLASSIFICATION_LEVELS = {
        'PUBLIC': {'level': 1, 'encryption': False, 'access_control': 'Everyone'},
        'INTERNAL': {'level': 2, 'encryption': 'Recommended', 'access_control': 'Employees'},
        'CONFIDENTIAL': {'level': 3, 'encryption': True, 'access_control': 'Select staff'},
        'RESTRICTED': {'level': 4, 'encryption': 'AES-256 Required', 'access_control': '1-2 people'}
    }
    
    # Retention periods by framework (in years)
    RETENTION_PERIODS = {
        'PDPL': {
            'PUBLIC': 1,
            'INTERNAL': 3,
            'CONFIDENTIAL': 5,
            'RESTRICTED': 7
        },
        'NCA-ECC': {
            'PUBLIC': 1,
            'INTERNAL': 1,
            'CONFIDENTIAL': 1,
            'RESTRICTED': 2
        },
        'SAMA-CSF': {
            'PUBLIC': 1,
            'INTERNAL': 3,
            'CONFIDENTIAL': 7,
            'RESTRICTED': 10
        }
    }
    
    # Patterns for PII detection
    PII_PATTERNS = {
        'passport': r'\b([A-Z]{1,2}\d{7})\b',  # Saudi ID format
        'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
        'phone': r'\b(?:\+966|0)[1-9]\d{8}\b',  # Saudi phone
        'credit_card': r'\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b',
        'ssn': r'\b\d{3}-\d{2}-\d{4}\b',
        'iban': r'\bSA\d{22}\b'  # Saudi IBAN
    }
    
    # Keywords indicating sensitive data
    SENSITIVE_KEYWORDS = {
        'financial': ['account', 'transaction', 'payment', 'invoice', 'salary'],
        'health': ['medical', 'diagnosis', 'prescription', 'patient', 'treatment'],
        'personal': ['ssn', 'passport', 'phone', 'email', 'address'],
        'confidential': ['secret', 'confidential', 'classified', 'private', 'restricted']
    }
    
    def __init__(self):
        self.classifications = []
        self.pii_detections = []
    
    def classify_data(self, data_type: str, data_location: str, 
                     data_sample: str = None) -> Tuple[str, Dict]:
        """
        Classify data based on type, location, and content analysis
        
        Returns: (classification_level, metadata)
        """
        classification = 'INTERNAL'  # Default
        confidence = 0.0
        detected_pii = []
        detected_keywords = []
        
        # Check for PII patterns
        if data_sample:
            for pii_type, pattern in self.PII_PATTERNS.items():
                if re.search(pattern, data_sample):
                    detected_pii.append(pii_type)
                    classification = 'RESTRICTED'
                    confidence = max(confidence, 0.95)
            
            # Check for sensitive keywords
            sample_lower = data_sample.lower()
            for category, keywords in self.SENSITIVE_KEYWORDS.items():
                for keyword in keywords:
                    if keyword in sample_lower:
                        detected_keywords.append(keyword)
                        if category == 'confidential':
                            classification = 'RESTRICTED'
                        elif category in ['financial', 'health']:
                            classification = 'CONFIDENTIAL'
        
        # Check data type
        if 'customer' in data_type.lower() and 'identity' in data_type.lower():
            classification = 'CONFIDENTIAL'  # KYC data
            confidence = max(confidence, 0.9)
        
        if 'transaction' in data_type.lower() or 'financial' in data_type.lower():
            classification = 'CONFIDENTIAL'  # Financial data
            confidence = max(confidence, 0.85)
        
        if 'log' in data_type.lower() or 'audit' in data_type.lower():
            if 'security' in data_type.lower():
                classification = 'CONFIDENTIAL'
            else:
                classification = 'INTERNAL'
        
        if 'marketing' in data_type.lower() or 'public' in data_type.lower():
            classification = 'PUBLIC'
            confidence = max(confidence, 0.9)
        
        # Check data location
        if 'encrypted' in data_location.lower() or 'vault' in data_location.lower():
            confidence += 0.1
        
        if 'public_bucket' in data_location.lower() or 'shared_drive' in data_location.lower():
            classification = 'PUBLIC'
        
        metadata = {
            'classification': classification,
            'confidence': confidence,
            'detected_pii': detected_pii,
            'detected_keywords': detected_keywords,
            'encryption_required': self.CLASSIFICATION_LEVELS[classification]['encryption'],
            'access_control': self.CLASSIFICATION_LEVELS[classification]['access_control'],
            'classified_at': datetime.now().isoformat(),
            'reviewed_by': 'automated_classifier'
        }
        
        return classification, metadata
    
    def apply_framework_retention(self, classification: str, 
                                  framework: str = 'PDPL') -> Dict:
        """Get retention period based on framework"""
        retention_years = self.RETENTION_PERIODS.get(framework, {}).get(
            classification, 1
        )
        
        return {
            'framework': framework,
            'classification': classification,
            'retention_years': retention_years,
            'deletion_date': self._calculate_deletion_date(retention_years)
        }
    
    @staticmethod
    def _calculate_deletion_date(years: int) -> str:
        """Calculate deletion date"""
        from datetime import timedelta
        deletion_date = datetime.now() + timedelta(days=365*years)
        return deletion_date.strftime('%Y-%m-%d')
    
    def classify_csv(self, input_file: str, output_file: str, 
                    framework: str = 'PDPL') -> None:
        """Classify all data in CSV file"""
        
        logger.info(f"Starting data classification from {input_file}")
        classified_count = 0
        
        try:
            with open(input_file, 'r', encoding='utf-8') as infile, \
                 open(output_file, 'w', encoding='utf-8', newline='') as outfile:
                
                reader = csv.DictReader(infile)
                
                # Add new columns to output
                fieldnames = reader.fieldnames + [
                    'classification', 'retention_years', 'deletion_date', 
                    'encryption_required', 'access_control', 'confidence', 
                    'detected_pii', 'review_required'
                ]
                
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()
                
                for row in reader:
                    data_type = row.get('data_type', '')
                    location = row.get('location', '')
                    sample = row.get('data_sample', '')
                    
                    # Classify
                    classification, metadata = self.classify_data(
                        data_type, location, sample
                    )
                    
                    # Get retention
                    retention_info = self.apply_framework_retention(
                        classification, framework
                    )
                    
                    # Determine if review needed
                    review_required = (
                        metadata['confidence'] < 0.8 or 
                        len(metadata['detected_pii']) > 0
                    )
                    
                    # Update row
                    row.update({
                        'classification': classification,
                        'retention_years': retention_info['retention_years'],
                        'deletion_date': retention_info['deletion_date'],
                        'encryption_required': metadata['encryption_required'],
                        'access_control': metadata['access_control'],
                        'confidence': f"{metadata['confidence']:.2%}",
                        'detected_pii': '|'.join(metadata['detected_pii']),
                        'review_required': 'YES' if review_required else 'NO'
                    })
                    
                    writer.writerow(row)
                    classified_count += 1
                    
                    # Log high-confidence classifications
                    if metadata['confidence'] >= 0.8:
                        logger.debug(
                            f"✅ Classified {data_type}: {classification} "
                            f"({metadata['confidence']:.0%} confidence)"
                        )
                    else:
                        logger.warning(
                            f"⚠️  Low confidence classification for {data_type}: "
                            f"{classification} ({metadata['confidence']:.0%}). "
                            f"Manual review recommended."
                        )
            
            logger.info(
                f"✅ Successfully classified {classified_count} data items. "
                f"Output: {output_file}"
            )
        
        except Exception as e:
            logger.error(f"❌ Error during classification: {str(e)}")
            raise
    
    def generate_classification_report(self, output_file: str) -> None:
        """Generate summary report"""
        from collections import Counter
        
        classifications = [item.get('classification') for item in self.classifications]
        summary = Counter(classifications)
        
        report = {
            'total_items_classified': len(self.classifications),
            'classification_summary': dict(summary),
            'items_with_pii': len(self.pii_detections),
            'generated_at': datetime.now().isoformat()
        }
        
        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        logger.info(f"Classification report saved to {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description='Classify data according to KSA compliance frameworks'
    )
    parser.add_argument('--input', required=True, help='Input CSV file')
    parser.add_argument('--output', required=True, help='Output CSV file')
    parser.add_argument(
        '--framework', 
        choices=['PDPL', 'NCA-ECC', 'SAMA-CSF'],
        default='PDPL',
        help='Compliance framework (default: PDPL)'
    )
    
    args = parser.parse_args()
    
    classifier = DataClassifier()
    classifier.classify_csv(args.input, args.output, args.framework)


if __name__ == '__main__':
    main()
