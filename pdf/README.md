## PDF utitlies

### `pdfcut`
* Remove a range of pages from pdf files

### How to create an automator for MacOS?

![Automator, create workflow](pdfCut_automator.png)

_Note_: This can be imported: ![Workflow location](pdfCut.workflow/Contents)


#### Improvements:

* Create a `symlink` of the executable:
```
ln -s ~/scripts/pdfcut ~/bin/pdfcut

# "~/bin" is the place where you can place your(user-created) binaries
```
* Add this location to the `PATH`
```
PATH=$PATH:~/bin
```

