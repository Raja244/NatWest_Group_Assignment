import unittest
from pact import Consumer, Provider

class DashboardServiceContractTest(unittest.TestCase):

    def test_dashboard_service_contract(self):
        # Define the consumer and provider
        with Consumer('Dashboard') as dashboard:
            with Provider('Employee Service') as employee_service:
                # Define the expected interactions
                expected_interaction = employee_service \
                    .given('Employees exist') \
                    .upon_receiving('A request to get employees for dashboard') \
                    .with_request('GET', '/employees') \
                    .will_respond_with(200, body=[
                        {'name': 'John Doe', 'age': 30, 'department': 'IT'},
                        {'name': 'Jane Smith', 'age': 35, 'department': 'HR'}
                    ])

                # Verify the contract
                employee_service.verify(dashboard, verbose=True)
