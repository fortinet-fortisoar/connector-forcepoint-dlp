""" Copyright start
  Copyright (C) 2024 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

import requests
from connectors.core.connector import get_logger, ConnectorError
import json
import urllib3
from datetime import datetime
urllib3.disable_warnings()
logger = get_logger('forcepoint-dlp')

class ForcePointDlp(object):
    
    def __init__(self, config):       
        self.host = config.get('server_url', None)
        self.user = config.get('username', None)
        self.password = config.get('password', None)
        self.protocol = config.get('protocol', None)
        self.port = config.get('port', None)
        self.verify_ssl = config.get('verify_ssl', None)
        
        if self.host.startswith('http') or self.host.startswith('https'):
            self.base_url = '{host}:{port}/dlp/rest/v1/'.format(host=self.host.rstrip('/'),port=self.port) 
        else:
            self.base_url = '{protocol}://{host}:{port}/dlp/rest/v1/'.format(protocol=self.protocol,
                                                                            host=self.host.rstrip('/'),
                                                                            port=self.port)
                      
    def _make_api_call(self, endpoint=None, method='GET', headers=None, health_check=False, data=None):
        
        if endpoint:
            url  = self.base_url + endpoint
        else:
            url = self.base_url
        try:
            logger.debug('Making a request with {0} method and {1} headers.'.format(method, headers))
            response = requests.request(method, url, headers=headers, data=data, verify=self.verify_ssl)
            if response.status_code in [200, 420, ]:
                if health_check:
                    return response
                try:
                    logger.debug(
                        'Converting the response into JSON format after returning with status code: {0}'.format(
                            response.status_code))
                    response_data = response.json()
                    return {'status': response_data['status'] if 'status' in response_data else 'Success',
                            'data': response_data}
                except Exception as e:
                    response_data = response.content
                    logger.error('Failed with an error: {0}. The response details are: {1}'.format(e, response_data))
                    return {'status': 'Failure', 'data': response_data}
            else:
                logger.error('Failed with response {0}'.format(response))
                raise ConnectorError(
                    {'status': 'Failure', 'status_code': str(response.status_code), 'response': response})
        except Exception as e:
            logger.exception(str(e))
            raise ConnectorError(str(e))
        
    def _get_token(self):
        try:
            headers = {'Content-Type': 'application/json', 'username': self.user, 'password': self.password}
            response_data = self._make_api_call(endpoint='auth/refresh-token', method='POST', headers=headers)
            refresh_token = response_data.get('data').get('refresh_token')
            if refresh_token:
                headers = {'Content-Type': 'application/json', 'refresh-token': f'Bearer {refresh_token}'}
                response_data = self._make_api_call(endpoint='auth/access-token', method='POST', headers=headers)
                return response_data.get('data').get('access_token') if response_data else None
            else:
                logger.debug('Token not generated.') 
                            
        except Exception as err:
            logger.exception('Health check failed with: {0}'.format(err))
            raise ConnectorError('Health check failed with: {0}'.format(err))    

def _check_health(config):
    try:
        obj = ForcePointDlp(config)
        user = config.get('username', None)
        password = config.get('password', None)
        headers = {'Content-Type': 'application/json', 'username': user, 'password': password}
        obj._make_api_call(endpoint='auth/refresh-token', method='POST', headers=headers, health_check=True)
        return True
    except Exception as err:
        logger.exception('Health check failed with: {0}'.format(err))
        raise ConnectorError('Health check failed with: {0}'.format(err))
            
def get_list_of_incidents_by_filter(config, params):
    try:
        obj = ForcePointDlp(config)
        access_token = obj._get_token()
        if access_token:
            payload = {
                'type': params.get('type'),
                'sort_by': params.get('sort_by'),
                'from_date':datetime.fromisoformat(params.get('from_date')[:-1]).strftime("%d/%m/%Y %H:%M:%S") if params.get('from_date') else '',
                'to_date': datetime.fromisoformat(params.get('to_date')[:-1]).strftime("%d/%m/%Y %H:%M:%S") if params.get('to_date') else '',
                'detected_by': params.get('detected_by'),
                'analyzed_by': params.get('analyzed_by'),
                'event_id': params.get('event_id'),
                'destination': params.get('destination'),
                'policies': params.get('policies'),
                'action': params.get('action'),
                'source': params.get('source'),
                'status': params.get('status'),
                'severity': params.get('severity'),
                'endpoint_type': params.get('endpoint_type'),
                'channel': params.get('channel'),
                'assigned_to': params.get('assigned_to'),
                'tag': params.get('tag')
            }
            payload = {key: value for key, value in payload.items() if value is not None and value != "" }
            headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {access_token}'}
            return obj._make_api_call(endpoint='incidents', method='POST', headers=headers, data=json.dumps(payload))           
        else :
            return logger.error('Failed to obtain access token.') 
    except ConnectorError as e:
        logger.error(f'Failed with error: {e}')
    
def get_incidents_by_ids(config, params):
    try:
        obj = ForcePointDlp(config)
        access_token = obj._get_token()
        if access_token:
            ids = str(params.get('ids')).split(',')
            payload = {
                'type': params.get('type'),
                'ids': list(map(int, ids))
            }
            payload = {key: value for key, value in payload.items() if value is not None and value != ""}
            headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {access_token}'}
            return obj._make_api_call(endpoint='incidents', method='POST', headers=headers, data=json.dumps(payload))
        else :
            return logger.error('Failed to obtain access token.')
    except ConnectorError as e:
        logger.error(f'Failed with error: {e}')


def get_incidents_by_date_range(config, params):
    try:
        obj = ForcePointDlp(config)
        access_token = obj._get_token()
        if access_token:
            payload = {
                    'type': params.get('type'),
                    'from_date': datetime.fromisoformat(params.get('from_date')[:-1]).strftime("%d/%m/%Y %H:%M:%S") if params.get('from_date') else '',
                    'to_date': datetime.fromisoformat(params.get('to_date')[:-1]).strftime("%d/%m/%Y %H:%M:%S") if params.get('to_date') else ''
            }
            payload = {key: value for key, value in payload.items() if value is not None and value != "" }
            headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {access_token}'}
            return obj._make_api_call(endpoint='incidents', method='POST', headers=headers, data=json.dumps(payload))
        else :
            return logger.error('Failed to obtain access token.') 
    except ConnectorError as e:
        logger.error(f'Failed with error: {e}')
        
def get_incidents_by_action(config, params):
    try:
        obj = ForcePointDlp(config)
        access_token = obj._get_token()
        if access_token:
            payload = {
                    'type': params.get('type'),
                    'from_date': datetime.fromisoformat(params.get('from_date')[:-1]).strftime("%d/%m/%Y %H:%M:%S") if params.get('from_date') else '',
                    'to_date': datetime.fromisoformat(params.get('to_date')[:-1]).strftime("%d/%m/%Y %H:%M:%S") if params.get('to_date') else '',
                    'action': params.get('action')    
            }
            payload = {key: value for key, value in payload.items() if value is not None and value != "" }
            headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {access_token}'}
            return obj._make_api_call(endpoint='incidents', method='POST', headers=headers, data=json.dumps(payload))
        else :
            return logger.error('Failed to obtain access token.') 
    except ConnectorError as e:
        logger.error(f'Failed with error: {e}')

def get_incidents_by_severity(config, params):
    try:
        obj = ForcePointDlp(config)
        access_token = obj._get_token()
        if access_token:
            payload = {
                    'type': params.get('type'),
                    'from_date':datetime.fromisoformat(params.get('from_date')[:-1]).strftime("%d/%m/%Y %H:%M:%S") if params.get('from_date') else '',
                    'to_date': datetime.fromisoformat(params.get('to_date')[:-1]).strftime("%d/%m/%Y %H:%M:%S") if params.get('to_date') else '',
                    'severity': params.get('severity')    
            }
            payload = {key: value for key, value in payload.items() if value is not None and value != ""}
            headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {access_token}'}
            return obj._make_api_call(endpoint='incidents', method='POST', headers=headers, data=json.dumps(payload))
        else :
            return logger.error('Failed to obtain access token.') 
    except ConnectorError as e:
        logger.error(f'Failed with error: {e}')
        
def get_incidents_by_status(config, params):
    try:
        obj = ForcePointDlp(config)
        access_token = obj._get_token()
        if access_token:
            payload = {
                    'type': params.get('type'),
                    'from_date':datetime.fromisoformat(params.get('from_date')[:-1]).strftime("%d/%m/%Y %H:%M:%S") if params.get('from_date') else '',
                    'to_date': datetime.fromisoformat(params.get('to_date')[:-1]).strftime("%d/%m/%Y %H:%M:%S") if params.get('to_date') else '',
                    'status': params.get('status')    
            }
            payload = {key: value for key, value in payload.items() if value is not None and value != "" }
            headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {access_token}'}
            return obj._make_api_call(endpoint='incidents', method='POST', headers=headers, data=json.dumps(payload))
        else :
            return logger.error('Failed to obtain access token.') 
    except ConnectorError as e:
        logger.error(f'Failed with error: {e}')

def get_incidents_by_policy_name(config, params):
    try:
        obj = ForcePointDlp(config)
        access_token = obj._get_token()
        if access_token:
            payload = {
                    'type': params.get('type'),
                    'from_date':datetime.fromisoformat(params.get('from_date')[:-1]).strftime("%d/%m/%Y %H:%M:%S") if params.get('from_date') else '',
                    'to_date': datetime.fromisoformat(params.get('to_date')[:-1]).strftime("%d/%m/%Y %H:%M:%S") if params.get('to_date') else '',
                    'policies': params.get('policies')
            }
            payload = {key: value for key, value in payload.items() if value is not None and value != ""}
            headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {access_token}'}
            return obj._make_api_call(endpoint='incidents', method='POST', headers=headers, data=json.dumps(payload))
        else :
            return logger.error('Failed to obtain access token.') 
    except ConnectorError as e:
        logger.error(f'Failed with error: {e}')        

def update_incident_status_by_incident_id_and_partition_index(config, params):
    try:
        obj = ForcePointDlp(config)
        access_token = obj._get_token()
        if access_token:
            if  params.get('type') == 'INCIDENTS':
                incident_ids = str(params.get('incident_id')).split(',')
                partition_index = params.get('partition_index')
                if partition_index is not None: 
                    incident_keys = [{'incident_id': int(id), 'partition_index': partition_index} for id in incident_ids]
                else:
                    incident_keys = [{'incident_id': int(id)} for id in incident_ids]
                payload ={
                    'incident_keys': incident_keys,
                    'type': params.get('type'),
                    'action_type': params.get('action_type'),
                    'value':  params.get('value')
                }
            else:  
                incident_ids = str(params.get('incident_id')).split(',')
                incident_keys = [{'incident_id': int(id)} for id in incident_ids] 
                payload ={
                    'incident_keys': incident_keys,
                    'type': params.get('type'),
                    'action_type': params.get('action_type'),
                    'value':  params.get('value')
                }
            payload = {key: value for key, value in payload.items() if value is not None and value != "" }
            headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {access_token}'}
            return obj._make_api_call(endpoint='incidents/update', method='POST', headers=headers, data=json.dumps(payload))           
        else :
            return logger.error('Failed to obtain access token.') 
    except ConnectorError as e:
        logger.error(f'Failed with error: {e}')   

def update_incident_status_by_scan_partitions(config, params):
    try:
        obj = ForcePointDlp(config)
        access_token = obj._get_token()
        if access_token:
            if  params.get('type') == 'INCIDENTS':
                incident_ids = str(params.get('incident_id')).split(',')
                partition_index = params.get('partition_index')
                if partition_index is not None: 
                    incident_keys = [{'incident_id': int(id), 'partition_index': partition_index} for id in incident_ids]
                else:
                    incident_keys = [{'incident_id': int(id)} for id in incident_ids]
                payload ={
                    'incident_keys': incident_keys,
                    'type': params.get('type'),
                    'action_type': params.get('action_type'),
                    'value':  params.get('value'),
                    'scan_partitions':  params.get('scan_partitions')
                }
            else:  
                incident_ids = str(params.get('incident_id')).split(',')
                incident_keys = [{'incident_id': int(id)} for id in incident_ids] 
                payload ={
                    'incident_keys': incident_keys,
                    'type': params.get('type'),
                    'action_type': params.get('action_type'),
                    'value':  params.get('value'),
                    'scan_partitions':  params.get('scan_partitions')
                }
            payload = {key: value for key, value in payload.items() if value is not None and value != "" }
            headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {access_token}'}
            return obj._make_api_call(endpoint='incidents/update', method='POST', headers=headers, data=json.dumps(payload))           
        else :
            return logger.error('Failed to obtain access token.') 
    except ConnectorError as e:
        logger.error(f'Failed with error: {e}')   
        
def update_incident_status_by_event_ids(config, params):
    try:
        obj = ForcePointDlp(config)
        access_token = obj._get_token()
        if access_token:
            event_ids = str(params.get('event_ids')).split(',')
            payload = {
                    'event_ids': list(map(int, event_ids)),
                    'type': params.get('type'),
                    'action_type': params.get('action_type'),
                    'value':  params.get('value'),
                    'status': params.get('status')    
            }
            payload = {key: value for key, value in payload.items() if value is not None and value != "" }
            headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {access_token}'}
            return obj._make_api_call(endpoint='incidents', method='POST', headers=headers, data=json.dumps(payload))
        else :
            return logger.error('Failed to obtain access token.') 
    except ConnectorError as e:
        logger.error(f'Failed with error: {e}')               
operations = {
    'get_list_of_incidents_by_filter': get_list_of_incidents_by_filter,
    'get_incidents_by_ids': get_incidents_by_ids,
    'get_incidents_by_date_range': get_incidents_by_date_range,
    'get_incidents_by_severity': get_incidents_by_severity,
    'get_incidents_by_status' : get_incidents_by_status,
    'get_incidents_by_action': get_incidents_by_action,
    'get_incidents_by_policy_name': get_incidents_by_policy_name,
    'update_incident_status_by_incident_id_and_partition_index': update_incident_status_by_incident_id_and_partition_index,
    'update_incident_status_by_scan_partitions': update_incident_status_by_scan_partitions,
    'update_incident_status_by_event_ids':update_incident_status_by_event_ids
}
