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

The search will automatically index all of the markdown files when the website is published and the depth is currently set to sub heading, which means that the content within each page can be searched. 

![](./../assets/images/search.gif "System Status")

For example, if you search the word "circuit" (above on large screens, or within the burger bar on mobile), you will see the granularity of the search. 

## PDF Documents 

Whenever a release is generated (explained properly later), a script automatically compiles the markdown into pdf files, currently two different pdf documents 'groundschool' and 'flying', any amount of documents can be generated and the system can be very easily expanded. 

### Document Structure

The pdf is generated using a typesetting tool called LaTeX, as a result, the pdf is 'properly formatted' and the document has a structure of chapters, sections and subsections. All of these will be parsed by a good pdf reader and become a navigatable tree alongside the document. Additionally, there is a table of contents with clickable links to all of the sections. 

![](./../assets/images/document_structure.png "Document structure and contents page")


* * * 


# Semantic Versioning 

This courseware will use semantic versioning to help make it clear to the users if they need to update their document set or not. The format of a semantic version is three digits, separated with dots `.`, sometimes prefixed with the letter `v`. This is in industry standard for versioning. 

For example, `v0.2.32`. 

The first digit represents the `major` version, if this digit is incremented, there have been breaking changes to the document. An example of such a breaking change could be a technique completely changing, or a limitation changing. If your document set is not at the current major version, some of the information in it is **incorrect** and **incomplete**.

The second digit represents the `minor` version, if this digit is incremented, there has been content added to the document but in a reverse compatible way. An example of such a change could be adding a new section to the flying manual, like a night flying section. If your document is not at the current minor version, the information in your document is **correct** but **incomplete**. 

The third digit represents the `patch` of the document. If this digit is incremented, there has been a patch update applied and none of the information has qualitatively changed. An example of such a change could be correcting spelling or punctuation errors or rewording a sentence for clarity. If your document is not at the current patch, the information in your document is **correct** and **complete** but perhaps not as clear or tidy as the most recent version. 

# Releases
 
The courseware will have a release "*everytime** the patch digit of the semantic version increments. 

A release is like a snapshot of the source documents. The releases for the courseware will simply be named after the semantic version which triggered the release. 

Everytime a release is created, the source code of the courseware is compressed into a zip file and stored with the release. 

## Release Assets

As well as a compressed version of the source code, we are free to associate any additional files to a given release, for the courseware we have chosen to associate the pdfs. This means that by viewing the releases in the GitHub repository, you can see the pdfs which were generated for every single version. 

## Persistent Links

Each of the files associated with each release are available to download with a unique URL which includes the release version and the filename. Helpfully, there is a consistent URL for the files associated with the `latest` release. That means there is a link which, whenever it is clicked, will download the most recently released pdf versions of the courseware and the link **never** changes. 

## Release Comparison (differences)

It is also possible to compare any two releases and see the changes which were made to the source files. This could be particularly useful for someone who has noticed the semantic version has been updated and wants to know exactly what has changed. GitHub shows this exceptionally clearly, displaying, file by file, lines which have been removed and lines which have been added. 

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

## Creating A Feature Branch

### Explicitly Creating A Branch

### Creating A Branch At The Point Of Edit 

## Merging A Feature Branch (Pull Request)

## Raising An Issue

Any member of the repository can raise an issue and submit proposed changes, the issue sits will be reviewed by the owners/maintainers and dealt with accordingly.

An example of this would be if a 310 student finds an incorrect limitation in the Spinning courseware e.g. "at 100kts select and maintain Full Pro Spin controls", they would create a Branch, change the limitation (to 90kts) and commit changes, giving an explaination of the change they deem necessary, then submit a pull request (a request to merge their branch into Master document).
The request would come through to an owner/maintainer (OC C Flt), who recognises the limitation is 90kts, they could accept the change and merge the branch, triggering an automatic document change and notification email. 
## Oversight and Audit
Due to the nature of the branches and pull requests, no changes can be made and implemented by anyone other than owners or maintainers. All changes that are requested are presented in their entirety and compared with previous versions (Students could not slip rogue words or phrases into courseware and it be approved without anybody noticing).
### Viewing A Commit 

### Viewing Document History 

* * * 


# Email Notifications 
When a Major or Minor change is made to the document sets, a notification email (similar to below) will be sent to all subscribers of the documents along with the most current versions of the documents.
![](./../assets/images/Email_Demo.png "Email Demo")

* * *

# Automation 

## Quality Control 

## PDF Generation 

## GitHub Release

## Email Notification 

