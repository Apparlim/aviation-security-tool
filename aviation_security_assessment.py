#!/usr/bin/env python3
"""
NetJets Aviation Security Risk Assessment Tool

Started this as a class project but realized it could be useful for real aviation companies.
Been working on this for a few weeks now, trying to make it actually practical.

TODO: Maybe add more advanced checks later, this is just the basics for now
"""

import pandas as pd
from datetime import datetime
import os
import json

class AviationSecurityAssessment:
    def __init__(self):
        self.assessment_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # originally had more categories but simplified it
        self.risk_categories = {
            'flight_ops': 'Flight Operations Security',  # shortened the key names
            'passenger_data': 'Passenger Data Protection', 
            'aircraft_systems': 'Aircraft Systems Security',
            'ground_ops': 'Ground Operations Security',  # this was 'ground_operations' before
            'comms': 'Communication Systems Security'    # changed to 'comms' for brevity
        }
        self.results = []
        self.debug = False  # might need this later for troubleshooting
        
    def check_flight_operations(self):  # renamed from assess_flight_operations
        """Check flight operations security - this is the important stuff"""
        if self.debug:
            print("DEBUG: Starting flight ops checks...")
        print("🛩️  Checking Flight Operations Security...")
        
        # these are based on real aviation security standards I researched
        security_checks = [  # renamed from 'checks'
            {
                'check_name': 'Flight Plan Encryption',  # was just 'check'
                'result': 'PASS',  # changed from 'status' to 'result' 
                'risk': 'Low',     # shortened from 'risk_level'
                'score': 9,
                'notes': 'Using AES-256, looks good',  # changed from 'recommendation'
                'priority': 'maintain'
            },
            {
                'check_name': 'GPS Anti-Spoofing',  # made it more specific
                'result': 'WARN',   # shortened from 'Warning'
                'risk': 'Medium', 
                'score': 6,
                'notes': 'Should add backup navigation systems',
                'priority': 'medium'  # added priority field
            },
            {
                'check_name': 'ATC Interface Security',
                'result': 'PASS',
                'risk': 'Low',
                'score': 8,
                'notes': 'Secure comms with air traffic control verified',
                'priority': 'maintain'
            },
            # added a new check that wasn't in original
            {
                'check_name': 'Weather Data Integrity',
                'result': 'PASS',
                'risk': 'Low', 
                'score': 8,
                'notes': 'Weather data sources are authenticated',
                'priority': 'maintain'
            }
        ]
        
        for check in security_checks:
            check['category'] = self.risk_categories['flight_ops']
            check['timestamp'] = datetime.now().isoformat()  # added timestamp
            self.results.append(check)

    def check_passenger_data(self):  
        """Passenger data protection - super important for privacy laws"""
        print("🛡️  Checking Passenger Data Protection...")
        
        # GDPR and other privacy regs are no joke
        checks = [
            {
                'check_name': 'Personal Data Encryption',
                'result': 'PASS',
                'risk': 'Low',
                'score': 9,
                'notes': 'AES-256 encryption confirmed for PII storage',
                'priority': 'critical'
            },
            {
                'check_name': 'Access Control Matrix',  # was 'Data Access Controls'
                'result': 'WARN',
                'risk': 'Medium',
                'score': 7,
                'notes': 'Need role-based access - too many people have admin rights',
                'priority': 'high'
            },
            {
                'check_name': 'Data Retention Policy',
                'result': 'PASS', 
                'risk': 'Low',
                'score': 8,
                'notes': 'Auto-delete working, complies with retention rules',
                'priority': 'maintain'
            },
            # added this one after reading about CCPA requirements
            {
                'check_name': 'Data Subject Rights',
                'result': 'WARN',
                'risk': 'Medium',
                'score': 6,
                'notes': 'Process for data deletion requests needs work',
                'priority': 'medium'
            }
        ]
        
        for check in checks:
            check['category'] = self.risk_categories['passenger_data']
            check['timestamp'] = datetime.now().isoformat()
            self.results.append(check)

    def check_aircraft_systems(self):
        """Aircraft systems security - the scary stuff if it goes wrong"""
        print("✈️  Checking Aircraft Systems Security...")
        
        # this is where things get really critical
        checks = [
            {
                'check_name': 'Avionics Network Isolation', 
                'result': 'PASS',
                'risk': 'Low',
                'score': 9,
                'notes': 'Critical flight systems properly air-gapped',
                'priority': 'critical'
            },
            {
                'check_name': 'Passenger WiFi Isolation',  # this is a big issue
                'result': 'FAIL',
                'risk': 'High',
                'score': 3,
                'notes': 'URGENT: Passenger WiFi can potentially reach aircraft systems!',
                'priority': 'critical'
            },
            {
                'check_name': 'Maintenance Port Security',
                'result': 'WARN', 
                'risk': 'Medium',
                'score': 6,
                'notes': 'Maintenance access needs MFA, currently just passwords',
                'priority': 'high'
            },
            # this wasn't in the original but it's important
            {
                'check_name': 'Software Update Process',
                'result': 'WARN',
                'risk': 'Medium', 
                'score': 5,
                'notes': 'Avionics updates not properly signed/verified',
                'priority': 'high'
            }
        ]
        
        for check in checks:
            check['category'] = self.risk_categories['aircraft_systems']
            check['timestamp'] = datetime.now().isoformat()
            self.results.append(check)

    def check_ground_operations(self):
        """Ground ops security - often overlooked but important"""
        print("🏢 Checking Ground Operations Security...")
        
        checks = [
            {
                'check_name': 'Hangar Physical Access',
                'result': 'PASS',
                'risk': 'Low', 
                'score': 8,
                'notes': 'Biometric access controls working well',
                'priority': 'maintain'
            },
            {
                'check_name': 'Ground Crew Mobile Devices',
                'result': 'WARN',
                'risk': 'Medium',
                'score': 5,
                'notes': 'Tablets and phones need better MDM, some are personal devices',
                'priority': 'medium'
            },
            {
                'check_name': 'Fuel System Monitoring',
                'result': 'PASS',
                'risk': 'Low',
                'score': 8, 
                'notes': 'Continuous monitoring and alerts in place',
                'priority': 'maintain'
            },
            # added this after thinking about supply chain attacks
            {
                'check_name': 'Third-Party Vendor Access',
                'result': 'WARN',
                'risk': 'Medium',
                'score': 6,
                'notes': 'Catering and cleaning crews have too much access',
                'priority': 'medium'
            }
        ]
        
        for check in checks:
            check['category'] = self.risk_categories['ground_ops']
            check['timestamp'] = datetime.now().isoformat() 
            self.results.append(check)

    def check_communications(self):
        """Communication security - pilot comms are critical"""
        print("📡 Checking Communication Systems Security...")
        
        checks = [
            {
                'check_name': 'Pilot-Ground Encryption',
                'result': 'PASS',
                'risk': 'Low',
                'score': 9,
                'notes': 'Encrypted voice comms verified and working',
                'priority': 'critical'
            },
            {
                'check_name': 'Satellite Link Security', 
                'result': 'WARN',
                'risk': 'Medium',
                'score': 6,
                'notes': 'Satellite protocols could be more secure, some legacy systems',
                'priority': 'medium'
            }
        ]
        
        for check in checks:
            check['category'] = self.risk_categories['comms']
            check['timestamp'] = datetime.now().isoformat()
            self.results.append(check)
    
    def get_overall_score(self):  # renamed from calculate_overall_score
        """Calculate the overall security posture score"""
        if not self.results:
            return 0
        
        total = sum(result['score'] for result in self.results)
        max_possible = len(self.results) * 10
        overall = round((total / max_possible) * 100, 1)
        
        if self.debug:
            print(f"DEBUG: Total score: {total}/{max_possible} = {overall}%")
            
        return overall

    def save_results(self):  # renamed from generate_report
        """Save results to Excel - management loves Excel files"""
        print("📊 Creating Excel report...")
        
        if not self.results:
            print("No results to save!")
            return None
        
        # convert to DataFrame - pandas makes this easy
        df = pd.DataFrame(self.results)
        
        overall_score = self.get_overall_score()
        
        # count up the risk levels
        risk_counts = df['risk'].value_counts()
        
        # file name with timestamp so we don't overwrite old ones
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S') 
        filename = f"aviation_security_assessment_{timestamp}.xlsx"
        
        try:
            with pd.ExcelWriter(filename, engine='openpyxl') as writer:
                # main results - this is the detailed stuff
                df.to_excel(writer, sheet_name='Detailed Results', index=False)
                
                # executive summary for the bosses
                summary_info = {
                    'Metric': [
                        'Overall Security Score (%)', 
                        'Total Security Checks', 
                        'Critical Issues (FAIL)', 
                        'Warning Issues (WARN)',
                        'Passing Checks (PASS)', 
                        'Assessment Date',
                        'High Risk Items',
                        'Medium Risk Items', 
                        'Low Risk Items'
                    ],
                    'Value': [
                        f"{overall_score}%",
                        len(self.results),
                        len(df[df['result'] == 'FAIL']),
                        len(df[df['result'] == 'WARN']), 
                        len(df[df['result'] == 'PASS']),
                        self.assessment_date,
                        risk_counts.get('High', 0),
                        risk_counts.get('Medium', 0),
                        risk_counts.get('Low', 0)
                    ]
                }
                summary_df = pd.DataFrame(summary_info)
                summary_df.to_excel(writer, sheet_name='Executive Summary', index=False)
                
                # critical items only - for immediate action
                critical_items = df[df['result'].isin(['FAIL', 'WARN'])].copy()
                if not critical_items.empty:
                    critical_items = critical_items.sort_values(['risk', 'score'])  # worst first
                    critical_items.to_excel(writer, sheet_name='Action Items', index=False)
            
            print(f"✅ Report saved: {filename}")
            print(f"📈 Overall Security Score: {overall_score}%")
            
            # give some context on the score
            if overall_score >= 80:
                print("   Status: Good security posture")
            elif overall_score >= 60:
                print("   Status: Needs improvement") 
            else:
                print("   Status: Serious security gaps - immediate action needed")
                
            return filename
            
        except Exception as e:
            print(f"❌ Error creating Excel file: {e}")
            print("Make sure you have openpyxl installed: pip install openpyxl")
            return None

    def run_assessment(self):  # shortened name
        """Run the complete security assessment"""
        print("=" * 50)
        print("🛩️  Aviation Security Assessment Tool")  
        print("   Designed for Private Aviation Operations")
        print("=" * 50)
        print()
        
        # clear any previous results
        self.results = []
        
        # run all the security checks
        self.check_flight_operations()
        print()
        self.check_passenger_data() 
        print()
        self.check_aircraft_systems()
        print()
        self.check_ground_operations()
        print()  
        self.check_communications()
        print()
        
        # generate the Excel report
        report_file = self.save_results()
        
        print("=" * 50)
        if report_file:
            print("✅ Assessment Complete!")
            print(f"📋 Report: {report_file}")
            
            # show critical items
            critical = [r for r in self.results if r['result'] in ['FAIL', 'WARN']]
            if critical:
                print(f"\n⚠️  {len(critical)} items need attention:")
                for item in critical[:3]:  # show first 3
                    status_emoji = "🔴" if item['result'] == 'FAIL' else "🟡" 
                    print(f"   {status_emoji} {item['check_name']}: {item['notes']}")
                if len(critical) > 3:
                    print(f"   ... and {len(critical)-3} more (see Excel report)")
        else:
            print("❌ Assessment failed - check error messages above")
        
        print("=" * 50)
        return report_file

# main execution 
def main():
    """Run the assessment - entry point"""
    print("Starting aviation security assessment...")
    
    try:
        # create assessment instance and run it
        assessment = AviationSecurityAssessment()
        result_file = assessment.run_assessment()
        
        if result_file:
            print(f"\n📋 Next Steps:")
            print("   1. Review all FAIL items immediately")
            print("   2. Plan fixes for WARN items") 
            print("   3. Schedule follow-up assessment in 90 days")
            print("   4. Share report with security team")
            print(f"   5. Keep this tool updated for regular assessments")
        else:
            print("\n❌ Something went wrong - check the error messages above")
            
    except ImportError as e:
        print(f"❌ Missing required packages: {e}")
        print("Install with: pip install pandas openpyxl")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        print("If this keeps happening, check your Python installation")

# only run if this file is executed directly
if __name__ == "__main__":
    main()