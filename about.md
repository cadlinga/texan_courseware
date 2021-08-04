---
layout: default
title: About
nav_order: 9999
---

# Single Source Documentation

The courseware is built using a single source of information, a folder of `markdown` files. Markdown is a simple templating language which is easy to understand, clutter free and importantly, easy to edit. 

The markdown can then be parsed using software into the correct format for a website and the correct format for a pdf. 

This means there is a `single source of truth` and reduces the ability for information to become disjointed and smeared across various sources.

## Online Documents 

The current web version of the courseware is generated using a static website generator and is publicly hosted (for free) using GitHub pages, [here](https://cadlinga.github.io/texan_courseware/). 

The content has a 'breadcrumbed' navigation structure and all of the content is fully searchable. 

### Search Function

The search will automatically index all of the markdown files when the website is published and the depth is currently set to sub headinng 

![](./../assets/images/search.gif "System Status")

## PDF Documents 

### Document Structure


* * * 


# Semantic Versioning 

# Releases

## Release Assets

## Persistent Links

# Readback (getting historic versions)

## Release Comparison (differences)


* * * 


# Edit Cycle and Git

## User Types and Permissions
Owner - OC 72(F)Sqn, Ascent Chief Pilot, OC C Flight, Lead QI

Maintainer - C Flight QFIs, Flight Commanders

Member - All other members of 72(F)Sqn

![](./../assets/images/comitting_to_main_is_blocked.png "Comitting to main to blocked")

## Creating A Feature Branch 
A "Branch" is a feature that allows users to make a copy of the Master document whilst editing an 'offline' version, anyone can create a Branch and submit changes via a "Pull Request" to be reviewed by an owner/maintainer.

![](./../assets/images/Branch_Demo.png "Branch Demo")
## Merging A Feature Branch (Pull Request)
If a repository owner/maintainer approves the "Pull Request" from the editor, the Master Document and Branch Document will be merged.
## Automatic Quality Control 

## Raising An Issue

Any member of the repository can raise an issue and submit proposed changes, the issue sits will be reviewed by the owners/maintainers and dealt with accordingly.

An example of this would be if a 310 student finds an incorrect limitation in the Spinning courseware e.g. "at 100kts select and maintain Full Pro Spin controls", they would create a Branch, change the limitation (to 90kts) and commit changes, giving an explaination of the change they deem necessary, then submit a pull request (a request to merge their branch into Master document).
The request would come through to an owner/maintainer (OC C Flt), who recognises the limitation is 90kts, they could accept the change and merge the branch, triggering an automatic document change and notification email. 
## Oversight and Audit
Due to the nature of the branches and pull requests, no changes can be made and implemented by anyone other than owners or maintainers. All changes that are requested are presented in their entirety and compared with previous versions (Students could not slip rogue words or phrases into courseware and it be approved without anybody noticing).

* * * 


# Email Notifications 
When a Major or Minor change is made to the document sets, a notification email (similar to below) will be sent to all subscribers of the documents along with the most current versions of the documents.
![](./../assets/images/Email_Demo.png "Email Demo")
