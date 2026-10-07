credit_applications = [
    {
        'application_id': 'CR001',
        'customer_name': 'Budi Santoso',
        'income': 8000000,
        'loan_amount': 50000000,
        'tenor': 24,
        'status': 'Pending'
    },
    {
        'application_id': 'CR002',
        'customer_name': 'Siti Aminah',
        'income': 12000000,
        'loan_amount': 75000000,
        'tenor': 36,
        'status': 'Pending'
    },
    {
        'application_id': 'CR003',
        'customer_name': 'Andi Wijaya',
        'income': 6000000,
        'loan_amount': 60000000,
        'tenor': 24,
        'status': 'Pending'
    }
]


def calculate_installment(loan_amount, tenor):
    installment = loan_amount / tenor
    return installment


def check_eligibility(installment, income):
    affordability_ratio = installment / income * 100

    if affordability_ratio <= 30:
        eligibility = 'Eligible'
    else:
        eligibility = 'Not Eligible'

    return affordability_ratio, eligibility


## CREATE menu
def create_application():
    pilihanCreate = input('''
==========================================
       CREATE CREDIT APPLICATION
==========================================
1. Add Credit Application
2. Back to Main Menu
==========================================
Choose menu : ''')

    if pilihanCreate == '1':

        print('''
------------------------------------------
       INPUT CREDIT APPLICATION
------------------------------------------''')

        application_id = input('Application ID : ')

        duplicate = False

        for data in credit_applications:
            if data['application_id'] == application_id:
                duplicate = True
                break

        if duplicate:
            print('''
------------------------------------------
Application ID already exists.
Please use another Application ID.
------------------------------------------''')

        else:
            customer_name = input('Customer Name : ')
            income = int(input('Monthly Income : '))
            loan_amount = int(input('Loan Amount : '))

            print('''
Tenor Options :
1. 12 Months
2. 24 Months
3. 36 Months
4. 48 Months
5. 60 Months
''')

            tenor = int(input('Tenor : '))

            if customer_name == '':
                print('Customer name cannot be empty.')

            elif income <= 0:
                print('Monthly income must be greater than 0.')

            elif loan_amount <= 0:
                print('Loan amount must be greater than 0.')

            elif tenor not in [12, 24, 36, 48, 60]:
                print('Invalid tenor. Please choose 12, 24, 36, 48, or 60 months.')

            else:
                installment = calculate_installment(loan_amount, tenor)

                affordability_ratio, eligibility = check_eligibility(
                    installment,
                    income
                )

                print('''
------------------------------------------
       CREDIT APPLICATION SUMMARY
------------------------------------------''')

                print(f'Application ID        : {application_id}')
                print(f'Customer Name         : {customer_name}')
                print(f'Monthly Income        : Rp{income:,.0f}')
                print(f'Loan Amount           : Rp{loan_amount:,.0f}')
                print(f'Tenor                 : {tenor} months')
                print(f'Estimated Installment : Rp{installment:,.0f}')
                print(f'Affordability Ratio   : {affordability_ratio:.2f}%')
                print(f'Eligibility           : {eligibility}')
                print(f'Status                : Pending')

                save = input('''
------------------------------------------
Save this application?

1. Yes
2. No
------------------------------------------
Choose menu : ''')

                if save == '1':

                    new_application = {
                        'application_id': application_id,
                        'customer_name': customer_name,
                        'income': income,
                        'loan_amount': loan_amount,
                        'tenor': tenor,
                        'status': 'Pending'
                    }

                    credit_applications.append(new_application)

                    print('''
------------------------------------------
Data successfully saved.
------------------------------------------''')

                elif save == '2':
                    print('''
------------------------------------------
Data not saved.
------------------------------------------''')

                else:
                    print('''
------------------------------------------
Invalid option. Data not saved.
------------------------------------------''')

    elif pilihanCreate == '2':
        pass

    else:
        print('Invalid menu. Please choose between 1 - 2.')


## READ menu
def read_application():
    pilihanRead = input('''
==========================================
        READ CREDIT APPLICATION
==========================================
1. Display All Applications
2. Search Application
3. Back to Main Menu
==========================================
Choose menu : ''')

    if pilihanRead == '1':

        if len(credit_applications) == 0:
            print('''
------------------------------------------
There is no credit application data.
------------------------------------------''')

        else:
            print('''
==========================================
       ALL CREDIT APPLICATIONS
==========================================''')

            for data in credit_applications:
                print(f'''
Application ID        : {data['application_id']}
Customer Name         : {data['customer_name']}
Monthly Income        : Rp{data['income']:,.0f}
Loan Amount           : Rp{data['loan_amount']:,.0f}
Tenor                 : {data['tenor']} months
Status                : {data['status']}
------------------------------------------''')

    elif pilihanRead == '2':

        application_id = input('Application ID : ')

        dataFound = False

        for data in credit_applications:
            if data['application_id'] == application_id:
                dataFound = True

                print('''
------------------------------------------
       CREDIT APPLICATION FOUND
------------------------------------------''')

                print(f'Application ID        : {data["application_id"]}')
                print(f'Customer Name         : {data["customer_name"]}')
                print(f'Monthly Income        : Rp{data["income"]:,.0f}')
                print(f'Loan Amount           : Rp{data["loan_amount"]:,.0f}')
                print(f'Tenor                 : {data["tenor"]} months')
                print(f'Status                : {data["status"]}')

                break

        if dataFound == False:
            print('''
------------------------------------------
The application data does not exist.
------------------------------------------''')

    elif pilihanRead == '3':
        pass

    else:
        print('Invalid menu. Please choose between 1 - 3.')


## UPDATE menu
def update_application():
    application_id = input('''
==========================================
       UPDATE CREDIT APPLICATION
==========================================
Application ID : ''')

    dataFound = False

    for data in credit_applications:
        if data['application_id'] == application_id:
            dataFound = True

            print('''
------------------------------------------
       CREDIT APPLICATION FOUND
------------------------------------------''')

            print(f'Application ID        : {data["application_id"]}')
            print(f'Customer Name         : {data["customer_name"]}')
            print(f'Monthly Income        : Rp{data["income"]:,.0f}')
            print(f'Loan Amount           : Rp{data["loan_amount"]:,.0f}')
            print(f'Tenor                 : {data["tenor"]} months')
            print(f'Status                : {data["status"]}')

            pilihanUpdate = input('''
------------------------------------------
Which field do you want to update?

1. Customer Name
2. Monthly Income
3. Loan Amount
4. Tenor
5. Status
6. Cancel
------------------------------------------
Choose menu : ''')

            if pilihanUpdate == '1':

                new_customer_name = input('New Customer Name : ')

                if new_customer_name == '':
                    print('Customer name cannot be empty.')

                else:
                    print(f'''
Old Customer Name : {data["customer_name"]}
New Customer Name : {new_customer_name}
''')

                    confirmation = input('''
Update this data?

1. Yes
2. No
Choose menu : ''')

                    if confirmation == '1':
                        data['customer_name'] = new_customer_name

                        print('''
------------------------------------------
Customer name successfully updated.
------------------------------------------''')

                    elif confirmation == '2':
                        print('Data not updated.')

                    else:
                        print('Invalid option. Data not updated.')

            elif pilihanUpdate == '2':

                new_income = int(input('New Monthly Income : '))

                if new_income <= 0:
                    print('Monthly income must be greater than 0.')

                else:
                    print(f'''
Old Monthly Income : Rp{data["income"]:,.0f}
New Monthly Income : Rp{new_income:,.0f}
''')

                    confirmation = input('''
Update this data?

1. Yes
2. No
Choose menu : ''')

                    if confirmation == '1':
                        data['income'] = new_income

                        installment = calculate_installment(
                            data['loan_amount'],
                            data['tenor']
                        )

                        affordability_ratio, eligibility = check_eligibility(
                            installment,
                            data['income']
                        )

                        print('''
------------------------------------------
Monthly income successfully updated.
Eligibility has been recalculated.
------------------------------------------''')

                        print(f'Estimated Installment : Rp{installment:,.0f}')
                        print(f'Affordability Ratio   : {affordability_ratio:.2f}%')
                        print(f'Eligibility           : {eligibility}')

                    elif confirmation == '2':
                        print('Data not updated.')

                    else:
                        print('Invalid option. Data not updated.')

            elif pilihanUpdate == '3':

                new_loan_amount = int(input('New Loan Amount : '))

                if new_loan_amount <= 0:
                    print('Loan amount must be greater than 0.')

                else:
                    print(f'''
Old Loan Amount : Rp{data["loan_amount"]:,.0f}
New Loan Amount : Rp{new_loan_amount:,.0f}
''')

                    confirmation = input('''
Update this data?

1. Yes
2. No
Choose menu : ''')

                    if confirmation == '1':
                        data['loan_amount'] = new_loan_amount

                        installment = calculate_installment(
                            data['loan_amount'],
                            data['tenor']
                        )

                        affordability_ratio, eligibility = check_eligibility(
                            installment,
                            data['income']
                        )

                        print('''
------------------------------------------
Loan amount successfully updated.
Eligibility has been recalculated.
------------------------------------------''')

                        print(f'Estimated Installment : Rp{installment:,.0f}')
                        print(f'Affordability Ratio   : {affordability_ratio:.2f}%')
                        print(f'Eligibility           : {eligibility}')

                    elif confirmation == '2':
                        print('Data not updated.')

                    else:
                        print('Invalid option. Data not updated.')

            elif pilihanUpdate == '4':

                print('''
Tenor Options :
1. 12 Months
2. 24 Months
3. 36 Months
4. 48 Months
5. 60 Months
''')

                new_tenor = int(input('New Tenor : '))

                if new_tenor not in [12, 24, 36, 48, 60]:
                    print('Invalid tenor. Please choose 12, 24, 36, 48, or 60 months.')

                else:
                    print(f'''
Old Tenor : {data["tenor"]} months
New Tenor : {new_tenor} months
''')

                    confirmation = input('''
Update this data?

1. Yes
2. No
Choose menu : ''')

                    if confirmation == '1':
                        data['tenor'] = new_tenor

                        installment = calculate_installment(
                            data['loan_amount'],
                            data['tenor']
                        )

                        affordability_ratio, eligibility = check_eligibility(
                            installment,
                            data['income']
                        )

                        print('''
------------------------------------------
Tenor successfully updated.
Eligibility has been recalculated.
------------------------------------------''')

                        print(f'Estimated Installment : Rp{installment:,.0f}')
                        print(f'Affordability Ratio   : {affordability_ratio:.2f}%')
                        print(f'Eligibility           : {eligibility}')

                    elif confirmation == '2':
                        print('Data not updated.')

                    else:
                        print('Invalid option. Data not updated.')

            elif pilihanUpdate == '5':

                print('''
Status Options :
1. Pending
2. Approved
3. Rejected
''')

                status_choice = input('Choose status : ')

                if status_choice == '1':
                    new_status = 'Pending'

                elif status_choice == '2':
                    new_status = 'Approved'

                elif status_choice == '3':
                    new_status = 'Rejected'

                else:
                    print('Invalid status option.')
                    new_status = ''

                if new_status != '':
                    print(f'''
Old Status : {data["status"]}
New Status : {new_status}
''')

                    confirmation = input('''
Update this data?

1. Yes
2. No
Choose menu : ''')

                    if confirmation == '1':
                        data['status'] = new_status

                        print('''
------------------------------------------
Status successfully updated.
------------------------------------------''')

                    elif confirmation == '2':
                        print('Data not updated.')

                    else:
                        print('Invalid option. Data not updated.')

            elif pilihanUpdate == '6':
                print('Update cancelled.')

            else:
                print('Invalid menu. Please choose between 1 - 6.')

            break

    if dataFound == False:
        print('''
------------------------------------------
The application data does not exist.
------------------------------------------''')


## DELETE menu
def delete_application():
    application_id = input('''
==========================================
       DELETE CREDIT APPLICATION
==========================================
Application ID : ''')

    dataFound = False

    for data in credit_applications:
        if data['application_id'] == application_id:
            dataFound = True

            print('''
------------------------------------------
       CREDIT APPLICATION FOUND
------------------------------------------''')

            print(f'Application ID        : {data["application_id"]}')
            print(f'Customer Name         : {data["customer_name"]}')
            print(f'Monthly Income        : Rp{data["income"]:,.0f}')
            print(f'Loan Amount           : Rp{data["loan_amount"]:,.0f}')
            print(f'Tenor                 : {data["tenor"]} months')
            print(f'Status                : {data["status"]}')

            confirmation = input('''
------------------------------------------
Are you sure you want to delete this data?

1. Yes
2. No
Choose menu : ''')

            if confirmation == '1':
                credit_applications.remove(data)

                print('''
------------------------------------------
Credit application successfully deleted.
------------------------------------------''')

            elif confirmation == '2':
                print('Data not deleted.')

            else:
                print('Invalid option. Data not deleted.')

            break

    if dataFound == False:
        print('''
------------------------------------------
The application data does not exist.
------------------------------------------''')


# menu utama
while True:
    pilihanMenu = input('''
==========================================
   CREDIT APPLICATION MANAGEMENT SYSTEM
==========================================
1. Create Credit Application
2. Read Credit Application
3. Update Credit Application
4. Delete Credit Application
5. Exit
==========================================
Choose menu : ''')

    if pilihanMenu == '1':
        create_application()

    elif pilihanMenu == '2':
        read_application()

    elif pilihanMenu == '3':
        update_application()

    elif pilihanMenu == '4':
        delete_application()

    elif pilihanMenu == '5':
        print('''
==========================================
Thank you for using Credit Application
Management System.
==========================================
''')
        break

    else:
        print('Invalid menu. Please choose between 1 - 5.')

