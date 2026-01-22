"""
Report generator module to create personnel management reports.
"""
import json
from datetime import datetime
from typing import List
from personnel_models import PersonnelReport, EmployeePerformance, StaffingRequirement


class ReportGenerator:
    """Generates personnel management reports in various formats."""
    
    @staticmethod
    def generate_text_report(report: PersonnelReport) -> str:
        """
        Generate a text-based personnel report.
        
        Args:
            report: PersonnelReport object
            
        Returns:
            Formatted text report
        """
        lines = []
        lines.append("=" * 80)
        lines.append("CARREFOUR - PERSONNEL MANAGEMENT REPORT")
        lines.append("=" * 80)
        lines.append(f"Report Date: {report.report_date.strftime('%Y-%m-%d %H:%M')}")
        lines.append(f"Analysis Period: {report.summary.get('period_days', 0)} days")
        lines.append("")
        
        # Summary section
        lines.append("-" * 80)
        lines.append("EXECUTIVE SUMMARY")
        lines.append("-" * 80)
        lines.append(f"Total Employees Analyzed: {report.summary.get('total_employees', 0)}")
        lines.append(f"Total Revenue Generated: €{report.summary.get('total_revenue', 0):,.2f}")
        lines.append(f"Average Efficiency Score: {report.summary.get('avg_efficiency_score', 0):.2f}/100")
        lines.append(f"Top Performer: {report.summary.get('top_performer', 'N/A')}")
        lines.append("")
        
        # Employee Performance section
        lines.append("-" * 80)
        lines.append("EMPLOYEE PERFORMANCE METRICS")
        lines.append("-" * 80)
        lines.append(f"{'Employee':<20} {'Dept':<15} {'Trans':<8} {'Revenue':<12} {'Eff.Score':<10}")
        lines.append("-" * 80)
        
        for performance in report.employee_performances:
            lines.append(
                f"{performance.employee_name:<20} "
                f"{performance.department:<15} "
                f"{performance.total_transactions:<8} "
                f"€{performance.total_revenue:<11,.2f} "
                f"{performance.efficiency_score:<10.2f}"
            )
        
        lines.append("")
        
        # Staffing Requirements section
        lines.append("-" * 80)
        lines.append("STAFFING REQUIREMENTS (Sample Hours)")
        lines.append("-" * 80)
        lines.append(f"{'Department':<15} {'Hour':<8} {'Staff Req':<12} {'Exp. Trans':<12} {'Exp. Revenue'}")
        lines.append("-" * 80)
        
        # Show a sample of peak hours (10-18)
        sample_requirements = [
            req for req in report.staffing_requirements 
            if 10 <= req.hour <= 18
        ][:15]  # Show first 15 entries
        
        for req in sample_requirements:
            lines.append(
                f"{req.department:<15} "
                f"{req.hour:02d}:00{'':<3} "
                f"{req.required_staff:<12} "
                f"{req.expected_transactions:<12} "
                f"€{req.expected_revenue:,.2f}"
            )
        
        lines.append("")
        lines.append("=" * 80)
        lines.append("END OF REPORT")
        lines.append("=" * 80)
        
        return "\n".join(lines)
    
    @staticmethod
    def generate_json_report(report: PersonnelReport) -> str:
        """
        Generate a JSON-based personnel report.
        
        Args:
            report: PersonnelReport object
            
        Returns:
            JSON formatted report
        """
        report_dict = report.to_dict()
        # Convert datetime objects to ISO format strings
        report_dict['report_date'] = report_dict['report_date'].isoformat()
        
        for perf in report_dict['employee_performances']:
            perf['period_start'] = perf['period_start'].isoformat()
            perf['period_end'] = perf['period_end'].isoformat()
        
        for req in report_dict['staffing_requirements']:
            req['date'] = req['date'].isoformat()
        
        return json.dumps(report_dict, indent=2, ensure_ascii=False)
    
    @staticmethod
    def save_report(report: PersonnelReport, filepath: str, format: str = 'text'):
        """
        Save personnel report to a file.
        
        Args:
            report: PersonnelReport object
            filepath: Path to save the report
            format: 'text' or 'json'
        """
        if format == 'json':
            content = ReportGenerator.generate_json_report(report)
        else:
            content = ReportGenerator.generate_text_report(report)
        
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)
