CloudTrail
==========

Browse the CloudTrail mappings on this page, download the mappings (in CSV/STIX format), or
visualize the sensor coverage in ATT&CK Navigator.

.. raw:: html

    <p>
        <a class="btn btn-primary" target="_blank" href="../../csv/CloudTrail-sensors-mappings-enterprise.csv">
        <i class="fa fa-table"></i> Download CSV</a>

        <a class="btn btn-primary" target="_blank" href="../../stix/CloudTrail-mappings-enterprise.json">
        <i class="fa fa-file-excel-o"></i> Download STIX</a>

        <a class="btn btn-primary" target="_blank" href="https://mitre-attack.github.io/attack-navigator/#layerURL=https://center-for-threat-informed-defense.github.io/sensor-mappings-to-attack/navigator/CloudTrail-heatmap.json">
        <i class="fa fa-map-signs"></i> Open in ATT&CK Navigator</a>
    </p>

.. MAPPINGS_TABLE Generated at: 2025-03-20T10:08:37.278457Z

Enterprise
----------

.. list-table::
  :widths: 50 50
  :header-rows: 1

  * - EVENT
    - ATT&CK MAPPING

  * - | **AddClientIDToOpenIDConnectProvider**
      |
      | Adds a new client ID (also known as audience) to the list of client IDs already registered for the specified IAM OpenID Connect (OIDC) provider resource.
    - | **Data Source:** Active Directory
      | **Data Component:** Active Directory Object Modification

  * - | **AddRoleToInstanceProfile**
      |
      | Adds the specified IAM role to the specified instance profile. An instance profile can contain only one role, and this quota cannot be increased. You can remove the existing role and then add a different role to an instance profile.
    - | **Data Source:** Instance
      | **Data Component:** Instance Metadata

  * - | **AddUserToGroup**
      |
      | A user has been added to a group.
    - | **Data Source:** Group
      | **Data Component:** Group Modification

  * - | **AttachGroupPolicy**
      |
      | A managed policy has been added to an IAM group.
    - | **Data Source:** Group
      | **Data Component:** Group Modification

  * - | **AttachRolePolicy**
      |
      | A managed policy has been added to an IAM role.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **AttachUserPolicy**
      |
      | A managed policy has been added to an IAM user.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **ChangePassword**
      |
      | A password for an IAM user has been changed. Changes the password of the IAM user who is calling this operation. This operation can be performed using the AWS CLI, the AWS API, or the My Security Credentials page in the AWS Management Console. The AWS account root user password is not affected by this operation.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **ConsoleLogin**
      |
      | A user has signed into AWS Management Console. That user could be an account owner, a federated user or an IAM user.
    - | **Data Source:** Logon Session
      | **Data Component:** Logon Session Creation

  * - | **CreateAccessKey**
      |
      | A new AWS secret access key and access key ID has been created.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **CreateAccountAlias**
      |
      | Creates an alias for your AWS account.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **CreateGroup**
      |
      | A new group has been created.
    - | **Data Source:** Group
      | **Data Component:** Group Creation

  * - | **CreateImage**
      |
      | Creates an Amazon EBS-backed AMI from an Amazon EBS-backed instance that is either running or stopped.
    - | **Data Source:** Image
      | **Data Component:** Image Creation

  * - | **CreateInstanceProfile**
      |
      | Creates a new instance profile.
    - | **Data Source:** Instance
      | **Data Component:** Instance Metadata

  * - | **CreateLoginProfile**
      |
      | A new password has been created for a user to access AWS services through the management console.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **CreateOpenIDConnectProvider**
      |
      | Creates an IAM entity to describe an identity provider (IdP) that supports OpenID Connect (OIDC). The OIDC provider that you create with this operation can be used as a principal in a role's trust policy. Such a policy establishes a trust relationship between AWS and the OIDC provider.
    - | **Data Source:** Active Directory
      | **Data Component:** Active Directory Object Creation

  * - | **CreatePolicy**
      |
      | A new managed policy has been created for an AWS account.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **CreatePolicyVersion**
      |
      | Creates a new version of the specified managed policy. To update a managed policy, you create a new policy version. A managed policy can have up to five versions. If the policy has five versions, you must delete an existing version using DeletePolicyVersion before you create a new version.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **CreateRole**
      |
      | A new role for an AWS account has been created.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **CreateSAMLProvider**
      |
      | Creates an IAM resource that describes an identity provider (IdP) that supports SAML 2.0. The SAML provider resource that you create with this operation can be used as a principal in an IAM role's trust policy. Such a policy can enable federated users who sign in using the SAML IdP to assume the role. You can create an IAM role that supports Web-based single sign-on (SSO) to the AWS Management Console or one that supports API access to AWS. When you create the SAML provider resource, you upload a SAML metadata document that you get from your IdP.
    - | **Data Source:** Active Directory
      | **Data Component:** Active Directory Object Metadata

  * - | **CreateServiceLinkedRole**
      |
      | Creates an IAM role that is linked to a specific AWS service. The service controls the attached policies and when the role can be deleted. This helps ensure that the service is not broken by an unexpectedly changed or deleted role, which could put your AWS resources into an unknown state.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **CreateServiceSpecificCredential**
      |
      | Generates a set of credentials consisting of a user name and password that can be used to access the service specified in the request. These credentials are generated by IAM, and can be used only for the specified service. You can have a maximum of two sets of service-specific credentials for each supported service per user.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **CreateSnapshot**
      |
      | Creates a snapshot of an EBS volume and stores it in Amazon S3.
    - | **Data Source:** Snapshot
      | **Data Component:** Snapshot Creation

  * - | **CreateUser**
      |
      | A new IAM user has been created for an AWS account.
    - | **Data Source:** User Account
      | **Data Component:** User Account Creation

  * - | **CreateVirtualMFADevice**
      |
      | Creates a new virtual MFA device for the AWS account. After creating the virtual MFA, use EnableMFADevice to attach the MFA device to an IAM user.
    - | **Data Source:** User Account
      | **Data Component:** User Account Authentication

  * - | **CreateVolume**
      |
      | Creates an EBS volume that can be attached to an instance in the same Availability Zone.
    - | **Data Source:** Volume
      | **Data Component:** Volume Creation

  * - | **DeactivateMFADevice**
      |
      | Deactivates the specified MFA device and removes it from association with the user name for which it was originally enabled.
    - | **Data Source:** User Account
      | **Data Component:** User Account Authentication

  * - | **DeleteAccessKey**
      |
      | An access key pair for an IAM user has been deleted.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **DeleteAccountAlias**
      |
      | An AWS account alias has been deleted.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **DeleteAccountPasswordPolicy**
      |
      | A password policy for an account has been deleted.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **DeleteGroup**
      |
      | An IAM group has been deleted. The group won't have contained any users or policies at time of deletion.
    - | **Data Source:** Group
      | **Data Component:** Group Deletion

  * - | **DeleteGroupPolicy**
      |
      | An inline policy for an IAM group has been deleted.
    - | **Data Source:** Group
      | **Data Component:** Group Metadata

  * - | **DeleteInstanceProfile**
      |
      | Deletes the specified instance profile. The instance profile must not have an associated role.
    - | **Data Source:** Instance
      | **Data Component:** Instance Metadata

  * - | **DeleteLoginProfile**
      |
      | A password for an IAM user has been deleted thus removing that user's ability to access services through the console.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **DeleteOpenIDConnectProvider**
      |
      | Deletes an OpenID Connect identity provider (IdP) resource object in IAM. Deleting an IAM OIDC provider resource does not update any roles that reference the provider as a principal in their trust policies. Any attempt to assume a role that references a deleted provider fails.
    - | **Data Source:** Active Directory
      | **Data Component:** Active Directory Object Deletion

  * - | **DeletePolicyVersion**
      |
      | A version of a policy has been deleted.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **DeleteRole**
      |
      | A role has been deleted. The role will not have had any policies attached if it was able to be deleted.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **DeleteRolePermissionsBoundary**
      |
      | Deletes the permissions boundary for the specified IAM role. You cannot set the boundary for a service-linked role.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **DeleteRolePolicy**
      |
      | An inline policy for an IAM role has been deleted.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **DeleteSAMLProvider**
      |
      | Deletes a SAML provider resource in IAM. Deleting the provider resource from IAM does not update any roles that reference the SAML provider resource's ARN as a principal in their trust policies. Any attempt to assume a role that references a non-existent provider resource ARN fails.
    - | **Data Source:** Active Directory
      | **Data Component:** Active Directory Object Deletion

  * - | **DeleteSSHPublicKey**
      |
      | An SSH public key has been deleted. The SSH public key deleted by this operation is used only for authenticating the associated IAM user to an CodeCommit repository.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **DeleteServerCertificate**
      |
      | A server certificate has been deleted.
    - | **Data Source:** Certificate
      | **Data Component:** Certificate Deletion

  * - | **DeleteServiceLinkedRole**
      |
      | Submits a service-linked role deletion request and returns a DeletionTaskId, which you can use to check the status of the deletion. Before you call this operation, confirm that the role has no active sessions and that any resources used by the role in the linked service are deleted.
    - | **Data Source:** Cloud Service Account
      | **Data Component:** Cloud Service Account Metadata

  * - | **DeleteServiceSpecificCredential**
      |
      | Deletes the specified service-specific credential.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **DeleteSigningCertificate**
      |
      | A signing certificate has been deleted.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **DeleteSnapshot**
      |
      | Deletes the specified snapshot.
    - | **Data Source:** Snapshot
      | **Data Component:** Snapshot Deletion

  * - | **DeleteUser**
      |
      | A user has been deleted.
    - | **Data Source:** User Account
      | **Data Component:** User Account Deletion

  * - | **DeleteUserPermissionsBoundary**
      |
      | Deletes the permissions boundary for the specified IAM user.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **DeleteUserPolicy**
      |
      | An inline policy for an IAM user has been deleted.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **DeleteVirtualMFADevice**
      |
      | Deletes a virtual MFA device.
    - | **Data Source:** User Account
      | **Data Component:** User Account Authentication

  * - | **DetachGroupPolicy**
      |
      | Removes the specified managed policy from the specified IAM group.
    - | **Data Source:** Group
      | **Data Component:** Group Metadata

  * - | **DetachRolePolicy**
      |
      | A managed policy has been removed from a role.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **DetachUserPolicy**
      |
      | A managed policy has been removed from a user.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **DetachVolume**
      |
      | Detaches an EBS volume from an instance.
    - | **Data Source:** Volume
      | **Data Component:** Volume Modification

  * - | **EnableMFADevice**
      |
      | Enables the specified MFA device and associates it with the specified IAM user. When enabled, the MFA device is required for every subsequent login by the IAM user associated with the device.
    - | **Data Source:** User Account
      | **Data Component:** User Account Authentication

  * - | **GenerateCredentialReport**
      |
      | Retrieves a credential report for the AWS account.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **GenerateOrganizationsAccessReport**
      |
      | Generates a report for service last accessed data for AWS Organizations. You can generate a report for any entities (organization root, organizational unit, or account) or policies in your organization. To call this operation, you must be signed in using your Organizations management account credentials. You can use your long-term IAM user or root user credentials, or temporary credentials from assuming an IAM role. SCPs must be enabled for your organization root. You must have the required IAM and Organizations permissions.
    - | **Data Source:** Cloud Service Account
      | **Data Component:** Cloud Service Account Metadata

  * - | **GenerateServiceLastAccessedDetails**
      |
      | Generates a report that includes details about when an IAM resource (user, group, role, or policy) was last used in an attempt to access AWS services. Recent activity usually appears within four hours.
    - | **Data Source:** Cloud Service
      | **Data Component:** Cloud Service Metadata

  * - | **GetAccountAuthorizationDetails**
      |
      | Retrieves information about all IAM users, groups, roles, and policies in your AWS account, including their relationships to one another. Use this operation to obtain a snapshot of the configuration of IAM permissions (users, groups, roles, and policies) in your account.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **GetAccountPasswordPolicy**
      |
      | Retrieves the password policy for the AWS account. This tells you the complexity requirements and mandatory rotation periods for the IAM user passwords in your account.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **GetAccountSummary**
      |
      | Retrieves information about IAM entity usage and IAM quotas in the AWS account.
    - | **Data Source:** User Account
      | **Data Component:** User Account Access

  * - | **GetContextKeysForCustomPolicy**
      |
      | Gets a list of all of the context keys referenced in the input policies. The policies are supplied as a list of one or more strings. To get the context keys from policies associated with an IAM user, group, or role, use GetContextKeysForPrincipalPolicy.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **GetContextKeysForPrincipalPolicy**
      |
      | Gets a list of all of the context keys referenced in all the IAM policies that are attached to the specified IAM entity. The entity can be an IAM user, group, or role. If you specify a user, then the request also includes all of the policies attached to groups that the user is a member of.
    - | **Data Source:** Group
      | **Data Component:** Group Metadata

  * - | **GetContextKeysForPrincipalPolicy**
      |
      | Gets a list of all of the context keys referenced in all the IAM policies that are attached to the specified IAM entity. The entity can be an IAM user, group, or role. If you specify a user, then the request also includes all of the policies attached to groups that the user is a member of.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **GetCredentialReport**
      |
      | Retrieves a credential report for the AWS account.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **GetGroup**
      |
      | Returns a list of IAM users that are in the specified IAM group.
    - | **Data Source:** Group
      | **Data Component:** Group Access

  * - | **GetGroupPolicy**
      |
      | Retrieves the specified inline policy document that is embedded in the specified IAM group.
    - | **Data Source:** Group
      | **Data Component:** Group Metadata

  * - | **GetInstanceProfile**
      |
      | Retrieves information about the specified instance profile, including the instance profile's path, GUID, ARN, and role.
    - | **Data Source:** Instance
      | **Data Component:** Instance Metadata

  * - | **GetLoginprofile**
      |
      | Retrieves the user name and password-creation date for the specified IAM user.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **GetMFADevice**
      |
      | Retrieves information about an MFA device for a specified user.
    - | **Data Source:** User Account
      | **Data Component:** User Account Authentication

  * - | **GetOpenIDConnectProvider**
      |
      | Returns information about the specified OpenID Connect (OIDC) provider resource object in IAM.
    - | **Data Source:** Active Directory
      | **Data Component:** Active Directory Object Access

  * - | **GetOrganizationsAccessReport**
      |
      | Retrieves the service last accessed data report for AWS Organizations that was previously generated using the GenerateOrganizationsAccessReport operation. This operation retrieves the status of your report job and the report contents. .. To call this operation, you must be signed in to the management account in your organization. SCPs must be enabled for your organization root. You must have permissions to perform this operation.  For each service that principals in an account (root user, IAM users, or IAM roles) could access using SCPs, the operation returns details about the most recent access attempt.
    - | **Data Source:** Cloud Service Account
      | **Data Component:** Cloud Service Account Access

  * - | **GetPolicy**
      |
      | Retrieves information about the specified managed policy, including the policy's default version and the total number of IAM users, groups, and roles to which the policy is attached.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **GetPolicyVersion**
      |
      | Retrieves information about the specified version of the specified managed policy, including the policy document.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **GetRole**
      |
      | Retrieves information about the specified role, including the role's path, GUID, ARN, and the role's trust policy that grants permission to assume the role.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **GetRolePolicy**
      |
      | Retrieves the specified inline policy document that is embedded with the specified IAM role.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **GetSSHPublicKey**
      |
      | Retrieves the specified SSH public key, including metadata about the key. The SSH public key retrieved by this operation is used only for authenticating the associated IAM user to an CodeCommit repository.
    - | **Data Source:** User Account
      | **Data Component:** User Account Access

  * - | **GetServerCertificate**
      |
      | Retrieves information about the specified server certificate stored in IAM.
    - | **Data Source:** Certificate
      | **Data Component:** Certificate Access

  * - | **GetServiceLastAccessedDetails**
      |
      | Retrieves a service last accessed report that was created using the GenerateServiceLastAccessedDetails operation.   The report includes a list of AWS services that the resource (user, group, role, or managed policy) can access.
    - | **Data Source:** Cloud Service Account
      | **Data Component:** Cloud Service Account Metadata

  * - | **GetServiceLastAccessedDetailsWithEntities**
      |
      | After you generate a group or policy report using the GenerateServiceLastAccessedDetails operation, you can use the JobId parameter in GetServiceLastAccessedDetailsWithEntities. This operation retrieves the status of your report job and a list of entities that could have used group or policy permissions to access the specified service. Group – For a group report, this operation returns a list of users in the group that could have used the group’s policies in an attempt to access the service. Policy – For a policy report, this operation returns a list of entities (users or roles) that could have used the policy in an attempt to access the service. You can also use this operation for user or role reports to retrieve details about those entities.
    - | **Data Source:** Cloud Service Account
      | **Data Component:** Cloud Service Account Metadata

  * - | **GetServiceLinkedRoleDeletionStatus**
      |
      | Retrieves the status of your service-linked role deletion.
    - | **Data Source:** Cloud Service Account
      | **Data Component:** Cloud Service Account Access

  * - | **GetUser**
      |
      | Retrieves information about the specified IAM user, including the user's creation date, path, unique ID, and ARN.
    - | **Data Source:** User Account
      | **Data Component:** User Account Access

  * - | **GetUserPolicy**
      |
      | Retrieves the specified inline policy document that is embedded in the specified IAM user.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **ListAccessKeys**
      |
      | Returns information about the access key IDs associated with the specified IAM user. If there is none, the operation returns an empty list.
    - | **Data Source:** User Account
      | **Data Component:** User Account Enumeration

  * - | **ListAccountAliases**
      |
      | Lists the account alias associated with the AWS account (Note: you can have only one).
    - | **Data Source:** User Account
      | **Data Component:** User Account Enumeration

  * - | **ListAttachedGroupPolicies**
      |
      | Lists all managed policies that are attached to the specified IAM group.
    - | **Data Source:** Group
      | **Data Component:** Group Enumeration

  * - | **ListAttachedRolePolicies**
      |
      | Lists all managed policies that are attached to the specified IAM role.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **ListAttachedUserPolicies**
      |
      | Lists all managed policies that are attached to the specified IAM user.
    - | **Data Source:** User Account
      | **Data Component:** User Account Enumeration

  * - | **ListEntitiesForPolicy**
      |
      | Lists all IAM users, groups, and roles that the specified managed policy is attached to.
    - | **Data Source:** Group
      | **Data Component:** Group Metadata

  * - | **ListEntitiesForPolicy**
      |
      | Lists all IAM users, groups, and roles that the specified managed policy is attached to.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **ListGroupPolicies**
      |
      | Lists the names of the inline policies that are embedded in the specified IAM group.
    - | **Data Source:** Group
      | **Data Component:** Group Enumeration

  * - | **ListGroups**
      |
      | Lists the IAM groups that have the specified path prefix.
    - | **Data Source:** Group
      | **Data Component:** Group Enumeration

  * - | **ListGroupsForUser**
      |
      | Lists the IAM groups that the specified IAM user belongs to.
    - | **Data Source:** Group
      | **Data Component:** Group Enumeration

  * - | **ListInstanceProfileTags**
      |
      | Lists the tags that are attached to the specified IAM instance profile. The returned list of tags is sorted by tag key.
    - | **Data Source:** Instance
      | **Data Component:** Instance Metadata

  * - | **ListInstanceProfiles**
      |
      | Lists the instance profiles that have the specified path prefix. If there are none, the operation returns an empty list.
    - | **Data Source:** Instance
      | **Data Component:** Instance Metadata

  * - | **ListInstanceProfilesForRole**
      |
      | Lists the instance profiles that have the specified associated IAM role. If there are none, the operation returns an empty list.
    - | **Data Source:** Instance
      | **Data Component:** Instance Metadata

  * - | **ListMFADeviceTags**
      |
      | Lists the tags that are attached to the specified IAM virtual multi-factor authentication (MFA) device. The returned list of tags is sorted by tag key.
    - | **Data Source:** User Account
      | **Data Component:** User Account Authentication

  * - | **ListMFADevices**
      |
      | Lists the MFA devices for an IAM user. If the request includes a IAM user name, then this operation lists all the MFA devices associated with the specified user. If you do not specify a user name, IAM determines the user name implicitly based on the AWS access key ID signing the request for this operation.
    - | **Data Source:** User Account
      | **Data Component:** User Account Authentication

  * - | **ListOpenIDConnectProviderTags**
      |
      | Lists the tags that are attached to the specified OpenID Connect (OIDC)-compatible identity provider. The returned list of tags is sorted by tag key.
    - | **Data Source:** Active Directory
      | **Data Component:** Active Directory Object Enumeration

  * - | **ListOpenIDConnectProviders**
      |
      | Lists information about the IAM OpenID Connect (OIDC) provider resource objects defined in the AWS account.
    - | **Data Source:** Active Directory
      | **Data Component:** Active Directory Object Enumeration

  * - | **ListPolicies**
      |
      | Lists all the managed policies that are available in your AWS account, including your own customer-defined managed policies and all AWS managed policies.
    - | **Data Source:** User Account
      | **Data Component:** User Account Enumeration

  * - | **ListPoliciesGrantingServiceAccess**
      |
      | Retrieves a list of policies that the IAM identity (user, group, or role) can use to access each specified service. The list of policies returned by the operation depends on the ARN of the identity that you provide.
    - | **Data Source:** Group
      | **Data Component:** Group Metadata

  * - | **ListPoliciesGrantingServiceAccess**
      |
      | Retrieves a list of policies that the IAM identity (user, group, or role) can use to access each specified service. The list of policies returned by the operation depends on the ARN of the identity that you provide.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **ListPolicyTags**
      |
      | Lists the tags that are attached to the specified IAM customer managed policy. The returned list of tags is sorted by tag key.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **ListPolicyVersions**
      |
      | Lists information about the versions of the specified managed policy, including the version that is currently set as the policy's default version.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **ListRolePolicies**
      |
      | Lists the names of the inline policies that are embedded in the specified IAM role.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **ListRoleTags**
      |
      | Lists the tags that are attached to the specified role. The returned list of tags is sorted by tag key.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **ListRoles**
      |
      | Lists the IAM roles that have the specified path prefix. If there are none, the operation returns an empty list.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **ListSAMLProviderTags**
      |
      | Lists the tags that are attached to the specified Security Assertion Markup Language (SAML) identity provider. The returned list of tags is sorted by tag key.
    - | **Data Source:** Active Directory
      | **Data Component:** Active Directory Object Enumeration

  * - | **ListSAMLProviders**
      |
      | Lists the SAML provider resource objects defined in IAM in the account.
    - | **Data Source:** Active Directory
      | **Data Component:** Active Directory Object Enumeration

  * - | **ListSSHPublicKeys**
      |
      | Returns information about the SSH public keys associated with the specified IAM user. If none exists, the operation returns an empty list.
    - | **Data Source:** User Account
      | **Data Component:** User Account Enumeration

  * - | **ListServerCertificates**
      |
      | Lists the server certificates stored in IAM that have the specified path prefix. If none exist, the operation returns an empty list.
    - | **Data Source:** Certificate
      | **Data Component:** Certificate Enumeration

  * - | **ListServiceSpecificCredentials**
      |
      | Returns information about the service-specific credentials associated with the specified IAM user. If none exists, the operation returns an empty list. The service-specific credentials returned by this operation are used only for authenticating the IAM user to a specific service.
    - | **Data Source:** User Account
      | **Data Component:** User Account Enumeration

  * - | **ListSigningCertificates**
      |
      | Returns information about the signing certificates associated with the specified IAM user. If none exists, the operation returns an empty list.
    - | **Data Source:** User Account
      | **Data Component:** User Account Enumeration

  * - | **ListUserPolicies**
      |
      | Lists the names of the inline policies embedded in the specified IAM user.
    - | **Data Source:** User Account
      | **Data Component:** User Account Enumeration

  * - | **ListUserTags**
      |
      | Lists the tags that are attached to the specified IAM user. The returned list of tags is sorted by tag key.
    - | **Data Source:** User Account
      | **Data Component:** User Account Enumeration

  * - | **ListUsers**
      |
      | Lists the IAM users that have the specified path prefix. If no path prefix is specified, the operation returns all users in the AWS account.
    - | **Data Source:** User Account
      | **Data Component:** User Account Enumeration

  * - | **ListVirtualMFADevices**
      |
      | Lists the virtual MFA devices defined in the AWS account by assignment status. If you do not specify an assignment status, the operation returns a list of all virtual MFA devices.
    - | **Data Source:** User Account
      | **Data Component:** User Account Authentication

  * - | **ModifyImageAttribute**
      |
      | Modifies the specified attribute of the specified AMI. You can specify only one attribute at a time.
    - | **Data Source:** Image
      | **Data Component:** Image Modification

  * - | **ModifySnapshotAttribute**
      |
      | Adds or removes permission settings for the specified snapshot. You may add or remove specified AWS account IDs from a snapshot's list of create volume permissions, but you cannot do both in a single operation.
    - | **Data Source:** Snapshot
      | **Data Component:** Snapshot Modification

  * - | **ModifyVolume**
      |
      | You can modify several parameters of an existing EBS volume, including volume size, volume type, and IOPS capacity.
    - | **Data Source:** Volume
      | **Data Component:** Volume Modification

  * - | **PutGroupPolicy**
      |
      | A policy for an IAM group has been added or updated.
    - | **Data Source:** Group
      | **Data Component:** Group Metadata

  * - | **PutGroupPolicy**
      |
      | Adds or updates an inline policy document that is embedded in the specified IAM group.
    - | **Data Source:** Group
      | **Data Component:** Group Metadata

  * - | **PutRolePermissionsBoundary**
      |
      | Adds or updates the policy that is specified as the IAM role's permissions boundary. You can use an AWS managed policy or a customer managed policy to set the boundary for a role. Use the boundary to control the maximum permissions that the role can have. Setting a permissions boundary is an advanced feature that can affect the permissions for the role.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **PutRolePolicy**
      |
      | A policy for an IAM role has been added or updated.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **PutRolePolicy**
      |
      | Adds or updates an inline policy document that is embedded in the specified IAM role.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **PutUserPermissionsBoundary**
      |
      | Adds or updates the policy that is specified as the IAM user's permissions boundary. You can use an AWS managed policy or a customer managed policy to set the boundary for a user. Use the boundary to control the maximum permissions that the user can have. Setting a permissions boundary is an advanced feature that can affect the permissions for the user.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **PutUserPolicy**
      |
      | A policy for an IAM user has been added or updated.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **PutUserPolicy**
      |
      | Adds or updates an inline policy document that is embedded in the specified IAM role.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **RemoveClientIDFromOpenIDConnectProvider**
      |
      | Removes the specified client ID (also known as audience) from the list of client IDs registered for the specified IAM OpenID Connect (OIDC) provider resource object.
    - | **Data Source:** Active Directory
      | **Data Component:** Active Directory Object Modification

  * - | **RemoveRoleFromInstanceProfile**
      |
      | An IAM role has been removed from an EC2 instance profile.
    - | **Data Source:** Instance
      | **Data Component:** Instance Metadata

  * - | **RemoveUserFromGroup**
      |
      | A user has been removed from an IAM group.
    - | **Data Source:** Group
      | **Data Component:** Group Modification

  * - | **ResetServiceSpecificCredential**
      |
      | Resets the password for a service-specific credential. The new password is AWS generated and cryptographically strong. It cannot be configured by the user. Resetting the password immediately invalidates the previous password associated with this user.
    - | **Data Source:** Cloud Service Account
      | **Data Component:** Cloud Service Account Metadata

  * - | **ResyncMFADevice**
      |
      | Synchronizes the specified MFA device with its IAM resource object on the AWS servers.
    - | **Data Source:** User Account
      | **Data Component:** User Account Authentication

  * - | **RunInstances**
      |
      | An Instance has been launched. From the associated metadata you’ll be able to determine who the owner is, what regions the resources are in, the InstanceType and more.
    - | **Data Source:** Instance
      | **Data Component:** Instance Start

  * - | **SetDefaultPolicyVersion**
      |
      | A version of a policy has been set as a default. This can apply to users, groups and roles. To find specifics, use the ListEntitiesForPolicy API.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **SetSecurityTokenPreferences**
      |
      | Sets the specified version of the global endpoint token as the token version used for the AWS account.
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **SimulateCustomPolicy**
      |
      | Simulate how a set of IAM policies and optionally a resource-based policy works with a list of API operations and AWS resources to determine the policies' effective permissions. The policies are provided as strings.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **SimulatePrincipalPolicy**
      |
      | Simulate how a set of IAM policies attached to an IAM entity works with a list of API operations and AWS resources to determine the policies' effective permissions. The entity can be an IAM user, group, or role. If you specify a user, then the simulation also includes all of the policies that are attached to groups that the user belongs to. You can simulate resources that don't exist in your account.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **StartInstances**
      |
      | An instance has been started. Similar metadata to RunInstances will give you an insight into more detail.
    - | **Data Source:** Instance
      | **Data Component:** Instance Start

  * - | **StopInstances**
      |
      | Stops an Amazon EBS-backed instance. Similar to StartInstances and RunInstances.
    - | **Data Source:** Instance
      | **Data Component:** Instance Stop

  * - | **StopLogging**
      |
      | CloudTrail has stopped recording CloudTrail Events. This is a significant red flag and should almost always be avoided.
    - | **Data Source:** Cloud Service
      | **Data Component:** Cloud Service Disable

  * - | **TagInstanceProfile**
      |
      | Adds one or more tags to an IAM instance profile. If a tag with the same key name already exists, then that tag is overwritten with the new value.
    - | **Data Source:** Instance
      | **Data Component:** Instance Metadata

  * - | **TagMFADevice**
      |
      | Adds one or more tags to an IAM virtual multi-factor authentication (MFA) device. If a tag with the same key name already exists, then that tag is overwritten with the new value.
    - | **Data Source:** User Account
      | **Data Component:** User Account Authentication

  * - | **TagOpenIDConnectProvider**
      |
      | Adds one or more tags to an OpenID Connect (OIDC)-compatible identity provider.
    - | **Data Source:** Active Directory
      | **Data Component:** Active Directory Object Modification

  * - | **TagPolicy**
      |
      | Adds one or more tags to an IAM customer managed policy. If a tag with the same key name already exists, then that tag is overwritten with the new value.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **TagRole**
      |
      | Adds one or more tags to an IAM role. The role can be a regular role or a service-linked role. If a tag with the same key name already exists, then that tag is overwritten with the new value.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **TagSAMLProvider**
      |
      | Adds one or more tags to a Security Assertion Markup Language (SAML) identity provider.
    - | **Data Source:** Active Directory
      | **Data Component:** Active Directory Object Modification

  * - | **TagServerCertificate**
      |
      | Adds one or more tags to an IAM server certificate. If a tag with the same key name already exists, then that tag is overwritten with the new value.
    - | **Data Source:** Certificate
      | **Data Component:** Certificate Modification

  * - | **TagUser**
      |
      | Adds one or more tags to an IAM user. If a tag with the same key name already exists, then that tag is overwritten with the new value.
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **Untag Policy**
      |
      | Removes the specified tags from the customer managed policy.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **UntagInstanceProfile**
      |
      | Removes the specified tags from the IAM instance profile.
    - | **Data Source:** Instance
      | **Data Component:** Instance Metadata

  * - | **UntagMFADevice**
      |
      | Removes the specified tags from the IAM virtual multi-factor authentication (MFA) device.
    - | **Data Source:** User Account
      | **Data Component:** User Account Authentication

  * - | **UntagOpenIDConnectProvider**
      |
      | Removes the specified tags from the specified OpenID Connect (OIDC)-compatible identity provider in IAM.
    - | **Data Source:** Active Directory
      | **Data Component:** Active Directory Object Modification

  * - | **UntagRole**
      |
      | Removes the specified tags from the role.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **UntagSAMLProvider**
      |
      | Removes the specified tags from the specified Security Assertion Markup Language (SAML) identity provider in IAM.
    - | **Data Source:** Active Directory
      | **Data Component:** Active Directory Object Modification

  * - | **UntagServerCertificate**
      |
      | Removes the specified tags from the IAM server certificate.
    - | **Data Source:** Certificate
      | **Data Component:** Certificate Modification

  * - | **UntagUser**
      |
      | Removes the specified tags from the user.
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **UpdateAccessKey**
      |
      | Changes the status of the specified access key from Active to Inactive, or vice versa. This operation can be used to disable a user's key as part of a key rotation workflow.
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **UpdateAccountPasswordPolicy**
      |
      | Updates the password policy settings for the AWS account.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **UpdateAssumeRolePolicy**
      |
      | Updates the policy that grants an IAM entity permission to assume a role.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **UpdateGroup**
      |
      | Updates the name and/or the path of the specified IAM group.
    - | **Data Source:** Group
      | **Data Component:** Group Modification

  * - | **UpdateLoginProfile**
      |
      | Changes the password for the specified IAM user.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **UpdateOpenIDConnectProviderThumbprint**
      |
      | Replaces the existing list of server certificate thumbprints associated with an OpenID Connect (OIDC) provider resource object with a new list of thumbprints.
    - | **Data Source:** Active Directory
      | **Data Component:** Active Directory Object Modification

  * - | **UpdateRole**
      |
      | Updates the description or maximum session duration setting of a role.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **UpdateSAMLProvider**
      |
      | Updates the metadata document for an existing SAML provider resource object.
    - | **Data Source:** Active Directory
      | **Data Component:** Active Directory Object Modification

  * - | **UpdateSSHPublicKey**
      |
      | Sets the status of an IAM user's SSH public key to active or inactive. SSH public keys that are inactive cannot be used for authentication. This operation can be used to disable a user's SSH public key as part of a key rotation work flow.
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **UpdateServerCertificate**
      |
      | Updates the name and/or the path of the specified server certificate stored in IAM.
    - | **Data Source:** Certificate
      | **Data Component:** Certificate Modification

  * - | **UpdateServiceSpecificCredential**
      |
      | Sets the status of a service-specific credential to Active or Inactive. Service-specific credentials that are inactive cannot be used for authentication to the service. This operation can be used to disable a user's service-specific credential as part of a credential rotation work flow.
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **UpdateSigningCertificate**
      |
      | Changes the status of the specified user signing certificate from active to disabled, or vice versa. This operation can be used to disable an IAM user's signing certificate as part of a certificate rotation work flow.
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **UpdateUser**
      |
      | Updates the name and/or the path of the specified IAM user.
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **UploadSSHPublicKey**
      |
      | Uploads an SSH public key and associates it with the specified IAM user.
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **UploadServerCertificate**
      |
      | Uploads a server certificate entity for the AWS account. The server certificate entity includes a public key certificate, a private key, and an optional certificate chain, which should all be PEM-encoded.
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **UploadSigningCertificate**
      |
      | Uploads an X.509 signing certificate and associates it with the specified IAM user.
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification
.. /MAPPINGS_TABLE
