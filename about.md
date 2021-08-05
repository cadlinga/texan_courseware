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
 
The courseware will have a release **everytime** the patch digit of the semantic version increments. 

A release is like a snapshot of the source documents. The releases for the courseware will simply be named after the semantic version which triggered the release.

![](./../assets/images/release.png "GitHub Release")

Everytime a release is created, the source code of the courseware is compressed into a zip file and stored with the release. 

## Release Assets

As well as a compressed version of the source code, we are free to associate any additional files to a given release, for the courseware we have chosen to associate the pdfs. This means that by viewing the releases in the GitHub repository, you can see the pdfs which were generated for every single version. 

## Persistent Links

Each of the files associated with each release are available to download with a unique URL which includes the release version and the filename. Helpfully, there is a consistent URL for the files associated with the `latest` release. That means there is a link which, whenever it is clicked, will download the most recently released pdf versions of the courseware and the link **never** changes. 

### [Latest Groundschool Manual](https://github.com/cadlinga/texan_courseware/releases/latest/download/groundschool.pdf)

### [Latest Flying Manual](https://github.com/cadlinga/texan_courseware/releases/latest/download/flying.pdf)


## Release Comparison (differences)

It is also possible to compare any two releases and see the changes which were made to the source files. This could be particularly useful for someone who has noticed the semantic version has been updated and wants to know exactly what has changed.

![](./../assets/images/release_comparison_1.png "Selecting versions to compare")

GitHub shows this exceptionally clearly, firstly showing a list of all of the commits taking one version to another. 

![](./../assets/images/release_comparison_2.png "List of commits between versions")

Every commit can be interrogated for more information, but the sum of all of their changes is then displayed for each file that has been changed. Anything highlighted in red has been removed, anything in green has been added. 

![](./../assets/images/release_comparison_3.png "Sum of changes for each file")

* * * 


# Edit Cycle and Git

The edit cycle using git uses branches and pull requests to allow multiple people to contribute to a set of documents in a collaberative way and makes merging all of the various changes from various contributors as simple as possible. 

![](./../assets/images/Branch_Demo.png "Branch Demo")

## User Types and Permissions

Owner - Single owner, admin permissions - held by Conner currently. 

Maintainer - Admin like permissions, responsible for approving pull requests (checking the content submitted) - possibly held by OC 72(F), OC C Flt, Chief Pilot etc. 

Member - All other people who need access to the courseware. They have read access to the 'Main' branch, can view releases, create a new branch or raise an issue. Nothing they can do without approval can compromise the documents. Comitting directly to Main is blocked (see below). 

![](./../assets/images/comitting_to_main_is_blocked.png "Comitting to main to blocked")

## Creating A Feature Branch 

A `Branch` is a feature that allows users to make a copy of the Main document whilst editing an 'offline' version.

Anyone can create a Branch and make as many edits as they like. It will never effect the main branch. 

### Explicitly Creating A Branch

A branch can be explicitly created using the branch drop down: 

![](./../assets/images/create-branch.png "Create a new branch")

### Creating A Branch At The Point Of Edit 

Alternatively, when editing a file, since main is restrcited, a branch can be created on the fly when editing a file. 

![](./../assets/images/comitting_to_main_is_blocked.png "Comitting to main to blocked")

When ready, they can submit changes and request that they are merged into the main branch.


### Automatic Quality Control 

There are several automations applied (explained later), but all commits made to any branch is submitted to an automatic quality check, and the owner of that branch is told whether or not their edits have passed the quality check. If they do not meet the standard, there is feedback provided to help the contributor get up to the required quality.

The green tick indicates that it has passed the quality check.

![](./../assets/images/quality-control.png "Quality control")

## Merging A Feature Branch (Pull Request)

When a feature branch is ready and the contributor would like to submit their work to be merged into main, they do so with a pull reuqest. This can be done explicitly in the pull request menu. 

![](./../assets/images/create-pull-request.png "Explicitly creating pull request")

Alternatively, when working on a branch that is not Main, GitHub will often prompt and suggest you can submit a pull request. 

![](./../assets/images/pull-request-prompt.png "GitHub prompt to create pull request")

If a repository owner/maintainer approves the pull request from the contributor, the edits are applied to the main branch.

When approving, the maintainer may provide feedback to the branch owner, asking them to make changes before finally accepting the changes and merging into main. 

## Raising An Issue

Any member of the repository can raise an issue which does not require them to suggest proposed changes. Once raised the issue is visible to everyone and anyone can suggest a solution. This could be as simple as commenting a solution, or creating a feature branch, fixing the problem and submitting a pull request, stating that the branch fixes the issue.

![](./../assets/images/issue.png "A raised issue")

An example of this would be if a 310 student finds an incorrect limitation in the Spinning courseware e.g. "at 100kts select and maintain Full Pro Spin controls", they simply raise the issue and it can be fixed by the community, or by the document maintainers. 

## Oversight and Audit

Due to the nature of the branches and pull requests, no changes can be made and implemented without being approved by one of the maintainers. All changes that are submitted and later approved are auditable in their entirety. Every line, in every file can be traced back to who wrote it and who approved it and when. This allows open contribution from everyone (QFIs, students, QIs etc) because due to the granularity, mischevious students or disgruntled staff could not slip rogue words or phrases into courseware without it being tracable to them and approved by a maintainer. 

### Viewing Document History 

You can select any document in the repository and view the history of the document, this will display a list of commits, as well as their authors. 

![](./../assets/images/view-history.png "Document History")

### Viewing A Commit 

Each of the commits can be inspected in further detail, where it will show which files were changed and exactly what changes were applied.

![](./../assets/images/view-commit.png "Commit Details")

* * * 


# Email Notifications 
When a Major or Minor change is made to the document sets, a notification email (similar to below) will be sent to all subscribers of the documents along with the most current versions of the documents.

![](./../assets/images/Email_Demo.png "Email Demo")

* * *

# Automation 

To keep the deployment process consistent and timely, the process has been as automated as possible. Everytime a branch is merged into 'Main' (the master document source code), a deployment script is run which assures the quality of the files, calculates the semantic version number, creates the pdf files, generates a release (attaching the pdfs to the release) and sends the notification email. 

![](./../assets/images/automation.png "Automatic Pipeline")

Any push to the Main branch has all of the automations applied, any push to any other branch (a feautre branch) only has the quality control applied. 

## Quality Control 

Currently, the quality control script checks for simple formatting of the markdown files, but this is very easily extended and could include things like spell check and syntax checking. 

## Calculate Semantic Version

The semantic version is automatically calculated. Every commit will 'bump' the patch number, but any commit which has `(MINOR)` in the commit message will bump the minor version and similarly, any commit with `(MAJOR)` will bump the major version. 

The maintainer who is responsible for accepting pull requests from feature branches will be responsible for labelling the merge as `(MAJOR)`, `(MINOR)` or leaving it as a patch. 

The automation then uses the commit message history to automatically generate the version number. 

## PDF Generation 

With the version number, the pdf files are then generated and the version number is inserted on the cover page to make it easy to determine which version you have.  

## GitHub Release

With a version number and pdf files to attach, the script then creates a new release, taking a snapshot of the source files and attaching the pdf files. This release now becomes the `latest` release and the persistent links described earlier will now point at the pdf files of this release. 

## Email Notification 

Finally, the email notification is automatically sent to the mailing list so that anyone who is subscribed to the document set is aware of the new release. 

# Future Developmens 

## Include EoTD

## Include Sortie Briefs

## Include Mass Briefs

## Include Phase Guides 

## Separate verisoning 

Potentially separate each document set out to have its own version number. This will prevent the flying manual being major incremeneted due to changes to the ground school manual.
