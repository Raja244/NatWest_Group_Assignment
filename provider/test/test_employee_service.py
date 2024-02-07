import unittest
from pact import Consumer, Like
from pact.consumer import Provider

class EmployeeServiceContractTest(unittest.TestCase):

    def test_employee_service_contract(self):
        # Define the consumer and provider
        with Consumer('Dashboard') as dashboard:
            with Provider('Employee Service') as employee_service:
                # Define the expected interactions
                expected_interaction = dashboard \
                    .given('Employees exist') \
                    .upon_receiving('A request to get employees') \
                    .with_request('GET', '/employees') \
                    .will_respond_with(200, body=Like([
                        {'name': 'John Doe', 'age': 30, 'department': 'IT'},
                        {'name': 'Jane Smith', 'age': 35, 'department': 'HR'}
                    ]))

                # Verify the contract
                dashboard.verify(employee_service, verbose=True)
