"""
Transformer module to convert purchase data into personnel management insights.
"""
from datetime import datetime, timedelta
from typing import List, Dict
from collections import defaultdict

from purchase_models import PurchaseTransaction
from personnel_models import EmployeePerformance, StaffingRequirement, PersonnelReport


class PurchaseToPersonnelTransformer:
    """Transforms purchase transaction data into personnel management data."""
    
    def __init__(self):
        self.employee_database = {}  # Maps employee_id to employee_name
        
    def register_employee(self, employee_id: str, employee_name: str):
        """Register an employee in the system."""
        self.employee_database[employee_id] = employee_name
    
    def calculate_employee_performance(
        self, 
        transactions: List[PurchaseTransaction],
        period_start: datetime,
        period_end: datetime
    ) -> List[EmployeePerformance]:
        """
        Calculate employee performance metrics from purchase transactions.
        
        Args:
            transactions: List of purchase transactions
            period_start: Start of the analysis period
            period_end: End of the analysis period
            
        Returns:
            List of EmployeePerformance objects
        """
        # Group transactions by employee
        employee_transactions = defaultdict(list)
        for transaction in transactions:
            if period_start <= transaction.timestamp <= period_end:
                employee_transactions[transaction.cashier_id].append(transaction)
        
        performances = []
        for employee_id, emp_transactions in employee_transactions.items():
            if not emp_transactions:
                continue
                
            # Calculate metrics
            total_transactions = len(emp_transactions)
            total_revenue = sum(t.amount for t in emp_transactions)
            avg_transaction_value = total_revenue / total_transactions if total_transactions > 0 else 0
            
            # Calculate working hours (simplified - assumes continuous work)
            timestamps = sorted([t.timestamp for t in emp_transactions])
            if len(timestamps) > 1:
                working_hours = (timestamps[-1] - timestamps[0]).total_seconds() / 3600
                working_hours = max(working_hours, 1)  # At least 1 hour
            else:
                working_hours = 1
                
            transactions_per_hour = total_transactions / working_hours
            
            # Calculate efficiency score (0-100)
            # Based on transactions per hour and average transaction value
            base_efficiency = min(transactions_per_hour * 5, 50)  # Up to 50 points
            value_bonus = min(avg_transaction_value / 10, 50)  # Up to 50 points
            efficiency_score = min(base_efficiency + value_bonus, 100)
            
            # Get department (most common)
            departments = [t.department for t in emp_transactions]
            department = max(set(departments), key=departments.count)
            
            employee_name = self.employee_database.get(employee_id, f"Employee {employee_id}")
            
            performance = EmployeePerformance(
                employee_id=employee_id,
                employee_name=employee_name,
                department=department,
                period_start=period_start,
                period_end=period_end,
                total_transactions=total_transactions,
                total_revenue=round(total_revenue, 2),
                avg_transaction_value=round(avg_transaction_value, 2),
                transactions_per_hour=round(transactions_per_hour, 2),
                efficiency_score=round(efficiency_score, 2)
            )
            performances.append(performance)
        
        return sorted(performances, key=lambda x: x.efficiency_score, reverse=True)
    
    def calculate_staffing_requirements(
        self,
        transactions: List[PurchaseTransaction],
        analysis_date: datetime
    ) -> List[StaffingRequirement]:
        """
        Calculate staffing requirements based on transaction patterns.
        
        Args:
            transactions: Historical purchase transactions
            analysis_date: Date for which to calculate requirements
            
        Returns:
            List of StaffingRequirement objects
        """
        # Analyze historical patterns by department and hour
        dept_hour_stats = defaultdict(lambda: {'transactions': [], 'revenue': []})
        
        for transaction in transactions:
            hour = transaction.timestamp.hour
            key = (transaction.department, hour)
            dept_hour_stats[key]['transactions'].append(1)
            dept_hour_stats[key]['revenue'].append(transaction.amount)
        
        requirements = []
        
        # Generate requirements for each department and hour
        departments = set(t.department for t in transactions)
        for department in departments:
            for hour in range(8, 22):  # Store hours 8 AM to 10 PM
                key = (department, hour)
                stats = dept_hour_stats.get(key, {'transactions': [], 'revenue': []})
                
                if stats['transactions']:
                    expected_transactions = int(sum(stats['transactions']) / len(stats['transactions']))
                    expected_revenue = sum(stats['revenue']) / len(stats['revenue'])
                else:
                    expected_transactions = 10  # Default minimum
                    expected_revenue = 100.0
                
                # Calculate required staff based on expected transactions
                # Assume 1 staff per 20 transactions per hour
                required_staff = max(1, (expected_transactions + 19) // 20)
                
                requirement = StaffingRequirement(
                    department=department,
                    date=analysis_date,
                    hour=hour,
                    required_staff=required_staff,
                    expected_transactions=expected_transactions,
                    expected_revenue=round(expected_revenue, 2)
                )
                requirements.append(requirement)
        
        return sorted(requirements, key=lambda x: (x.department, x.hour))
    
    def generate_personnel_report(
        self,
        transactions: List[PurchaseTransaction],
        report_date: datetime,
        period_days: int = 7
    ) -> PersonnelReport:
        """
        Generate a complete personnel management report.
        
        Args:
            transactions: Purchase transactions
            report_date: Date of the report
            period_days: Number of days to analyze
            
        Returns:
            PersonnelReport object
        """
        period_end = report_date
        period_start = report_date - timedelta(days=period_days)
        
        # Calculate employee performances
        employee_performances = self.calculate_employee_performance(
            transactions, period_start, period_end
        )
        
        # Calculate staffing requirements
        staffing_requirements = self.calculate_staffing_requirements(
            transactions, report_date
        )
        
        # Generate summary
        if employee_performances:
            summary = {
                'total_employees': len(employee_performances),
                'total_revenue': sum(ep.total_revenue for ep in employee_performances),
                'avg_efficiency_score': round(
                    sum(ep.efficiency_score for ep in employee_performances) / len(employee_performances),
                    2
                ),
                'top_performer': employee_performances[0].employee_name if employee_performances else None,
                'period_days': period_days
            }
        else:
            summary = {
                'total_employees': 0,
                'total_revenue': 0,
                'avg_efficiency_score': 0,
                'top_performer': None,
                'period_days': period_days
            }
        
        return PersonnelReport(
            report_date=report_date,
            employee_performances=employee_performances,
            staffing_requirements=staffing_requirements,
            summary=summary
        )
