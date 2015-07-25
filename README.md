# python-fleetio

A simple Python interface for [FleetIO](http://www.fleetio.com/).

# Install

In terminal:

    python setup.py install

# API Example

    >>> from fleetio import FleetIO
    >>> f = FleetIO('api_key', 'account_token')
  
    # Create a GET call
    >>> r = f.api_get('accounts')
    >>> r.status_code
    200
    >>> r.json()
    [{u'token': u'TOKEN', u'role': u'owner', u'name': u'TEST_ACCOUNT'}]
    
    # Create a GET call (indexed)
    >>> r = f.api_get('vehicles') #return all vehicles
    >>> r.json()
    [{u'trim': None, u'meter_name': u'Odometer', u'color': u'', u'fuel_type_id': 61260, u'loan_interest_rate': None, u'vin': u'', u'license_plate': u'TEST', u'group_name': 
    {u'socialProfiles': [...], u'demographics': {...}, ..., u'id': XXXXXXX,}
    
    >>> r = f.api_get('vehicles', 'XXXXXXX') # return vehicles ID XXXXXXX
    >>> r.json()
    {u'trim': None, u'meter_name': u'Odometer', u'color': u''.....}

# Callable functions:
    api_get(self, endpoint, *identifier):  
        endpoint: API endpoint to use.
        *identifier: The URL index for some endpoints.  
        If you wish to get https://secure.fleetio.com/api/v1/vehicles/:vehicle_id/meter_entries   
        You would use the default_endpoint(vehicles) and then pass all other indexes to *identifier  
        Example:
    
        f = FleetIO('API_KEY', 'API_TOKEN')
        r = f.api_get('vehicles', 'ID', 'meter_entries')
---
    api_post(self, endpoint, *identifier, **payload):
        endpoint: API endpoint to use.
        *identifier: The URL index for some endpoints. Not in use...but you never know :-)
        **payload: The parameters to pass.
        If you wish to post https://secure.fleetio.com/api/v1/contacts 
        You would use the default_endpoint(contact) and then pass all other parameters through payload
        Example:
        
        f = FleetIO('API_KEY', 'API_TOKEN')
        r = f.api_post('contacts', **{'first_name': 'John', 'last_name': 'Jon', 'email': 'John@Jon.com'})
---
    api_patch(self, endpoint, *identifier, **payload):
        endpoint: API endpoint to use.
        *identifier: The URL index for some endpoints.
        **payload: The parameters to pass.
        If you wish to PATCH https://secure.fleetio.com/api/v1/contacts/:id
        You would use the default_endpoint(contact) and then pass all other parameters through payload
        Example:
        
        f = FleetIO('API_KEY', 'API_TOKEN')
        r = f.api_patch('contacts', 'ID', **{'email': 'John@Jon.com'})
---
    def api_del(self, endpoint, *identifier):
        endpoint: API endpoint to use.
        *identifier: The URL index for some endpoints.
        If you wish to DEL https://secure.fleetio.com/api/v1/contacts/:id 
        You would use the default_endpoint(contact) and then pass all other parameters through payload
        Example:
        
        f = FleetIO('API_KEY', 'API_TOKEN')
        r = f.api_post('contacts', 'ID')


# General Notes:
The decision for separating each call(each request method has a separate function) was made to make interactions with the API cleaner, although all functions follow the same logic and code. It could have easily been designed in such a way that accommodates arguments for each method in a singal function.
# FleetIO API Documentation

Check out FullContact's documentation [here](http://developer.fleetio.com/).
