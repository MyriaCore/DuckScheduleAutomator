# Course Sign Up System API Docs

## Navigation
- [Home](home.md)
- [SIT Scheduler API Documentation](sitsched.md)
- [Course Signup System API Documentation](signup.md)

<!-- TODO: Find a less spammy way to include the site's files -->
<!-- TODO: Add a table of contents to this -->

## Intro

Get / Post Requests don't show up during site navigation, so it can be assumed that all the information is encoded in the website and the whole thing is somehow static, or that there's some weird js stuff going on. There's a pretty large ajax script, which will be posted in its respective section.

## Site Structure

In the sources tab of inspect element, there's a folder in `top/my.stevens.edu/default/modules/custom` that contains most of what seems to be the logic.

![site structure](https://i.imgur.com/6NIwcwd.png)

The files in `misc` seem to be related to site logic, and are documented in the [misc scripts section](). <!-- TODO: add section link -->
The folders / files in `modules` are all UI related css files. `profiles/openatrium` seems to have app/logic-related files too<sup>[[Citation Needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)]</sup>. Everything in `sites` is pretty much misc. UI / authentication stuff.

![folder structure](https://i.imgur.com/44p1All.png)

All of these folders have a cooresponding `{foldername}.js` file in them. `my_stevens_feedback` has a `feedback.css` file in it, however.

`stevens_mystevens_api_badge.js` and `stevens_mystevens_detect_network.js` both seem to be for user identification / verification, implying the over-arching site logic is elsewhere. The files in `stevens_mystevens_feedback` and `stevens_mystevens_flexslider_link` seem to be UI/UX related.

<!-- TODO: document the rest of the site structure -->


## HTML
There used to be a big code block here with the static HTML page, but I removed it when I realized how bad of an idea that was xP

## Misc Scripts

The following script is located under `top/my.stevens.edu/misc/`, and are titles `ajax.js`, `drupal.js`, and `progress.js` respectively.

### ajax.js
Maybe one day there'll be a nice happy way to put all of the stuff here securely. For now, however, I guess this'll have to stay blank.

### drupal.js
I really should be reading through the code I post here before I post it.

## progress.js
F
