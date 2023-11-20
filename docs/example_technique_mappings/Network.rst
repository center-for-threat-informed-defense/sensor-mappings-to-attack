Network Example Scenario
========================

This example explores usage of events detected using network traffic content to provide 
potential visibility into detecting activity associated with Data from Configuration 
Repository: SNMP (T1602.001).

Data from Configuration Repository: SNMP (T1602.001)
----------------------------------------------------

The example explores the use of network traffic information to find evidence of the collection 
and/or mining of information in a network managed Data from Configuration Repository: SNMP 
(T1602.001). Network Traffic Content is a data component of this technique, and the Zeek events 
of Snmp_report, Ssl_plaintext_data, http_entity_data have been mapped to this data component 
under this project.

.. image:: _static/NetworkEx1.png
   :width: 700

1. Looking at the events themselves, is this enough proof or evidence to determine "data is 
   being collected or mined using Simple Network Management Protocol (SNMP)"?
   
   To find evidence of an adversary gathering data using SNMP, network traffic content and 
   patterns can be monitored and analyzed.  
   
 * snmp_report

   Event information: `Book of Zeek - snmp_report <https://docs.zeek.org/en/current/script-reference/proto-analyzers.html#id-snmp_report>`_

   Yes. Monitor and analyze unusual SNMP reply packet content and inspect information associated 
   with the host that sent it (e.g. snmp traffic originating from unauthorized or untrusted hosts, 
   signature detection for strings mapped to device configurations, anomolies in snmp requests).

 * ssl_plaintext_data

   Event information: `Book of Zeek - ssl_plaintext_data <https://docs.zeek.org/en/current/script-reference/proto-analyzers.html#id-ssl_plaintext_data>`_

   Yes. Inspect SSL/TLS messages sent before full session encryption starts for specific data 
   being collected.

 * http_entity_data

   Event information: `Book of Zeek - http_entity_data <https://docs.zeek.org/en/current/script-reference/proto-analyzers.html#id-http_entity_data>`_

   Not likely. This is useful for Hypertext Transfer Protocol (HTTP) traffic content, which is 
   also a TCP/IP protocol. SNMP communication through applets is possible using HTTP protocol, but
   is less efficient.