import json
import logging
import requests
import urllib


log = logging.getLogger(__name__)


class FleetIO(object):
    """
    General Notes:

    - Header as per supplied example:
        -H 'Authorization: Token token="YOUR_API_KEY"' 
        -H "Account-Token: YOUR_ACCOUNT_TOKEN"

    - The decision for separating each call(each request method has a separate function) 
      was made to make interactions with the API cleaner, although all functions 
      follow the same logic and code. It could have easily been designed in such
      a way that accommodates arguments for each method in a singal function.


    """
    def __init__(self, api_key, account_token):
        self.api_key = api_key
        self.account_token = account_token
        self.base_url = 'https://secure.fleetio.com/api/'
        self.version = 'v1/'
        self.call_url = self.base_url + self.version
        self.headers = {'Authorization':'Token token="%s"' % self.api_key, 'Account-Token': self.account_token}
            

        self.endpoints = {
            'accounts': 'accounts',
            'vehicles': 'vehicles/',
            'contacts': 'contacts/',
            'meter_entries': 'meter_entries/',
            'service_entries': 'service_entries/',
            'fuel_entries': 'fuel_entries/',
            'work_orders': 'work_orders/',
            'vehicle_assignments': 'vehicle_assignments/',
            'parts': 'parts/',
            'vehicle_statuses': 'vehicle_statuses/',
            'vehicle_types': 'vehicle_types/'}

    def api_get(self, endpoint, *identifier):
        """ Makes a FleetIO GET request

        Formats and submits a GET request to the specified endpoint.

        Args:
            endpoint: API endpoint to use.
            *identifier: The URL index for some endpoints.
                If you wish to get https://secure.fleetio.com/api/v1/vehicles/:vehicle_id/meter_entries 
                You would use the default_endpoint(vehicles) and then pass all other indexes to *identifier
                Example:
                    f = FleetIO('API_KEY', 'API_TOKEN')
                    r = f.api_get('vehicles', 'ID', 'meter_entries')
                The logic follows all api calls.


        Returns:
            A Requests object containing the result of the API call. Interact
            with the return value of this function as you would with any
            other Requests object.

        Raises:
            KeyError: the specified endpoint was not recognized. Check the
                docs.
            Requests.Exceptions.*: an error was raised by the Requests
                module.
        """
        uri_call = ''
        for uri in identifier:
            uri_call+=uri+'/'
        r = requests.get(self.call_url + self.endpoints[endpoint]+ uri_call, headers=self.headers)
        return r

    def api_post(self, endpoint, *identifier, **payload):
        """ Makes a FleetIO POST request

        Formats and submits a POST request to the specified endpoint.

        Args:
            endpoint: API endpoint to use.
            *identifier: The URL index for some endpoints. Not in use...but you never know :-)
            **payload: The parameters to pass.
                If you wish to post https://secure.fleetio.com/api/v1/contacts 
                You would use the default_endpoint(contact) and then pass all other parameters through payload
                Example:
                    f = FleetIO('API_KEY', 'API_TOKEN')
                    r = f.api_post('contacts', **{'first_name': 'John', 'last_name': 'Jon', 'email': 'John@Jon.com'})
                The logic follows all api calls.


        Returns:
            A Requests object containing the result of the API call. Interact
            with the return value of this function as you would with any
            other Requests object.

        Raises:
            KeyError: the specified endpoint was not recognized. Check the
                docs.
            Requests.Exceptions.*: an error was raised by the Requests
                module.
        """
        uri_call = ''
        for uri in identifier:
            uri_call+=uri+'/'
        r = requests.post(self.call_url + self.endpoints[endpoint]+ uri_call, params=payload, headers=self.headers)
        return r

    def api_patch(self, endpoint, *identifier, **payload):
        """ Makes a FleetIO PATCH request

        Formats and submits a PATCH request to the specified endpoint.

        Args:
            endpoint: API endpoint to use.
            *identifier: The URL index for some endpoints.
            **payload: The parameters to pass.
                If you wish to PATCH https://secure.fleetio.com/api/v1/contacts/:id
                You would use the default_endpoint(contact) and then pass all other parameters through payload
                Example:
                    f = FleetIO('API_KEY', 'API_TOKEN')
                    r = f.api_patch('contacts', 'ID', **{'email': 'John@Jon.com'})
                The logic follows all api calls.


        Returns:
            A Requests object containing the result of the API call. Interact
            with the return value of this function as you would with any
            other Requests object.

        Raises:
            KeyError: the specified endpoint was not recognized. Check the
                docs.
            Requests.Exceptions.*: an error was raised by the Requests
                module.
        """
        uri_call = ''
        for uri in identifier:
            uri_call+=uri+'/'
        r = requests.patch(self.call_url + self.endpoints[endpoint]+ uri_call, params=payload, headers=self.headers)
        return r

    def api_del(self, endpoint, *identifier):
        """ Makes a FleetIO DEL request

        Formats and submits a DEL request to the specified endpoint.

        Args:
            endpoint: API endpoint to use.
            *identifier: The URL index for some endpoints.
                If you wish to DEL https://secure.fleetio.com/api/v1/contacts/:id 
                You would use the default_endpoint(contact) and then pass all other parameters through payload
                Example:
                    f = FleetIO('API_KEY', 'API_TOKEN')
                    r = f.api_post('contacts', 'ID')
                The logic follows all api calls.


        Returns:
            A Requests object containing the result of the API call. Interact
            with the return value of this function as you would with any
            other Requests object.

        Raises:
            KeyError: the specified endpoint was not recognized. Check the
                docs.
            Requests.Exceptions.*: an error was raised by the Requests
                module.
        """
        uri_call = ''
        for uri in identifier:
            uri_call+=uri+'/'
        r = requests.delete(self.call_url + self.endpoints[endpoint]+ uri_call, headers=self.headers)
        return r

