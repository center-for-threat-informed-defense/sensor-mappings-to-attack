Use Cases
=========

Target Audience
---------------

The existing communities of Sensors and ATT&CK users include many roles and responsibilities 
associated with organizational detection processes and procedures. These roles and responsibilities 
include: 

Incident Response (IR) Professional
    Responsibilities include response,
    management, and coordination, and remediation activities for cyber incidents such as
    malware infections, data theft, ransomware encryption, denial of service, and
    control systems intrusions.

Chief Information Security Officer (CISO)
    Responsibilities include carrying
    out information security policies, procedures, and controls, and providing primary
    interface between senior managers and information system owners.

Information System Security Officer (ISSO)
    Responsibilities include ensuring
    the appropriate operational security posture is maintained for information systems
    or programs.

Security Operations Center (SOC) Analyst
    Responsibilities include monitoring
    an organization's networks and systems to detect threats and investigating potential
    security incidents.

Security Engineer (SE)
    Responsibilities include developing and implementing
    security controls and solutions to protect networks and systems from unauthorized
    access and attacks.

Usage
-----

Understanding Current Visibility
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
*What is my coverage for known adversary TTPs given my current tools?*

- Understand which techniques you have visibility into given current set of tools and capabilities.

<img src="./docs/_static/visibility.png" width="900px">

Filling Defensive Gaps
^^^^^^^^^^^^^^^^^^^^^^
*If I were to add Tool X, how does that coverage change?*

- Identify tools and capabilities to acquire or enable in order to fill gaps.

<img src="./docs/_static/gaps.png" width="900px">

Find Potential Threats
^^^^^^^^^^^^^^^^^^^^^^
*I'm concerned about a recent threat report. Can I see it if it were to happen in my environment and where do I look?*

- Determine which tools and capabilities to use to find adversary behaviors.

<img src="./docs/_static/threats.png" width="900px">

User Stories
------------

This section describes user stories associated with organizational detection processes and 
procedures, based on the roles and usage identified above.

1. As an IR, I want to ensure I have complete visibility of an active security incident.  

   Use the mappings to take the observed adversary behaviors as described in ATT&CK to understand current visibility of potential suspicious activities and tie in actionable intelligence from CTI reporting. 

2. As a CISO or ISSO, I need to align defensive posture with the real-world threats targeting my industry.  

   Use the mappings to understand which of tools and capabilities provide visibility into specific real-world adversary techniques and where gaps may lie. 

3. As a SOC Analyst, I need visibility into threats launched against my organization.  

   Use the mappings for identified Data Sources associated with adversary techniques used to identify areas to look for additional indicators of potential suspicious activities. 

4. As a SE, I want to detect entire classes of adversarial behavior.  

   Build in defensive countermeasures for specific adversary TTPs, using the mappings to identify areas and fill in defensive coverage gaps by reconfiguring existing or adding additional tools or capabilities.
