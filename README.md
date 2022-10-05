# **SampleGrabber**
SampleGrabber is a small and easy to use tool to download audio files from the SampleFocus website.

## **Installation**
1. Download and install [Python](https://www.python.org/) (the program that runs the code)
    - [Here](https://www.youtube.com/watch?v=ZRbirvsDQ-I) is a video on how to install Python

2. Thats it! You can now open the application by double clicking on the "SampleGrabber.pyw" file

## **How to use**
### Setup
1. Add the Chrome extension [Javascript & Css auto injection](https://chrome.google.com/webstore/detail/javascript-css-auto-injec/oakjdafonfdgbgbcofjpaecngfimohno) and then open it

2. Add a new rule by clicking on the plus button and give it a name of your choise (does not matter how you call it)

3. Paste the url "https://samplefocus.com/samples/" into the url field, on the left select the option "URL start with" (if not already selected) and on the right select the option "On Page Loaded"

4. In the JS code field, paste in [this](https://pastebin.com/VKZRpLu6) script

![Extension](https://i.imgur.com/t6jZW3E.png "Javascript & Css auto injection")

### Pull process
1. Open the SampleGrabber.pyw file

2. Open your desired sample on the SampleFocus website

3. Refresh the website and an alert will pop up with an url that you have to copy

4. Go on the SampleGrabber application and paste in the previously copied url into the url field and the name of the sample into the name field

5. Press on the "pull" button at the button to download the sample

6. Done! A new audio file that contains your sample should now appear in the same directory as the SampleGrabber.pyw file

![SampleGrabber](https://i.imgur.com/JMCgpnV.png "SampleGrabber application")
