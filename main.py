#!/usr/bin/env python3
"""
Main application for Carrefour Purchase to Personnel Management System.

This system transforms purchase transaction data into personnel management insights,
including employee performance metrics and staffing requirements.
"""
import sys
import os
from datetime import datetime
from data_loader import PurchaseDataLoader
from transformer import PurchaseToPersonnelTransformer
from report_generator import ReportGenerator


def main():
    """Main function to run the purchase to personnel transformation system."""
    print("=" * 80)
    print("CARREFOUR - Purchase to Personnel Management System")
    print("Sistema di Trasformazione Dati Acquisti in Gestione Personale")
    print("=" * 80)
    print()
    
    # Check if sample data exists
    sample_data_path = os.path.join(os.path.dirname(__file__), 'sample_data', 'purchases.csv')
    
    if not os.path.exists(sample_data_path):
        print(f"Error: Sample data file not found at {sample_data_path}")
        print("Please ensure sample_data/purchases.csv exists.")
        sys.exit(1)
    
    # Load purchase data
    print(f"Loading purchase data from {sample_data_path}...")
    try:
        transactions = PurchaseDataLoader.load_from_csv(sample_data_path)
        print(f"✓ Loaded {len(transactions)} transactions")
    except Exception as e:
        print(f"Error loading data: {e}")
        sys.exit(1)
    
    print()
    
    # Initialize transformer
    print("Initializing transformation system...")
    transformer = PurchaseToPersonnelTransformer()
    
    # Register employees (in real system, this would come from HR database)
    employees = {
        'CASH001': 'Maria Rossi',
        'CASH002': 'Giovanni Bianchi',
        'CASH003': 'Laura Verdi',
        'CASH004': 'Marco Ferrari'
    }
    
    for emp_id, emp_name in employees.items():
        transformer.register_employee(emp_id, emp_name)
    
    print(f"✓ Registered {len(employees)} employees")
    print()
    
    # Generate personnel report
    print("Generating personnel management report...")
    report_date = datetime.now()
    report = transformer.generate_personnel_report(
        transactions=transactions,
        report_date=report_date,
        period_days=7
    )
    print("✓ Report generated successfully")
    print()
    
    # Display report to console
    text_report = ReportGenerator.generate_text_report(report)
    print(text_report)
    print()
    
    # Save reports to files
    output_dir = os.path.join(os.path.dirname(__file__), 'output')
    os.makedirs(output_dir, exist_ok=True)
    
    # Save text report
    text_report_path = os.path.join(output_dir, f'personnel_report_{report_date.strftime("%Y%m%d_%H%M%S")}.txt')
    ReportGenerator.save_report(report, text_report_path, format='text')
    print(f"✓ Text report saved to: {text_report_path}")
    
    # Save JSON report
    json_report_path = os.path.join(output_dir, f'personnel_report_{report_date.strftime("%Y%m%d_%H%M%S")}.json')
    ReportGenerator.save_report(report, json_report_path, format='json')
    print(f"✓ JSON report saved to: {json_report_path}")
    
    print()
    print("=" * 80)
    print("Transformation completed successfully!")
    print("Sistema completato con successo!")
    print("=" * 80)


if __name__ == '__main__':
    main()
