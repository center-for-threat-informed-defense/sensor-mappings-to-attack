ZEEK
====

Browse the Zeek mappings on this page, download the mappings (in CSV/STIX format), or
visualize the sensor coverage in ATT&CK Navigator.

.. raw:: html

    <p>
        <a class="btn btn-primary" target="_blank" href="../../csv/Zeek-sensors-mappings-enterprise.csv">
        <i class="fa fa-table"></i> Download CSV</a>

        <a class="btn btn-primary" target="_blank" href="../../stix/Zeek-mappings-enterprise.json">
        <i class="fa fa-file-excel-o"></i> Download STIX</a>

        <a class="btn btn-primary" target="_blank" href="https://mitre-attack.github.io/attack-navigator/#layerURL=https://center-for-threat-informed-defense.github.io/sensor-mappings-to-attack/navigator/Zeek-heatmap.json">
        <i class="fa fa-map-signs"></i> Open in ATT&CK Navigator</a>
    </p>

.. MAPPINGS_TABLE Generated at: 2025-03-20T10:08:37.277890Z

Enterprise
----------

.. list-table::
  :widths: 50 50
  :header-rows: 1

  * - EVENT
    - ATT&CK MAPPING

  * - | **arp_reply**
      |
      | Generated for ARP replies.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **arp_request**
      |
      | Generated for ARP requests.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **connection_SYN_packet**
      |
      | Generated for a SYN packet.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Connection Creation

  * - | **connection_attempt**
      |
      | Generated for an unsuccessful connection attempt.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **connection_eof**
      |
      | Generated at the end of reassembled TCP connections.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **connection_established**
      |
      | Generated when seeing a SYN-ACK packet from the responder in a TCP handshake.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Connection Creation

  * - | **connection_finished**
      |
      | Generated for a TCP connection that finished normally.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **connection_first_ack**
      |
      | Generated for the first ACK packet seen for a TCP connection from its originator.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Connection Creation

  * - | **connection_half_finished**
      |
      | Generated when one endpoint of a TCP connection attempted to gracefully close the connection, but the other endpoint is in the TCP_INACTIVE state.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **connection_partial_close**
      |
      | Generated when a previously inactive endpoint attempts to close a TCP connection via a normal FIN handshake or an abort RST sequence.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **connection_pending**
      |
      | Generated for each still-open TCP connection when Zeek terminates.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **connection_rejected**
      |
      | Generated for a rejected TCP connection.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **connection_reset**
      |
      | Generated when an endpoint aborted a TCP connection.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **dce_rpc_alter_context**
      |
      | Generated for every DCE-RPC alter context request message.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **dce_rpc_alter_context_resp**
      |
      | Generated for every DCE-RPC alter context response message.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **dce_rpc_bind**
      |
      | Generated for every DCE-RPC bind request message.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **dce_rpc_bind_ack**
      |
      | Generated for every DCE-RPC bind request ack message.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **dce_rpc_reply**
      |
      | Generated for every DCE-RPC reply message.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **dce_rpc_request**
      |
      | Generated for every DCE-RPC request message.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **dhcp_message**
      |
      | Generated for all DHCP messages.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **dns_AAAA_reply**
      |
      | Generated for DNS replies of type AAAA.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **dns_A_reply**
      |
      | Generated for DNS replies of type A.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **dns_CAA_reply**
      |
      | Generated for DNS replies of type CAA (Certification Authority Authorization).
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **dns_CNAME_reply**
      |
      | Generated for DNS replies of type CNAME.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **dns_DNSKEY_reply**
      |
      | Generated for DNS replies of type DNSKEY.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **dns_DS_reply**
      |
      | Generated for DNS replies of type DS.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **dns_EDNS_addl_reply**
      |
      | Generated for DNS replies of type EDNS.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **dns_EDNS_ecs_reply**
      |
      | Generated for DNS replies of type EDNS.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **dns_HINFO_reply**
      |
      | Generated for DNS replies of type HINFO.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **dns_MX_reply**
      |
      | Generated for DNS replies of type MX.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **dns_NSEC_reply**
      |
      | Generated for DNS replies of type NSEC.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **dns_NSEC_reply**
      |
      | Generated for DNS replies of type NSEC3.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **dns_NS_reply**
      |
      | Generated for DNS replies of type NS.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **dns_PTR_reply**
      |
      | Generated for DNS replies of type PTR.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **dns_RRSIG_reply**
      |
      | Generated for DNS replies of type RRSIG.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **dns_SOA_reply**
      |
      | Generated for DNS replies of type SOA.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **dns_SPF_reply**
      |
      | Generated for DNS replies of type SPF.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **dns_SRV_reply**
      |
      | Generated for DNS replies of type SRV.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **dns_TSIG_reply**
      |
      | Generated for DNS replies of type TSIG.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **dns_TXT_reply**
      |
      | Generated for DNS replies of type TXT.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **dns_WKS_reply**
      |
      | Generated for DNS replies of type WKS.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **dns_a6_reply**
      |
      | Generated for DNS replies of type A6.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **dns_request**
      |
      | Generated for DNS requests.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **dns_unknown_reply**
      |
      | Generated on DNS reply resource records when the type of record is not one that Zeek knows how to parse and generate another more specific event.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **ftp_reply**
      |
      | Generated for server-side FTP replies.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **ftp_request**
      |
      | Generated for client-side FTP commands.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **http_all_headers**
      |
      | Generated for HTTP headers, passing on all headers of an HTTP message at once.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **http_content_type**
      |
      | Generated for reporting an HTTP body’s content type.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **http_entity_data**
      |
      | Generated when parsing an HTTP body entity, passing on the data.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **http_reply**
      |
      | Generated for HTTP replies.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **http_request**
      |
      | Generated for HTTP requests.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **icmp_echo_reply**
      |
      | Generated for ICMP echo reply messages.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **icmp_echo_request**
      |
      | Generated for ICMP echo request messages.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **icmp_neighbor_advertisement**
      |
      | Generated for ICMP neighbor advertisement messages.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **icmp_neighbor_advertisement**
      |
      | Generated for ICMP router advertisement messages.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **icmp_neighbor_solicitation**
      |
      | Generated for ICMP neighbor solicitation messages.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **icmp_neighbor_solicitation**
      |
      | Generated for ICMP router solicitation messages.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **icmp_unreachable**
      |
      | Generated for ICMP destination unreachable messages.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **imap_capabilities**
      |
      | Generated when a server sends a capability list to the client, after being queried using the CAPABILITY command.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **imap_start_tls**
      |
      | Generated when a IMAP connection goes encrypted after a successful StartTLS exchange between the client and the server.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **krb_ap_request**
      |
      | A Kerberos 5 Authentication Header (AP) Request as defined in RFC 4120.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **krb_ap_response**
      |
      | A Kerberos 5 Authentication Header (AP) Response as defined in RFC 4120.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **krb_as_request**
      |
      | A Kerberos 5 Authentication Server (AS) Request as defined in RFC 4120.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **krb_as_response**
      |
      | A Kerberos 5 Authentication Server (AS) Response as defined in RFC 4120.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **krb_tgs_request**
      |
      | A Kerberos 5 Ticket Granting Service (TGS) Request as defined in RFC 4120.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **krb_tgs_response**
      |
      | A Kerberos 5 Ticket Granting Service (TGS) Response as defined in RFC 4120.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **mime_all_data**
      |
      | Generated for passing on all data decoded from a single email MIME message.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **mime_all_headers**
      |
      | Generated for MIME headers extracted from email MIME entities, passing all headers at once.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **mime_content_hash**
      |
      | Generated for decoded MIME entities extracted from email messages, passing on their MD5 checksums.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **mime_entity_data**
      |
      | Generated for data decoded from an email MIME entity.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **mount_proc_mnt**
      |
      | Generated for MOUNT3 request/reply dialogues of type mnt.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **mount_proc_not_implemented**
      |
      | Generated for MOUNT3 request/reply dialogues of a type that Zeek’s MOUNTv3 analyzer does not implement.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **mount_proc_null**
      |
      | Generated for MOUNT3 request/reply dialogues of type null.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **mount_proc_umnt**
      |
      | Generated for MOUNT3 request/reply dialogues of type umnt.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **mount_proc_umnt_all**
      |
      | Generated for MOUNT3 request/reply dialogues of type umnt_all.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **mount_reply_status**
      |
      | Generated for each MOUNT3 reply message received, reporting just the status included.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **netbios_session_accepted**
      |
      | Generated for NetBIOS messages of type positive session response.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **netbios_session_keepalive**
      |
      | Generated for NetBIOS messages of type keep-alive.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **netbios_session_message**
      |
      | Generated for all NetBIOS SSN and DGM messages.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **netbios_session_raw_message**
      |
      | Generated for NetBIOS messages of type session message that are not carrying an SMB payload.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **netbios_session_rejected**
      |
      | Generated for NetBIOS messages of type negative session response.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **netbios_session_request**
      |
      | Generated for NetBIOS messages of type session request.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **netbios_session_ret_arg_resp**
      |
      | Generated for NetBIOS messages of type retarget response.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **nfs_proc_create**
      |
      | Generated for NFSv3 request/reply dialogues of type create.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **nfs_proc_getattr**
      |
      | Generated for NFSv3 request/reply dialogues of type getattr.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **nfs_proc_link**
      |
      | Generated for NFSv3 request/reply dialogues of type link.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **nfs_proc_lookup**
      |
      | Generated for NFSv3 request/reply dialogues of type lookup.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **nfs_proc_mkdir**
      |
      | Generated for NFSv3 request/reply dialogues of type mkdir.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **nfs_proc_mkdir**
      |
      | Generated for NFSv3 request/reply dialogues of type null.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **nfs_proc_read**
      |
      | Generated for NFSv3 request/reply dialogues of type read.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **nfs_proc_readdir**
      |
      | Generated for NFSv3 request/reply dialogues of type readdir.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **nfs_proc_readlink**
      |
      | Generated for NFSv3 request/reply dialogues of type readlink.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **nfs_proc_remove**
      |
      | Generated for NFSv3 request/reply dialogues of type remove.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **nfs_proc_rename**
      |
      | Generated for NFSv3 request/reply dialogues of type rename.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **nfs_proc_rmdir**
      |
      | Generated for NFSv3 request/reply dialogues of type rmdir.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **nfs_proc_sattr**
      |
      | Generated for NFSv3 request/reply dialogues of type sattr.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **nfs_proc_symlink**
      |
      | Generated for NFSv3 request/reply dialogues of type symlink.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **nfs_proc_write**
      |
      | Generated for NFSv3 request/reply dialogues of type write.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **nfs_reply_status**
      |
      | Generated for each NFSv3 reply message received, reporting just the status included.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **ntlm_authenticate**
      |
      | Generated for NTLM messages of type authenticate.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Connection Creation

  * - | **ntlm_challenge**
      |
      | Generated for NTLM messages of type challenge.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Connection Creation

  * - | **ntlm_negotiate**
      |
      | Generated for NTLM messages of type negotiate.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **ntp_message**
      |
      | Generated for all NTP messages.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **partial_connection**
      |
      | Generated for a new active TCP connection if Zeek did not see the initial handshake.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **pm_attempt_callit**
      |
      | Generated for failed Portmapper requests of type callit.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **pm_attempt_dump**
      |
      | Generated for failed Portmapper requests of type dump.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **pm_attempt_getport**
      |
      | Generated for failed Portmapper requests of type getport.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **pm_attempt_null**
      |
      | Generated for failed Portmapper requests of type null.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **pm_attempt_set**
      |
      | Generated for failed Portmapper requests of type set.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **pm_attempt_unset**
      |
      | Generated for failed Portmapper requests of type unset.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **pm_bad_port**
      |
      | Generated for Portmapper requests or replies that include an invalid port number.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **pm_request_callit**
      |
      | Generated for Portmapper request/reply dialogues of type callit.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **pm_request_dump**
      |
      | Generated for Portmapper request/reply dialogues of type dump.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **pm_request_getport**
      |
      | Generated for Portmapper request/reply dialogues of type getport.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **pm_request_null**
      |
      | Generated for Portmapper request/reply dialogues of type null.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **pm_request_set**
      |
      | Generated for Portmapper request/reply dialogues of type set.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **pm_request_unset**
      |
      | Generated for Portmapper request/reply dialogues of type unset.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **pop3_data**
      |
      | Generated for server-side multi-line responses on POP3 connections.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **pop3_login_failure**
      |
      | Generated for unsuccessful authentications on POP3 connections.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **pop3_login_success**
      |
      | Generated for successful authentications on POP3 connections.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Connection Creation

  * - | **pop3_reply**
      |
      | Generated for server-side replies to commands on POP3 connections.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **pop3_request**
      |
      | Generated for client-side commands on POP3 connections.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **pop3_starttls**
      |
      | Generated when a POP3 connection goes encrypted.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **rdp_begin_encryption**
      |
      | Generated when an RDP session becomes encrypted.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **rdp_client_cluster_data**
      |
      | Generated for client cluster data packets.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **rdp_client_core_data**
      |
      | Generated for MCS client requests.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **rdp_client_network_data**
      |
      | Generated for Client Network Data (TS_UD_CS_NET) packets.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **rdp_client_security_data**
      |
      | Generated for client security data packets.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **rdp_connect_request**
      |
      | Generated for X.224 client requests.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **rdp_gcc_server_create_response**
      |
      | Generated for MCS server responses.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **rdp_native_encrypted_data**
      |
      | Generated for each packet after RDP native encryption begins.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **rdp_negotiation_failure**
      |
      | Generated for RDP Negotiation Failure messages.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **rdp_negotiation_response**
      |
      | Generated for RDP Negotiation Response messages.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **rdp_server_certificate**
      |
      | Generated for a server certificate section.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **rdp_server_security**
      |
      | Generated for MCS server responses.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **rdpeudp_data**
      |
      | Generated when for data messages exchanged after a RDPEUDP connection establishes
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **rdpeudp_established**
      |
      | Generated when RDPEUDP connections are established (both sides SYN)
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Connection Creation

  * - | **rdpeudp_syn**
      |
      | Generated for RDPEUDP SYN UDP Datagram
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Connection Creation

  * - | **rdpeudp_synack**
      |
      | Generated for RDPEUDP SYNACK UDP Datagram
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Connection Creation

  * - | **rpc_call**
      |
      | Generated for RPC call messages.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **rpc_dialogue**
      |
      | Generated for RPC request/reply pairs.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **rpc_reply**
      |
      | Generated for RPC reply messages.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **sip_all_headers**
      |
      | Generated once for all SIP headers from the originator or responder.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **sip_reply**
      |
      | Generated for SIP replies, used in Voice over IP (VoIP).
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **sip_request**
      |
      | Generated for SIP requests, used in Voice over IP (VoIP).
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **smb2_close_request**
      |
      | Generated for SMB/CIFS version 2 requests of type close.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **smb2_close_response**
      |
      | Generated for SMB/CIFS version 2 responses of type close.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **smb2_create_request**
      |
      | Generated for SMB/CIFS version 2 requests of type create.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **smb2_create_response**
      |
      | Generated for SMB/CIFS version 2 responses of type create.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **smb2_file_allocation**
      |
      | Generated for SMB/CIFS version 2 requests of type set_info of the allocation subtype
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **smb2_file_allocation**
      |
      | Generated for SMB/CIFS version 2 requests of type set_info of the delete subtype
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **smb2_file_endoffile**
      |
      | Generated for SMB/CIFS version 2 requests of type set_info of the end_of_file subtype
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **smb2_file_fscontrol**
      |
      | Generated for SMB/CIFS version 2 requests of type set_info of the fs_control subtype
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **smb2_file_fsobjectid**
      |
      | Generated for SMB/CIFS version 2 requests of type set_info of the fs_object_id subtype
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **smb2_file_fullea**
      |
      | Generated for SMB/CIFS version 2 requests of type set_info of the full_EA subtype
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **smb2_file_link**
      |
      | Generated for SMB/CIFS version 2 requests of type set_info of the link subtype
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **smb2_file_mode**
      |
      | Generated for SMB/CIFS version 2 requests of type set_info of the mode subtype
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **smb2_file_pipe**
      |
      | Generated for SMB/CIFS version 2 requests of type set_info of the pipe subtype
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **smb2_file_position**
      |
      | Generated for SMB/CIFS version 2 requests of type set_info of the position subtype
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **smb2_file_rename**
      |
      | Generated for SMB/CIFS version 2 requests of type set_info of the rename subtype
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **smb2_file_sattr**
      |
      | Generated for SMB/CIFS version 2 requests of type set_info of the sattr subtype
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **smb2_file_shortname**
      |
      | Generated for SMB/CIFS version 2 requests of type set_info of the short_name subtype
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **smb2_file_validdatalength**
      |
      | Generated for SMB/CIFS version 2 requests of type set_info of the valid_data_length subtype
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **smb2_negotiate_request**
      |
      | Generated for SMB/CIFS version 2 requests of type negotiate.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **smb2_negotiate_response**
      |
      | Generated for SMB/CIFS version 2 responses of type negotiate.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **smb2_read_request**
      |
      | Generated for SMB/CIFS version 2 requests of type read.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **smb2_session_setup_request**
      |
      | Generated for SMB/CIFS version 2 requests of type session_setup.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **smb2_session_setup_response**
      |
      | Generated for SMB/CIFS version 2 responses of type session_setup.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **smb2_transform_header**
      |
      | Generated for SMB/CIFS version 3.x transform_header.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **smb2_tree_connect_request**
      |
      | Generated for SMB/CIFS version 2 requests of type tree_connect.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **smb2_tree_connect_response**
      |
      | Generated for SMB/CIFS version 2 responses of type tree_connect.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **smb2_tree_disconnect_request**
      |
      | Generated for SMB/CIFS version 2 requests of type tree disconnect.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **smb2_tree_disconnect_response**
      |
      | Generated for SMB/CIFS version 2 responses of type tree disconnect.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **smb2_write_request**
      |
      | Generated for SMB/CIFS version 2 requests of type write.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **smb2_write_response**
      |
      | Generated for SMB/CIFS version 2 responses of type write.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **smtp_data**
      |
      | Generated for DATA transmitted on SMTP sessions.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **smtp_reply**
      |
      | Generated for server-side SMTP commands.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **smtp_request**
      |
      | Generated for client-side SMTP commands.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **smtp_starttls**
      |
      | Generated if a connection switched to using TLS using STARTTLS or X-ANONYMOUSTLS.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **snmp_encrypted_pdu**
      |
      | An SNMPv3 encrypted PDU message.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **snmp_get_bulk_request**
      |
      | An SNMP GetBulkRequest-PDU message from RFC 3416.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **snmp_get_next_request**
      |
      | An SNMP GetNextRequest-PDU message from either RFC 1157 or RFC 3416.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **snmp_get_request**
      |
      | An SNMP GetRequest-PDU message from either RFC 1157 or RFC 3416.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **snmp_inform_request**
      |
      | An SNMP InformRequest-PDU message from RFC 3416.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **snmp_report**
      |
      | An SNMP Report-PDU message from RFC 3416.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **snmp_response**
      |
      | An SNMP GetResponse-PDU message from RFC 1157 or a Response-PDU from RFC 3416.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **snmp_set_request**
      |
      | An SNMP SetRequest-PDU message from either RFC 1157 or RFC 3416.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **snmp_trap**
      |
      | An SNMP Trap-PDU message from RFC 1157.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **snmp_trapv2**
      |
      | An SNMP SNMPv2-Trap-PDU message from RFC 1157.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **socks_login_userpass_reply**
      |
      | Generated when a SOCKS server replies to a username/password login attempt.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Connection Creation

  * - | **socks_login_userpass_request**
      |
      | Generated when a SOCKS client performs username and password based login.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Connection Creation

  * - | **socks_reply**
      |
      | Generated when a SOCKS reply is analyzed.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **socks_request**
      |
      | Generated when a SOCKS request is analyzed.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **ssh1_server_host_key**
      |
      | During the SSH key exchange, the server supplies its public host key.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **ssh2_dh_server_params**
      |
      | Generated if the connection uses a Diffie-Hellman Group Exchange key exchange method.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Connection Creation

  * - | **ssh2_ecc_key**
      |
      | The ECDH and ECMQV key exchange algorithms use two ephemeral key pairs to generate a shared secret.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **ssh2_server_host_key**
      |
      | During the SSH key exchange, the server supplies its public host key.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **ssh_auth_attempted**
      |
      | This event is generated when an SSH connection was determined to have had an authentication attempt.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **ssh_auth_successful**
      |
      | This event is generated when an SSH connection was determined to have had a successful authentication.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Connection Creation

  * - | **ssh_capabilities**
      |
      | During the initial SSH key exchange, each endpoint lists the algorithms that it supports, in order of preference.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **ssh_client_version**
      |
      | An SSH Protocol Version Exchange message from the client.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **ssh_encrypted_packet**
      |
      | This event is generated when an SSH encrypted packet is seen.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **ssh_server_version**
      |
      | An SSH Protocol Version Exchange message from the server.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **ssl_alert**
      |
      | Generated for SSL/TLS alert records.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **ssl_change_cipher_spec**
      |
      | This event is raised when a SSL/TLS ChangeCipherSpec message is encountered before encryption begins.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **ssl_client_hello**
      |
      | Generated for an SSL/TLS client’s initial hello message.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Connection Creation

  * - | **ssl_dh_client_params**
      |
      | Generated if a client uses a DH-anon or DHE cipher suite.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **ssl_dh_server_params**
      |
      | Generated if a server uses a DH-anon or DHE cipher suite.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **ssl_ecdh_client_params**
      |
      | Generated if a client uses an ECDH-anon or ECDHE cipher suite.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **ssl_ecdh_server_params**
      |
      | Generated if a server uses an ECDH-anon or ECDHE cipher suite using a named curve This event contains the named curve name and the server ECDH parameters contained in the ServerKeyExchange message as defined in RFC 4492.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **ssl_encrypted_data**
      |
      | Generated for SSL/TLS messages that are sent after session encryption started.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **ssl_established**
      |
      | Generated at the end of an SSL/TLS handshake.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Connection Creation

  * - | **ssl_extension**
      |
      | Generated for SSL/TLS extensions seen in an initial handshake.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **ssl_handshake_message**
      |
      | This event is raised for each unencrypted SSL/TLS handshake message.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **ssl_heartbeat**
      |
      | Generated for SSL/TLS heartbeat messages that are sent before session encryption starts.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **ssl_rsa_client_pms**
      |
      | Generated if a client uses RSA key exchange.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Connection Creation

  * - | **ssl_server_hello**
      |
      | Generated for an SSL/TLS server’s initial hello message.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Connection Creation

  * - | **ssl_server_signature**
      |
      | Generated if a server uses a non-anonymous DHE or ECDHE cipher suite.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **ssl_session_ticket_handshake**
      |
      | Generated for SSL/TLS handshake messages that are a part of the stateless-server session resumption mechanism.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Connection Creation

  * - | **tcp_contents**
      |
      | Generated for each chunk of reassembled TCP payload.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **tcp_options**
      |
      | Generated for each TCP header that contains TCP options.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **tcp_packet**
      |
      | Generated for every TCP packet.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **tcp_rexmit**
      |
      | Generated for each detected TCP segment retransmission.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **udp_contents**
      |
      | Generated for UDP packets to pass on their payload.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **udp_reply**
      |
      | Generated for each packet sent by a UDP flow’s responder.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow

  * - | **udp_request**
      |
      | Generated for each packet sent by a UDP flow’s originator.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Flow
.. /MAPPINGS_TABLE
