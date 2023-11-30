Linux Example Scenario
======================

The Linux example explores `Local Account (T1136.001)
<https://attack.mitre.org/techniques/T1136/001>`__ and usage of the mappings done under
this project to provide visibility using the Auditd events: ``ADD_USER`` and
``ANOM_ADD_ACCOUNT``.


Create Local Account (T1136.001)
--------------------------------

This example explores Auditd events mapped to the User Account Creation data component and
their potential visibility into detecting activity associated with Create Local Account
(T1136.001).

.. image:: ../_static/linuxex1.png

**Looking at the event data, is this enough evidence to conclude that a user account was
created per T1136.001?** It could be inferred by the name of the technique and the names
of the Auditd events of ADD_USER and ANOM_ADD_ACCOUNT that these events may be
associated with the technique. Further context is needed, though to see if these events
can be directly associated with the technique. Use ``/var/log/audit/audit.log`` to
search on event names.

**ADD_USER:**

*Yes.* This event is triggered when a user account is created, which in this case could
be directly associated with User Account Creation of a local account.

**ANOM_ADD_ACCOUNT:**

*No.* This event is only triggered when the addition of account ends abnormally. It does
not simply provide information specifically for new account creation.

*References:*

* `Linux man page - auditd(8) <https://www.man7.org/linux/man-pages/man8/auditd.8.html>`_

.. warning::

  Systemd Journal is a Linux system service that collects and stores logging data. Systemd
  Journal reflects user creation activity and attendant commands but does not appear to
  display the event names in RHEL-derived distributions. Also, Systemd Journal is not 100%
  accurate. For example, user creation/deletion events are not copied from auditd to the
  journal with perfect fidelity, depending on distribution.
