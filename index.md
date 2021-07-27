---
layout: default
title: Home
nav_order: 1
---

# Roadmap to the demo

- [x] Create demo repository
- [x] Render markdown documents using a Jekyll theme
- [x] Figure out search function
- [ ] ~~Include a table of contents~~ (side bar nav will suffice with search)
- [ ] Demonstrate the edit cycle
- [ ] Add semantic versioning and document the triggers (semantic-release package github CI integration)
- [ ] Create a pdf render of the documents (potentially will require separate code)
- [ ] Document the 'student' facing features in About 
- [ ] Document the contribution guidelines in readme.md

## PDF generation 
Currently it looks like the best option will be to use [this custom python code](https://github.com/catmorbid/markdown-book) but adapting it so that it orders the book using meta data instead of a number at the end of the file names... 

Right now, I think [this front matter parser](https://github.com/eyeseast/python-frontmatter) would be easy to drop in - albeit a little more costly in terms of run time. 

Once the document can be generated programmatically, all that remains is to develop the CI/CD pipeline, possibly using GitHub Actions to "build" the pdfs whenever a push is made to main branch
 
It would be tidy if we could find somewhere to include the version number in the pdf and the webpage. 

Overall - this seems possible!
