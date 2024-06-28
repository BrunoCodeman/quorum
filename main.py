from lib.business_logic import generate_legislators_report_csv, generate_bills_report_csv


if __name__ == '__main__':
    legislators_report_filepath='./deliverables/legislators-support-oppose-count.csv'
    bills_report_filepath='./deliverables/bills.csv'
    generate_legislators_report_csv(legislators_report_filepath)
    generate_bills_report_csv(bills_report_filepath)