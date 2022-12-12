# About 📜
### *A **simple** item manager for [Frozen Freebies](https://frozensoftware.com/), an Amazon auto freebie bot.*
### Download the app [here!](https://github.com/makors/inventory-manager/releases/download/cool/app.zip)
#### This manager is **USER RUN**, meaning that you have to run the binary/python file on your server or home PC.

#### **Now, to the actual setup.**

# Google Cloud Setup ☁️
*Getting started requires you to be logged into a [Google Account](https://accounts.google.com).*

*Step 1, Signing into Google Cloud:* **You NEED to make a [Google Cloud Project](https://console.cloud.google.com/projectcreate) to continue, you can create this by clicking the [link](https://console.cloud.google.com/projectcreate) and accepting Google Cloud TOS.**

*Step 2, Creating Project:* **Create the Google Cloud Project, by adding in a name like "makorsisthebest12331" (example below)**  
![Example](https://i.ibb.co/SvD223Z/image.png)

*Step 3, Adding API(s):* **Close the last window, as it is not needed anymore, and enable the Google Sheets API [here](https://console.cloud.google.com/flows/enableapi?apiid=sheets.googleapis.com). Confirm the project is the same as the name you selected above, and if not, select your project at the top of the page. You are then going to want to click "Next", which should bring you to a new section and all you have to do from that point is click enable! Lastly for this section, you have to enable the [Google Drive API](https://console.cloud.google.com/apis/library/drive.googleapis.com), this can be done by clicking the "Enable" button, and that is pretty much it for adding the API(s)!**

*Step 4, Getting Credentials:* **The final part of the Google Cloud setup is getting the credentials, which are needed to create and edit Google Sheets documents. These credentials can be accessed by going [here](https://console.cloud.google.com/apis/credentials) and clicking "+ Create Credentials", which should pop-up a menu, and on this menu, you want to select "Service account" (example below)**  
![Example](https://i.ibb.co/5WrshR0/image.png)  
**After doing this, you should be presented with a screen to create a "Service account", which is required for this piece of software. To create a service account, enter a nickname for it like "makors", and an ID for it like "makors1234" (example below). After you enter those details, skip the optional steps and click "Done" at the bottom of the page section.**  
![Example](https://i.ibb.co/Y2sqC0h/image.png)  
**The last step of this process is to get the credentials in a JSON format, which is used by the Inventory Manager software. After clicking done, you should be brought to the credtials screen, and if not click [here](https://console.cloud.google.com/apis/credentials) to go there. Under "Service accounts", you want to find the one you just created and click the edit icon under the actions tab (example below).**  
![Example](https://i.ibb.co/cDcMkpQ/image.png)  
**Then at the top of the webpage, you want to click over to the "KEYS" tab. You then want to click "Add key", and then click "Create new key". Select the JSON format and click "Create", then a file download should start. You want to rename the file to "credentials.json" and save it in the folder called "tokens" where you initally download the Inventory Manager software. Now that that is done with, lets get onto Software setup.**  
![Example](https://i.ibb.co/6DQFDvq/image.png)

# Software Setup 💾
### From here, getting the software setup is made to be easy!

**The file that is being referred to is the `the.config` file, which is where you edit your basic information. Here is what a basic config file would look like:**
```
[USER]
email = test@example.com

[SHEET]
title = Inventory Manager
```
**In this software, email refers to the email your spreadsheet will be shared with, which is *VERY IMPORTANT*, so you can see your file! 🎉 The variable `title` refers to the title of the Google Sheet the bot will be creating and updating.**

### Webhook Setup (super ez 🔥)
#### To get this set up, Frozen Freebies needs to know where to send the additional success webhooks, which you can do by following the instructions below.
**First, you are going to want to click the "Edit all" button at the top of the Frozen Freebies software. Then, you are going to want to click the "Advanced settings" option (example below). Next you are going to want to paste `http://localhost:8080/webhook` into the "Additional Success Webhook" field.**  
![Example](https://i.ibb.co/gVmDB4y/image.png)  

# Final Setup / Notes 📄
### To run the main bot, open the `bot.exe` file in the directory where you downloaded this, which has to be run in the background.
#### *The way to access the  Spreadsheet📃 is by clicking the link the bot will print out when it runs, or going to your [Google Drive Shared](https://drive.google.com/drive/u/0/shared-with-me) and finding the spreadsheet manually. API may also take a few minutes to go through Google servers.*
### If you also would like to delete ALL of your spreadsheets, you can run the `delete_all.exe` file, which will prompt you to confirm by typing some text in.
### Credit to `aravind#0001` for the general idea, this was made to add some extra features to it 🎉