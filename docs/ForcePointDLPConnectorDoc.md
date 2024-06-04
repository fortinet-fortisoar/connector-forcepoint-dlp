## About the connector
Forcepoint DLP used to prevent data leakage, ensure regulatory compliance, protect intellectual property, manage employee productivity, mitigate risks, and respond to security incidents within organizations.
<p>This document provides information about the Forcepoint DLP Connector, which facilitates automated interactions, with a Forcepoint DLP server using FortiSOAR&trade; playbooks. Add the Forcepoint DLP Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Forcepoint DLP.</p>

### Version information

Connector Version: 1.0.0


Authored By: spryIQ.co

Certified: No
## Installing the connector
<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-forcepoint-dlp`

## Prerequisites to configuring the connector
- You must have the URL of Forcepoint DLP server to which you will connect and perform automated operations and credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Forcepoint DLP server.

## Minimum Permissions Required
- N/A

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Forcepoint DLP</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Server URL<br></td><td>Specify the URL of the Forcepoint dlp server to connect and perform automated operations.<br>
<tr><td>Username<br></td><td>Username used to access the Forcepoint DLP server to which you will connect and perform the automated operations.<br>
<tr><td>Password<br></td><td>Password used to access the Forcepoint DLP server to which you will connect and perform the automated operations.<br>
<tr><td>Protocol<br></td><td>Protocol that will be used to communicate with the Forcepoint DLP server. Choose either http and https.By default, this is set to https.<br>
<tr><td>Port<br></td><td>Port number used for connecting to the Forcepoint DLP server.Defaults to 9443 for the https protocol.<br>
<tr><td>Verify SSL<br></td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set as True.<br></td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Get Incidents by IDs<br></td><td>List incidents by ids.<br></td><td>get_incidents_by_ids <br/>Investigation<br></td></tr>
<tr><td>Get Incidents by Date Range<br></td><td>List incidents by date range.<br></td><td>get_incidents_by_date_range <br/>Investigation<br></td></tr>
<tr><td>Get Incidents by Action<br></td><td>List incidents by action.<br></td><td>get_incidents_by_action <br/>Investigation<br></td></tr>
<tr><td>Get Incidents by Severity<br></td><td>List incidents by severity.<br></td><td>get_incidents_by_severity <br/>Investigation<br></td></tr>
<tr><td>Get Incidents by Status<br></td><td>List incidents by status.<br></td><td>get_incidents_by_status <br/>Investigation<br></td></tr>
<tr><td>Get Incidents by Policy Name<br></td><td>List incidents by policy_name.<br></td><td>get_incidents_by_policy_name <br/>Investigation<br></td></tr>
<tr><td>Get List Of Incident By Filter<br></td><td>Retrieves a list of all incident on a registered system.<br></td><td>get_list_of_incidents_by_filter <br/>Investigation<br></td></tr>
<tr><td>Update Incident Status By Incident ID And Partition Index<br></td><td>Update Incident Status By Incident ID And Partition Index.<br></td><td>update_incident_status_by_incident_id_and_partition_index <br/>Investigation<br></td></tr>
<tr><td>Update Incident Status By Scan Partitions<br></td><td>Update incident status by scan partitions<br></td><td>update_incident_status_by_scan_partitions <br/>Investigation<br></td></tr>
<tr><td>Update Incident Status By Event IDs<br></td><td>Update incident status by event ids<br></td><td>update_incident_status_by_event_ids <br/>Investigation<br></td></tr>
</tbody></table>

### operation: Get Incidents by IDs
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Type<br></td><td>Select option 'INCIDENTS' or 'DISCOVERY'.<br>
</td></tr><tr><td>IDs<br></td><td>Specify the ids comma separated value that you want to retrieve from Forecpoint DLP.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "incidents": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "severity": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "action": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "tag": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "source": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "email_address": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "event_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "maximum_matches": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "transaction_size": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "analyzed_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ignored_incidents": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "event_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "incident_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "channel": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "policies": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "partition_index": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "destination": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "detected_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "details": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "released_incident": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "violation_triggers": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "file_name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "total_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "total_returned": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "not_found_ids": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ]
</code><code><br>}</code>

### operation: Get Incidents by Date Range
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Type<br></td><td>Select option 'INCIDENTS' or 'DISCOVERY'.<br>
</td></tr><tr><td>From Date<br></td><td>Specify 'from date' to fetch data from Forcepoint DLP server.<br>
</td></tr><tr><td>To Date<br></td><td>Specify 'to date' to fetch data from Forcepoint DLP server.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "incidents": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "severity": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "action": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "tag": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "source": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "email_address": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "event_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "maximum_matches": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "transaction_size": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "analyzed_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ignored_incidents": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "event_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "incident_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "channel": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "policies": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "partition_index": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "destination": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "detected_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "details": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "released_incident": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "violation_triggers": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "file_name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "total_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "total_returned": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "not_found_ids": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ]
</code><code><br>}</code>

### operation: Get Incidents by Action
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Type<br></td><td>Select option 'INCIDENTS' or 'DISCOVERY'.<br>
</td></tr><tr><td>From Date<br></td><td>Specify 'from date' to fetch data from Forcepoint DLP server.<br>
</td></tr><tr><td>To Date<br></td><td>Specify 'to date' to fetch data from Forcepoint DLP server.<br>
</td></tr><tr><td>Action<br></td><td>Specify 'action' to fetch data from Forcepoint DLP server.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "incidents": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "severity": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "action": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "tag": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "source": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "email_address": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "event_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "maximum_matches": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "transaction_size": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "analyzed_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ignored_incidents": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "event_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "incident_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "channel": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "policies": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "partition_index": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "destination": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "detected_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "details": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "released_incident": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "violation_triggers": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "file_name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "total_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "total_returned": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "not_found_ids": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ]
</code><code><br>}</code>

### operation: Get Incidents by Severity
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Type<br></td><td>Select option 'INCIDENTS' or 'DISCOVERY'.<br>
</td></tr><tr><td>From Date<br></td><td>Specify 'from date' to fetch data from Forcepoint DLP server.<br>
</td></tr><tr><td>To Date<br></td><td>Specify 'to date' to fetch data from Forcepoint DLP server.<br>
</td></tr><tr><td>Severity<br></td><td>Specify 'severity' to fetch data from Forcepoint DLP server.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "incidents": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "severity": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "action": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "tag": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "source": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "email_address": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "event_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "maximum_matches": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "transaction_size": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "analyzed_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ignored_incidents": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "event_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "incident_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "channel": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "policies": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "partition_index": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "destination": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "detected_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "details": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "released_incident": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "violation_triggers": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "file_name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "total_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "total_returned": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "not_found_ids": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ]
</code><code><br>}</code>

### operation: Get Incidents by Status
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Type<br></td><td>Select option 'INCIDENTS' or 'DISCOVERY'.<br>
</td></tr><tr><td>From Date<br></td><td>Specify 'from date' to fetch data from Forcepoint DLP server.<br>
</td></tr><tr><td>To Date<br></td><td>Specify 'to date' to fetch data from Forcepoint DLP server.<br>
</td></tr><tr><td>Status<br></td><td>Specify 'status' to fetch data from Forcepoint DLP server.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "incidents": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "severity": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "action": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "tag": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "source": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "email_address": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "event_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "maximum_matches": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "transaction_size": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "analyzed_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ignored_incidents": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "event_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "incident_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "channel": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "policies": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "partition_index": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "destination": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "detected_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "details": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "released_incident": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "violation_triggers": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "file_name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "total_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "total_returned": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "not_found_ids": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ]
</code><code><br>}</code>

### operation: Get Incidents by Policy Name
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Type<br></td><td>Select option 'INCIDENTS' or 'DISCOVERY'.<br>
</td></tr><tr><td>From Date<br></td><td>Specify 'from date' to fetch data from Forcepoint DLP server.<br>
</td></tr><tr><td>To Date<br></td><td>Specify 'to date' to fetch data from Forcepoint DLP server.<br>
</td></tr><tr><td>Policies<br></td><td>Specify 'policies' to fetch data from Forcepoint DLP server.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "incidents": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "severity": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "action": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "tag": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "source": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "email_address": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "event_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "maximum_matches": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "transaction_size": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "analyzed_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ignored_incidents": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "event_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "incident_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "channel": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "policies": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "partition_index": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "destination": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "detected_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "details": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "released_incident": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "violation_triggers": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "file_name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "total_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "total_returned": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "not_found_ids": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ]
</code><code><br>}</code>

### operation: Get List Of Incident By Filter
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Type<br></td><td>Select option 'INCIDENTS' or 'DISCOVERY'.<br>
</td></tr><tr><td>Sort By<br></td><td>Specify 'sort by' to fetch data from Forcepoint DLP server.<br>
</td></tr><tr><td>From Date<br></td><td>Specify 'from date' to fetch data from Forcepoint DLP server.<br>
</td></tr><tr><td>To Date<br></td><td>Specify 'to date' to fetch data from Forcepoint DLP server.<br>
</td></tr><tr><td>Detected By<br></td><td>Specify 'detected by' to fetch data from Forcepoint DLP server.<br>
</td></tr><tr><td>Analyzed By<br></td><td>Specify 'Policy Engine ID' to fetch data from Forcepoint DLP server.<br>
</td></tr><tr><td>Event ID<br></td><td>Specify 'event id' to fetch data from Forcepoint DLP server.<br>
</td></tr><tr><td>Destination<br></td><td>Specify 'destination' to fetch data from Forcepoint DLP server.<br>
</td></tr><tr><td>Policies<br></td><td>Specify 'policies' to fetch data from Forcepoint DLP server.<br>
</td></tr><tr><td>Action<br></td><td>Specify 'action' to fetch data from Forcepoint DLP server.<br>
</td></tr><tr><td>Source<br></td><td>Specify 'source' to fetch data from Forcepoint DLP server.<br>
</td></tr><tr><td>Status<br></td><td>Specify 'status' to fetch data from Forcepoint DLP server.<br>
</td></tr><tr><td>Severity<br></td><td>Specify 'severity' to fetch data from Forcepoint DLP server.<br>
</td></tr><tr><td>Endpoint Type<br></td><td>Specify 'endpoint type' to fetch data from Forcepoint DLP server.<br>
</td></tr><tr><td>Channel<br></td><td>Specify 'channel' to fetch data from Forcepoint DLP server.<br>
</td></tr><tr><td>Assigned To<br></td><td>Specify 'assigned to' to fetch data from Forcepoint DLP server.<br>
</td></tr><tr><td>Tag<br></td><td>Specify 'tag' to fetch data from Forcepoint DLP server.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "incidents": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "severity": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "action": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "tag": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "source": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "email_address": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "event_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "maximum_matches": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "transaction_size": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "analyzed_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ignored_incidents": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "event_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "incident_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "channel": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "policies": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "partition_index": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "destination": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "detected_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "details": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "released_incident": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "violation_triggers": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "file_name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "total_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "total_returned": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "not_found_ids": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ]
</code><code><br>}</code>

### operation: Update Incident Status By Incident ID And Partition Index
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Type<br></td><td>Select option 'INCIDENTS' or 'DISCOVERY'.<br>
<strong>If you choose 'INCIDENTS'</strong><ul><li>Incident IDs: Specify array of the Incident IDs comma separated to be updated.</li><li>Partition Index: Partition Index from the incidents table that are required to build a query. If this field is not provided on an INCIDENTS request, then the system should look up this parameter internally. In this case, the API will require more resources to complete the update action.</li></ul><strong>If you choose 'DISCOVERY'</strong><ul><li>Incident IDs: Specify array of the Incident IDs comma separated to be updated.</li></ul></td></tr><tr><td>Action Type<br></td><td>Specify 'action type' to fetch data from Forcepoint DLP server.<br>
<strong>If you choose 'STATUS'</strong><ul><li>Value: Specify value to fetch data from Forcepoint DLP server.</li><strong>If you choose 'Custom Status'</strong><ul><li>Enter Custom Status: Specify value to fetch data from Forcepoint DLP server.</li></ul></ul><strong>If you choose 'SEVERITY'</strong><ul><li>Value: Specify value to fetch data from Forcepoint DLP server.</li></ul><strong>If you choose 'ASSIGN_TO'</strong><ul><li>Value: Specify value to fetch data from Forcepoint DLP server.</li></ul><strong>If you choose 'ADD_COMMENT'</strong><ul><li>Value: Specify value to fetch data from Forcepoint DLP server.</li></ul><strong>If you choose 'TAG'</strong><ul><li>Value: Enter Tag Name Max 100 Chars.</li></ul><strong>If you choose 'FALSE_POSITIVE'</strong><ul><li>Value: Specify value to fetch data from Forcepoint DLP server.</li></ul></td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "incidents": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "severity": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "action": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "tag": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "source": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "email_address": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "event_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "maximum_matches": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "transaction_size": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "analyzed_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ignored_incidents": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "event_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "incident_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "channel": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "policies": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "partition_index": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "destination": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "detected_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "details": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "released_incident": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "violation_triggers": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "file_name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "total_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "total_returned": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "not_found_ids": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ]
</code><code><br>}</code>

### operation: Update Incident Status By Scan Partitions
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Type<br></td><td>Select option 'INCIDENTS' or 'DISCOVERY'.<br>
<strong>If you choose 'INCIDENTS'</strong><ul><li>Incident IDs: Specify array of the Incident IDs comma separated to be updated.</li><li>Partition Index: Partition Index from the incidents table that are required to build a query. If this field is not provided on an INCIDENTS request, then the system should look up this parameter internally. In this case, the API will require more resources to complete the update action.</li></ul><strong>If you choose 'DISCOVERY'</strong><ul><li>Incident IDs: Specify array of the Incident IDs comma separated to be updated.</li></ul></td></tr><tr><td>Action Type<br></td><td>Specify 'action type' to fetch data from Forcepoint DLP server.<br>
<strong>If you choose 'STATUS'</strong><ul><li>Value: Specify value to fetch data from Forcepoint DLP server.</li><strong>If you choose 'Custom Status'</strong><ul><li>Enter Custom Status: Specify value to fetch data from Forcepoint DLP server.</li></ul></ul><strong>If you choose 'SEVERITY'</strong><ul><li>Value: Specify value to fetch data from Forcepoint DLP server.</li></ul><strong>If you choose 'ASSIGN_TO'</strong><ul><li>Value: Specify value to fetch data from Forcepoint DLP server.</li></ul><strong>If you choose 'ADD_COMMENT'</strong><ul><li>Value: Specify value to fetch data from Forcepoint DLP server.</li></ul><strong>If you choose 'TAG'</strong><ul><li>Value: Enter Tag Name Max 100 Chars.</li></ul><strong>If you choose 'FALSE_POSITIVE'</strong><ul><li>Value: Specify value to fetch data from Forcepoint DLP server.</li></ul></td></tr><tr><td>Scan Partitions<br></td><td>Specify 'scan partitions' to fetch data from Forcepoint DLP server.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "incidents": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "severity": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "action": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "tag": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "source": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "email_address": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "event_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "maximum_matches": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "transaction_size": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "analyzed_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ignored_incidents": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "event_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "incident_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "channel": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "policies": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "partition_index": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "destination": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "detected_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "details": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "released_incident": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "violation_triggers": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "file_name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "total_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "total_returned": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "not_found_ids": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ]
</code><code><br>}</code>

### operation: Update Incident Status By Event IDs
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Type<br></td><td>Select option 'INCIDENTS' or 'DISCOVERY'.<br>
</td></tr><tr><td>Event IDs<br></td><td>Specify 'event ids' to fetch data from Forcepoint DLP server.<br>
</td></tr><tr><td>Action Type<br></td><td>Specify 'action type' to fetch data from Forcepoint DLP server.<br>
<strong>If you choose 'STATUS'</strong><ul><li>Value: Specify value to fetch data from Forcepoint DLP server.</li><strong>If you choose 'Custom Status'</strong><ul><li>Enter Custom Status: Specify value to fetch data from Forcepoint DLP server.</li></ul></ul><strong>If you choose 'SEVERITY'</strong><ul><li>Value: Specify value to fetch data from Forcepoint DLP server.</li></ul><strong>If you choose 'ASSIGN_TO'</strong><ul><li>Value: Specify value to fetch data from Forcepoint DLP server.</li></ul><strong>If you choose 'ADD_COMMENT'</strong><ul><li>Value: Specify value to fetch data from Forcepoint DLP server.</li></ul><strong>If you choose 'TAG'</strong><ul><li>Value: Enter Tag Name Max 100 Chars.</li></ul><strong>If you choose 'FALSE_POSITIVE'</strong><ul><li>Value: Specify value to fetch data from Forcepoint DLP server.</li></ul></td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "incidents": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "severity": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "action": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "tag": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "source": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "email_address": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "event_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "maximum_matches": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "transaction_size": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "analyzed_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ignored_incidents": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "event_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "incident_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "channel": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "policies": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "partition_index": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "destination": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "detected_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "details": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "released_incident": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "violation_triggers": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "file_name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "total_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "total_returned": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "not_found_ids": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ]
</code><code><br>}</code>
## Included playbooks
The `Sample - forcepoint-dlp - 1.0.0` playbook collection comes bundled with the Forcepoint DLP connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the Forcepoint DLP connector.

- Get Incidents by IDs
- Get Incidents by Date Range
- Get Incidents by Action
- Get Incidents by Severity
- Get Incidents by Status
- Get Incidents by Policy Name
- Get List Of Incident By Filter
- Update Incident Status By Incident ID And Partition Index
- Update Incident Status By Scan Partitions
- Update Incident Status By Event IDs

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.
