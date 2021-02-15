# finder_mailtags
Scripts for setting MailTags to Finder tags

Dependencies

* [SmallCubed MailSuite](https://smallcubed.com)

* GNU Find. This can be installed with

	```brew install findutils```
	
* [Tag utility](https://github.com/jdberry/tag). This can be installed with

	```brew install tag```

The Applescripts can be slow to run and will cause any running Mail application to be unresponsive. 

The Python script is reasonably quick. I run it every 10 minutes so that it doesn't have to process a large backlog of files. 

This process was developed on macOS 10.13.6 (High Sierra). finder_mailtags.py was tested under Python 3.6.
