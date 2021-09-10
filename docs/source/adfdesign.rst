***************************
Azure Data Factory Design Principles 
***************************

Open access and reusable Design documentation of utilities and modular pipelines used in the NHSX Analytics Unit Azure Data Factory (ADF) environment.

.. image:: _static/img/adf_logo.png
  :width: 300
  :alt: ADF 

ADF utilities
========

Latest Folder Lookup
---------------------

**Developed by:** Craig Shenton and Mattia Ficarelli 

The latest folder lookup ADF utility allows you to find the most recent folder from a directory of time-stamped folders. This utility was developed from a method to get the latest added file in a folder, the source of which can be found `here <https://stackoverflow.com/questions/60558731/get-the-latest-added-file-in-a-folder-azure-data-factory/60558836#60558836>`_. 

**Problem:** Data is saved in directory of time stamped folders, as shown below.

.. code:: python
  root/
  ├── directory/
  │   ├── 2021-06-01/
  │   ├── 2021-06-02/
  │   ├── 2021-06-03/
  │   └── 2021-06-04/

How to select the latest folder in an ADF pipeline based on the name of the folder (rather than the latest modified)?

**Solution:**


**Pipeline setup:**
#.Create two pipeline variables: ``latestFolder`` and ``prevFolder`` (see Figure 1).
  a. The ``latestFolder`` variable is an empty string to save the latest folder name.
  b. The ``prevFolder`` variable is set to a historical date before you started collecting data for example, ‘1970-01-01’

*Figure 1: Adding pipeline variables*

#. Create a 'folder_metadata' dataset with the path set to the root directory of the time-stamped folder for example, ``root/directory/``

*Figure 2: Creating a folder_metadata dataset*

#. Create a GetMetadata activity. More information on the GetMetadata ADF activity can be found `here <https://docs.microsoft.com/en-us/azure/data-factory/control-flow-get-metadata-activity>`_ (see Figure 3).
  a. Link the 'folder_metadata' dataset to the GetMetadata activity under the dataset tab.
  b. Add a 'Field List' argument as ``Child Items``, this will list each subfolder in the 'folder metadata' dataset.

*Figure 3: Creating a GetMetadata activity*

**Loop setup:**

#. Create a ForEach activity. More information on the ForEach ADF activity can be found `here <https://docs.microsoft.com/en-us/azure/data-factory/control-flow-for-each-activity>`_ (see Figure 4).
  a. In the ForEach activity settings, set 'items' as ``@activity('get_folder_metadata').output.childItems``.

*Figure 4: Creating a ForEach activity*

#. Within the ForEach activity create a second get GetMetadata activity (see Figure 5).
  a. Create a 'date metadata' dataset with the path set to: ``@concat('root/directory/',dataset().latestDate)``.
  b. Set the target dataset to 'date_metadata' and add a parameter to the dataset called ``latestDate``. 

#. In the second GetMetadata activity set the parameter ``latestDate`` to ``@item().name``.

*Figure 5: Creating a second GetMetadata activity, within the previously created ForEach activity*

**Conditional setup:**

#. Create a If Conditional activity. More information on the If Conditional ADF activity can be found `here <https://docs.microsoft.com/en-us/azure/data-factory/control-flow-if-condition-activity>`_.
  a. Set the expression in the If Conditional activity (added as dynamic content) as ``@greater(formatDateTime(activity('get_folder_metadata_2').output.itemName,'yyyyMMdd'),formatDateTime(variables('prevFolder'),'yyyyMMdd'))``. This will check if the name of each folder (formatted as a date) is greater (i.e., the latest) than the previous folder in the loop, starting with the default value - '1970-01-01' (see Figure 6).

*Figure 6: Setting an expression within an If Conditional activity*

#. In the If Conditional activity where ``Case = True`` (i.e.,  if the folder name is greater than the previous folder name) create a new Set Variable activity. More information on the Set Variable ADF activity can be found `here <https://docs.microsoft.com/en-us/azure/data-factory/control-flow-set-variable-activity>`_ (see Figure 7).
  a. Within the Set Variable activity set ``Name = latestFolder`` and ``Value = @activity('get_folder_metadata_2').output.itemName``.


*Figure 7: Creating a Set Variable activity*



NHS-App-Analytics-Dashboard
===========================

The NHS App dashboard enables you to see how many patients are using the NHS App across England, and which features they are using. It can be accessed by anyone with an NHS email address.

Information you can get through the dashboard
---------------------------------------------
You can choose to view figures at weekly or monthly data level.

You can view figures broken down by:

#. Regions
#. Sustainability and Transformation Partnerships (STP)
#. Clinical Commissioning Groups (CCG)
#. GP practice

You can view figures for the use of the individual features of the NHS App at any of these levels,  including:

#. Registrations – and registrations by patients who have not previously used patient online access
#. Appointment bookings and cancellations
#. Record reviews
#. Prescription requests
#. Visits to NHS 111 online
#. Organ donation registrations and withdrawals
#. Users visiting the health A-Z
#. Users visiting the national data opt-out site

The data is updated weekly, every Wednesday at 7:30am.

How to access the dashboard
---------------------------
To access the dashboard, you need to log in to your OKTA account. This is the same account used for other NHS Improvement services on the NHS Improvement website. Log in and then click on ‘My account’, select ‘Your analytical products’ and select ‘NHS App dashboard’.

Access the NHS App Dashboard: (https://tabanalytics.data.england.nhs.uk/#/views/NHSAppDashboard/Uptake)

Background to the NHS App dashboard
-----------------------------------
The NHS App dashboard is provided by NHSX, NHS Digital, and NHS England and Improvement. It enables those working in the health and care system to monitor the adoption and uptake of the NHS App. This information can then support strategic decision making at all levels of the system.

NHS App Data Dictionary
=======================

+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| Metric Name                                             | Description                                                                                                |
+=========================================================+============================================================================================================+
| NHS App Registrations                                   | Number of App users who have obtained P9 verification (full access) in the specified reporting period      |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| % of GP patients aged 13+ yrs, registered for NHS App   | Proportion of GP registered population registered for the NHS App to date (cumulative)                     |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| NHS App downloads                                       | Number of NHS App downloads from Google and Apple Stores in the specified reporting period                 |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| Total GP registered patients aged 13+ years             | Number of patients registered at a general practice to date (cumulative)                                   |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| GP population registered for Patient Online             | Number of 'online patients' registered for at least one online service to date (cumulative)                |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| Total GP List Size (from Patient Online)                | Number of patients registered at a general practice to date (cumulative)                                   |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| % GP population registered for Patient Online           | Proportion of GP registered population registered for GP Online Services to date (cumulative)              |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| NHS App Logins                                          | Number of NHS App logins in the specified reporting period                                                 |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| Users Booking Appointments                              | Number of App users booking GP appointments in the specified reporting period                              |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| Appointment Cancellation                                | Number of App users cancelling GP appointments in the specified reporting period                           |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| Users Requesting Prescriptions                          | Number of App users requesting prescriptions in the specified reporting period                             |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| User Accessing Medical Records                          | Number of App users accessing their medical records in the specified reporting period                      |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| Users Visiting NHS 111 Online                           | Number of App users visiting NHS 111 online from the NHS App in the specified reporting period             |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| Organ Donation Registrations                            | Number of App users who have registered to be an organ donor in the specified reporting period             |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| Organ Donation Updates                                  | Number of App users who have updated their Organ Donation Status in the specified reporting period         |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| Organ Donation Withdrawals                              | Number of App users who have withdrawn their organ donor registrations in the specified reporting period   |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| Users Visiting Health A-Z                               | Number of App users visiting the Health A-Z page in the specified reporting period                         |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| Users visiting National Data Opt-out                    | Number of App users visiting the National Data opt-out page in the specified reporting period              |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------+

Change log
=======================

NHS App Dashboard v1.4
----------------------

Data Caveats
---------------
#. GP Registered Patients data is not available for a small proportion of GP practices. Any metrics that use this measure as a denominator (e.g. Proportion of GP population registered for the NHS App) will have a slightly higher than expected rate.

#. The dashboard displays data only for GP practices that are currently active. Should a practice close, their historical data will no longer appear in the dashboard.

## Version 1.4 Change Log (29-11-2020)

1. Features Added:
------------------

#. **National Summary and Local App Usage:** Split national and local level data into separate sheets. Filters now work correctly on all graphs with no caveats
#. **Data Table page:** Allows users to easily filter data via Region, STP, CCG, CCG Code, Practice, Practice Code. 
#. **Data Dictionary page:** Will help users understand the meaning, description, lowest level of data, calculation, limitations and data source(s) for the different metrics in the NHS App Analytics Dashboard
#. **Information icons:** Allow the user to understand the purpose behind each page 

2. User Interface Changes:
--------------------------

#. UI fixes on National Summary Dashboard charts and titles to ensure accessibility, as well as adherence to NHSE&I dashboard formatting guidance
#. Clickable mailto link added to About page to allow users to email developers for support
#. Minor UI fixes to the About page
#. UI fixes on National Summary and App Usage pages
#. Consistent colour scheme applied to all charts on dashboard to improve user experience
#. Minor UI fixes on National Summary and App Usage page
#. Header formatting changed for all pages to improve user experience
#. Null Value(s) option deleted from filters
#. Filters now correspond with all charts

3. Features Removed: 
-------------------

To ensure the dashboard only includes metrics that are supported by the NHS App, the following charts have been removed:
#. Registrations by Non-Patient Online users running total
#. % of registrations by Non-Patient Online Users based on running totals
#. Active returning visitors


Version 1.3 Change Log (29-09-2020)
-----------------------------------

1. User Verification Process:
-----------------------------

To improve the App’s user registration journey and increase digital uptake, a 2-tier verification process has been implemented for new App users. The two tiers are as follows: 
#. Partially Verified (P5) users - Requiring Name, Email, D.O.B, Postcode and Mobile Number 
#. Fully Verified (P9) users - Requiring Photo ID and Photo/Video Identity Matching 
Partially verified (P5) users cannot access confidential information, and have limited access to App features until fully (P9) verified. 

2. Updated Registration Metric:
-------------------------------

The 'NHS App Registrations' metric has been updated to give a count of new App users who have obtained full (P9) verification. The dashboard has now been updated to account for this change and will resume weekly updates.

As a result of the new verification process and developments to the App over time, a new method for tracking user acquisition has been established. Previously, patients moving practice may have been assigned a new Linkage Key, and would therefore have been counted as a new app user. Data prior to May-2020 has been updated to reflect the new tracking method made possible by the new verification system, which avoids the risk of duplication. This may result in a slightly lower registrations count at practice level prior to May-2020.
