CloudTrail Example Scenarios
============================

Both CloudTrail examples involve User Account data components. The first review the use of
User Account Modification to provide visbility into Account Manipulation (T1098), while the 
second considers User Account Metadata for detection of Password Policy Discovery (T1201)
behavior. 

Account Manipulation (T1098)
----------------------------

The following are the criteria considered for Account Manipulation (T1098). These were 
directly taken by reviewing the definition of the technique. 

.. image:: _static/CldTrlEx1.png
   :width: 700

1. Looking at the event logs themselves, is this enough proof or evidence to determine 
   “changes to account objects were made under this technique”?

   Most CloudTrail events are straightforward, and the associated API call performs a 
   User Account Modification that meets the criteria for proving an Account Manipulation 
   may have occurred. 

   User must be valid on system or domain

   - Any Action preserves an adversary access
   - Modifying credentials
   - Modifying permissions to groups
   - Activity designed to subvert security policies

 * TagUser

   Event information: `AWS Documentation <https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AddTags.html>`_

   Yes. Careful attention was given to CloudTrail Roles, and related information. For 
   example, the “TagUser/UntagUser” API entry was examined to determine that the act of 
   Tagging/Untagging met the conditions to change (give or takeaway) access. 

   One concept that came up was to also explore relevant sub-techniques, in case those could 
   provide additional insight in deciding if an event met the defined conditions: 

   - `Additional Cloud Credentials (T1098.001) <https://attack.mitre.org/techniques/T1098/001/>`_
   - `Additional Cloud Roles (T1098.003) <https://attack.mitre.org/techniques/T1098/003/>`_

 * UpdateUser

   Event information: `AWS Documentation <https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateUser.html>`_

   Yes. Another interesting event is UpdateUser. As an API call, it does not perform a 
   technical action that results in literal modification of concern (i.e., no access or 
   permissions for an IAM user is changed). It does not preserve adversary action in a 
   purely technical sense. HOWEVER: It does qualify because it could be used to “hide in 
   plain sight” The event is worth noting as potential evidence of (an unexpected) name 
   change.

 * UploadSigningCertificate

   Event information: `AWS Documentation <https://docs.aws.amazon.com/IAM/latest/APIReference/API_UploadSigningCertificate.html>`_

   Yes. This provides the name of the IAM user the signing certificate is for and the 
   contents of the signing certificate. The elements provide information that can be used 
   to look for changes to account objects.

 Additional information: `AWS Documentation <https://docs.aws.amazon.com/IAM/latest/APIReference/API_SetSecurityTokenServicePreferences.html>`_

Password Policy Discovery (T1201)
----------------------------------

The following are the criteria considered for Password Policy Discovery (T1201). These 
were directly taken by reviewing the definition of the technique. 

.. image:: _static/CldTrlEx2.png
   :width: 700

1. Looking at the event logs themselves, is this enough proof or evidence to determine 
   “are attempts being made to access detailed information about the password policy 
   under this technique”?

   This technique may be used by adversaries attempting to access/obtain detailed password 
   policy information. This policy information may aid the creation of password lists for 
   dictionary or brute force attacks.

 * CreatePolicyVersion

   Event information: `AWS Documentation <https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreatePolicyVersion.html>`_

   No. This contains details about IAM policy versions, but does not provide information about 
   attempts to access policy documents.

 * GetAccountPasswordPolicy

   Event information: `AWS Documentation <https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccountPasswordPolicy.html>`_

   Yes. The description of T1201 references that “password policies can be discovered in cloud 
   environments using available APIs such as GetAccountPasswordPolicy in AWS.”

   Select Examples of User Account Metadata events:

   * AttachRolePolicy
   * AttachUserPolicy
   * CreatePolicy
   * CreatePolicyVersion

   * DeleteAccountPasswordPolicy
   * DeletePolicyVersoin
   * DeleteRolePolicy
   * DeleteUserPolicy
   * DetachUserPolicy
   * DetachRolePolicy

   * ChangePassword
   * GenerateCredentialReport
   * GetAccountPasswordPolicy

   * ListAttachedRolePolicies
   * ListEntitiesForPolicy
   * ListPoliciesGrantingServiceAccess

 * GetLoginProfile

   Event information: `AWS Documentation <https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetLoginProfile.html>`_

   No. This contains information about IAM usernames and password creation dates, not 
   actual passwords or password policy constructs.