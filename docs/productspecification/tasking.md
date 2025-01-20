# 3. Tasking

## 3.1 Standard and Custom Orders

ICEYE groups orders into two different groups, Standard Orders and Custom Orders.


### 3.1.1 Standard Orders

**Standard Orders** are orders that

1. leverage only tasking options described in this Section [3](#3-tasking) (other than those explicitly designated as “custom”), without customizations, and

2. only order data products listed in Section [5](dataproducts.md#5-data-products-14) (other than those described in Section [5.5](dataproducts.md#55-on-demand-only-data-products) and/or explicitly designated as “custom” or  “on-demand (only)”) with the imaging modes listed in Section [2](imagingmodes.md#2-iamaspaceimaging-modes-5), without customizations.

The intent of this Product Specification is to thoroughly describe any product that may be ordered as a Standard Order.


### 3.1.2 Custom Orders

All orders that do not meet the definition of Standard Orders, are designated as **Custom Orders**.

ICEYE can support non-standard tasking and product requirements. Custom order requirements will be governed by specific contract terms agreed separately. Please contact ICEYE to discuss requirements for custom orders. ICEYE customer service can be reached via [the Contact pages at ICEYE website](https://www.iceye.com/contact/).


## 3.2 How to Place a Tasking Order

**New customers** should complete [the Contact Form for SAR Data Customers](https://www.iceye.com/contact/sar-data) on the [ICEYE website](https://www.iceye.com/) to start onboarding as an ICEYE customer. The ICEYE Customer Operations and Satellite Planning (**COSP**) team will provide the new customers with the **Order Form** and ordering instructions and help them set up **Secure File Transfer Protocol (SFTP) accounts** for data transfer as part of the onboarding process. After the account set up and onboarding process is complete, customers should follow the below instructions for existing customers on how to place tasking orders.

**Existing customers** can place tasking orders by completing the Order Form that they were provided with during customer onboarding. Customers can request a new order form from the COSP team using the information they were provided with during account set up. All customer contact information and all the required tasking options must be specified in the Order Form. All on-demand or custom products, options, requirements and/or other expectations must also be clearly specified in the Order Form. The completed form must then be submitted to the **ICEYE COSP email address** received during account set up along with any optional area of interest (AOI) files as email attachments.


## 3.3 Tasking Order Types

ICEYE accepts two types of tasking orders as summarized in Table [3-1](#table-3-1-a-summary-of-the-benefits-and-trade-offs-of-the-two-tasking-order-types) and further described in the following subsections.


##### _Table 3-1: A summary of the benefits and trade-offs of the two Tasking Order Types_

| Tasking Order Type | Benefits                                                          | Trade-offs                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------ | ----------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Constellation      | Provides highest speed and reliability                            | Customer has to specify acquisition time windows and optionally repeat cycles                                                                                                                                                                                                                                                                                                                                                                                                      |
| Single-Satellite   | Supports the widest selection of tasking requirements and options | Customer has to specify tasking requirements in detail and then review and approve an exact acquisition plan;Each task relies on a single satellite for its execution, thus is inherently less reliable than tasks that can be executed by any satellite in the constellation. Additionally, single-satellite orders placed  more than 14 days before the desired acquisition are more susceptible to replanning because of long term satellite orbit predictability limitations.  |


#####

### 3.3.1 Constellation Tasking Orders

**Constellation Tasking Orders** are orders that leverage the capacity of the entire ICEYE satellite constellation. This yields a significant advantage as the ICEYE planning system can continuously optimize the usage of the satellites in the constellation and automatically react to unexpected situations like technical anomalies, changes in satellite orbits and new satellites joining the fleet such as to ensure that all accepted tasking orders are successfully fulfilled.

Upon placing a constellation tasking order, the customer can specify a list of timing requirements that define one or more **acquisition time windows** and optionally also **repeat cycles** (periodicity) in which the desired images should be acquired. Upon receipt, the order is ingested into the ICEYE planning system which will determine if the order can be confirmed within the requested area of interest (AOI), time windows and other specifications. The customer will then be notified via email whether the order has been accepted or not. If the order is accepted, the images will be scheduled for acquisition by any satellite in the ICEYE constellation. No further confirmation by the customer is necessary. 


### 3.3.2 Single-Satellite Tasking Orders

**Single-Satellite Tasking Orders** are orders that offer customers a higher level of control in terms of tasking requirements. Many options that are not available as part of constellation tasking orders can be requested as part of a single-satellite tasking order.

Upon placing a single-satellite tasking order, our tasking experts will study the feasibility of the request and will quote an **acquisition plan** for approval. The acquisition plan will include a list of **acquisition opportunities** including the exact acquisition time, acquisition geometry and coverage of the specified AOI. From the plan, the customer can select their desired exact acquisition opportunities.

While this gives a higher degree of control, single-satellite tasking orders have the disadvantage of not leveraging the entire ICEYE constellation: Each ordered acquisition relies on only one satellite, therefore being more exposed to possible technical anomalies or changes in satellite orbits. Please note that ICEYE can currently only accept Single-Satellite Tasking as standard orders up to 14 days in advance of the desired acquisition date. This is because the reliability of predicted orbits for specific satellites decreases considerably after 14 days. For orders with desired acquisition date more than 14 days in the future, Constellation Tasking Orders (section [3.3.1](#331-constellation-tasking-orders)) are strongly recommended. If Single-Satellite Tasking is nevertheless desired, it will be considered a custom order (section [3.1.2](#312-custom-orders)).


## 3.4 Tasking Priority Options

ICEYE's task prioritization is based on the two standard priority options described in Table [3-2](#table-3-2-a-summary-of-the-two-tasking-priority-options) and the subsections below. Table [3-2](#table-3-2-a-summary-of-the-two-tasking-priority-options) describes the purpose, commitment level, notice time requirements and statistical reliability of both priority options. Note that all priority options are available for all imaging modes.


##### _Table 3-2: A summary of the two Tasking Priority Options_

| Tasking Priority Option |                             Purpose                             |                                        ICEYE commits to acquire task                                       | Min time before collection to choose pass | Min time before collection to choose target | Statistical Reliability  |
| ----------------------- | :-------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------: | :---------------------------------------: | :-----------------------------------------: | :----------------------: |
| Commercial              |                   Commercial reliable SAR data                  |                    Yes - ICEYE commits to acquire task within the specified constraints                    |                    12 h                   |                     12 h                    |           >90%           |
| Background              | Price sensitive applications. Collect only with spare capacity. | No - ICEYE makes no hard commitment to acquire.  Images tasked at commercial priority may take precedence. |                    24 h                   |                     24 h                    |     varies by region     |


### 3.4.1 Commercial Tasking Priority

Tasks at **Commercial Tasking Priority** are prioritized as regular commercial acquisition tasks. Satellite constellation capacity for image acquisition is allocated on a first-come-first-served basis (FIFO). Tasks placed at commercial priority have a statistical likelihood of at least 90% of being acquired and delivered successfully.


### 3.4.2 Background Tasking Priority

Tasks at **Background Tasking Priority** are executed at a lower priority than Commercial Tasking Priority. Consequently, such tasks may be displaced by higher priority tasks, or may not be acquired within the requested time window. Background tasking offers excellent value to customers that do not have precise timing constraints or who can accept flexibility in task fulfillment.

It is not possible for a user to alter the tasking priority after ICEYE has confirmed a task. To change the priority of an already submitted task, the user must first cancel the task (possibly subject to cancellation penalties, see Section [3.6](#36-order-cancellation)) and then resubmit the tasking request. Note that in case of Commercial priority, canceling and re-submitting an order may result in the loss of priority in the FIFO schema.


## 3.5 Catalog Withhold

ICEYE provides two options to address customer privacy needs for completed collections: **Public Catalog** and **Private Catalog**. These options are summarized in Table [3-3](#table-3-3-a-summary-of-the-benefits-and-trade-offs-relating-to-catalog-withhold-options) and further described below.

The catalog designation for an image is immutable and thus after order submission, a Public Catalog image cannot be changed to Private Catalog, and vice versa.


##### _Table 3-3: A summary of the benefits and trade-offs relating to Catalog Withhold options_

| Option          | Description                                                                                                                                                             | Trade-offs                                                                                                                                    |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Public Catalog  | Acquired  images are listed in ICEYE's public archive catalog 14 days after acquisition time. The images are available to other ICEYE customers to purchase from ICEYE. | Better cost economy.Images are available to other ICEYE customers for purchase                                                                |
| Private Catalog | Acquired  images are permanently withheld from ICEYE's public archive catalog. They are not available for other  ICEYE customer to purchase                             | Initial acquisition cost is higher.  Images are not available for purchase, nor is the existence of images revealed to other ICEYE customers. |


#####

### 3.5.1 Public Catalog Option

All successfully completed collections with the **Public Catalog Option** will be listed in ICEYE's public historical collections archive catalog 14 days after being acquired and made available to all ICEYE customers to purchase.


### 3.5.2 Private Catalog Option

With the **Private Catalog Option** completed collections will only be listed in the private catalog assigned to the customer. Consequently, ICEYE accepts to withhold from adding the collected data into ICEYE's public historical collections archive catalog thereby preventing other ICEYE customers from purchasing them, or even discovering that they were ever collected.

This option is also known as (Public) **Catalog Withhold** and it comes with a price premium but it is nonetheless favored by customers collecting SAR data over sensitive areas of interest.


## 3.6 Order Cancellation

ICEYE understands that customers may have cause to cancel an order before collection. ICEYE offers a **cancellation policy** which balances flexibility for customers with the need to operationally finalize the collection deck as the time of collection approaches. The policy depends on the Tasking Order Type as follows:

**Single-Satellite Tasking Orders** may be canceled within twenty four (24) hours after order confirmation at no cost, as long as the order is submitted at least three days (72 hours) before the proposed data collection time.

**Constellation Tasking Orders** can be canceled free of charge up to 72 hours prior to the start of the acquisition time window. After that there is a cancellation charge of 100% of the order value, or less as described in Table [3-4](#table-3-4-cancellation-charges-and-cancellation-policy-conditions-for-constellation-tasking-orders) below.


##### _Table 3-4: Cancellation charges and cancellation policy conditions for Constellation Tasking Orders_

|                     Cancellation Request Time                    |                       Additional Condition                       |                        Cancellation Charge                       |
| :--------------------------------------------------------------: | :--------------------------------------------------------------: | :--------------------------------------------------------------: |
| More than 72 h prior to the start of the acquisition time window |                                N/A                               |                          Free of charge                          |
|    72 - 48 h prior to the start of the acquisition time window   |                                N/A                               |                  10% of the order value         |
|    48 - 24 h prior to the start of the acquisition time window   |                                N/A                               |  20% of the order value |
| Less than 24 h prior to the start of the acquisition time window | Order submitted >24h before the start of the acquisition time window |  100% of the order value (i.e. no refund) |

In other cases orders cannot be canceled and the order must be fully paid and no refund can be expected. The order must be fully paid and no refund can be expected despite the cancellation when the cancellation charge is 100% as per above.


### 3.6.1 Return Policy

In the event that a Customer’s purchase is non-compliant with the Data Product Specification, the Customer must contact ICEYE Customer Operations and Satellite Planning (COSP) team (via the email address received during customer onboarding) providing details of the non-compliance within 14 days of receiving their order.

As customer satisfaction is a priority for us at ICEYE, we will work quickly to ensure our customers receive compliant images.


## 3.7 Order Fulfillment

An order is fulfilled when the data requested in the order is collected, quality controlled and ready to be downloaded at the agreed delivery endpoint. The exact time when this data becomes available determines the fulfillment of the delivery service levels described in Section [3.7.3](#373-delivery-time-service-level). Additionally, some customers will receive a notification via email every time a new acquisition has passed ICEYE's detailed quality control process and the final version of the data is ready for download. This email notification is sent for convenience only and is not to be considered towards the fulfillment of a delivery service level. 

More information about deliverables, delivery endpoints and the quality control process is available in the subsections below.


### 3.7.1 Deliverables

All successfully fulfilled orders result in a **Deliverables Package** which consists of SAR data product files and their accompanying metadata. More information about the actual data product deliverables, their metadata and file naming is available in Section [5](dataproducts.md#5-data-products-15).


### 3.7.2 Delivery Endpoints

ICEYE provides a **Standard Delivery Endpoint** that is intended to meet most customer requirements. However, **Custom Delivery Endpoints** can also be considered as part of a custom order. Table [3-5](#table-3-5-descriptions-of-iceye-delivery-endpoint-options) presents a description of these two delivery endpoint options.


##### _Table 3-5: Descriptions of ICEYE Delivery Endpoint Options_

| Delivery Endpoint Option | Description                                                                                                                                                                                                                                                             |
| -----------------------: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                 Standard | - Processed data files are delivered to the customer’s account in the ICEYE SFTP server from which the customer can access the data using an SFTP client.<br>- SFTP authentication is based on SSH keys only; authentication based on usernames and passwords is not supported. |
|                   Custom | - Delivery to a customer’s third party cloud storage (e.g. S3 bucket) or similar is not standard and requires a custom order.<br>- Please contact ICEYE to discuss alternative delivery endpoint needs.                                                                         |

### 3.7.3 Delivery Time Service Level

A central pillar of the ICEYE tasking product specification is the ICEYE commitment to deliver imagery within a predetermined time following collection. The realized delivery time is calculated as the difference of a) the timestamp of when the data products have been delivered to the agreed delivery endpoint, and b) the timestamp of original SAR data collection in the satellite as stored also in the image metadata.

ICEYE delivery times are fulfilled for over 90 % of the applicable deliveries. This performance statistic applies to all applicable customer deliveries, and is intended to hold regardless of AOI or imaging mode. The statistic is evaluated based on all applicable collections from the previous calendar year and the Data Product Specification is updated annually based on the performance of the previous calendar year. Because this is a global statistic applied to all customers, no single collection is guaranteed to deliver the expected timeline:  a customer’s results may vary even while the Data Product Specification is honored.

For all Standard Orders, ICEYE currently offers two **Delivery Time Options** or delivery tiers: an 8 h delivery tier, and a 3 h delivery tier for applications requiring rapid delivery. These delivery time options and how they map with the offered data product formats are further described in the below subsections, and summarized in Table [3-6](#table-3-6-summary-of-delivery-time-service-levels). Note that the delivery time service levels described in this subsection do not apply to Custom Orders. The delivery time service level must be separately agreed for custom orders and by default are delivered on the basis of best effort.


##### _Table 3-6: Summary of Delivery Time Service Levels_

| Delivery Time Option | Description                                                         | Supported Data Products                                                                     |
| -------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| 8 h                  | Data files are delivered in 8 hours or less after acquisition time  | GRD, Legacy GRD, CSI, VID, Quicklook, SLC, Legacy SLC(See Section [5](dataproducts.md#5-data-products)) |
| 3 h                  | Data files are delivered in 3 hours or less after acquisition time  |                                                                                             |


#####

ICEYE intends to expand its specified delivery timelines beyond these two tiers. ICEYE also accommodates nonstandard delivery times of otherwise standard orders on a custom order basis. Customers are advised to explore nonstandard delivery time options and the delivery time options for custom orders potentially involving on-demand products (such as the CPHD, SICD + SIDD (NITF), and Orthorectified imagery data products; See Section [5](#5-data-products-17)) or nonstandard products and/or imaging modes together with the ICEYE customer service team, preferably via the email address the customer received during ICEYE’s customer onboarding.


#### _3.7.3.1 8-hour Delivery Time_

With the **8-hour Delivery Time** option automatic delivery will be completed in 8 hours or less of the data being acquired. The GRD, Legacy GRD, CSI, VID, Quicklook, SLC, and Legacy SLC data products are supported. See Section [5](dataproducts.md#5-data-products) for more information on the different data products.


#### _3.7.3.2 3-hour Delivery Time_

With the **3-hour Delivery Time** option automatic delivery will be completed within 3 hours of the data being acquired. This option is intended for applications requiring rapid delivery. The same data products are supported as with the 8-hour Delivery Time option.


### 3.7.4 Quality Control

ICEYE performs an automated and rapid **quality control** in which we ensure the image meets basic image quality attributes. Because this quality control is automated, it does not detect all image defects. Customers with concerns about a defective image are invited to contact ICEYE COSP organization  in accordance with Section [3.6.1](#361-return-policy) (Return Policy) above for consultation and potential remedy.

