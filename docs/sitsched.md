# SIT Scheduler API Docs

## Navigation
- Pages
  - [Home](home.md)
  - [SIT Scheduler API Documentation](sitsched.md)
  - [Course Signup System API Documentation](signup.md)
- SIT Scheduler API Docs
	- [Navigation](#navigation)
	- [Intro / Lay of the land](#intro-lay-of-the-land)
	- [Available Term Codes](#available-term-codes)
		- [Example Response](#example-response)
	- [Per-Term Section Info](#per-term-section-info)
		- [Example Response](#example-response)

## Intro / Lay of the land
The main site that [SITScheduler](http://sitscheduler.com/) seems to be using for information is
[https://stevens-scheduler.cfapps.io/](https://stevens-scheduler.cfapps.io/), which seems to have
its most get request endpoints located at [[https://stevens-scheduler.cfapps.io/](https://stevens-scheduler.cfapps.io/p/)].

| Request Type | Request URL | Response Description |
|--------------|-------------|----------------------|
| N/A | https://stevens-scheduler.cfapps.io/ | Root URL |
| Get | https://stevens-scheduler.cfapps.io/p/terms | Available Terms |
| Get | https://stevens-scheduler.cfapps.io/p/`{term code}` | Class Information for all classes in a given Term, where `{term code}` is a valid term code, like `2019F`. |

## Available Term Codes
To get a list of valid term codes, do a GET request with request URL `https://stevens-scheduler.cfapps.io/p/terms`. It will give you a list of strings, all of which are valid term codes.

### Example Response
Request cURL: `curl 'https://stevens-scheduler.cfapps.io/p/terms' -H 'Accept: application/json, text/plain, */*' -H 'Referer: http://sitscheduler.com/' -H 'Origin: http://sitscheduler.com' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36' -H 'DNT: 1' --compressed`

Request Response:
```
["2019S","2018F","2018B","2018A","2018S","2017F","2017B","2017A", (...),"2006W","2005F","2005B","2005A","2005S","2005W","2004F"]
```

## Per-Term Section Info

To get information on the courses, [SITScheduler](http://sitscheduler.com/) uses
a get request to URL `https://stevens-scheduler.cfapps.io/p/{SEM}`, where `{SEM}`
is the semester code, like `2019F`, or `2018S`.

Note: It has not yet been confirmed how SITScheduler retrieves coreq / prereq info. 
It may have to do with the stevens.edu cookie it sets, maybe it just grabs it from previous
mystevens logins.

### Example Response
Request cURL: `curl 'https://stevens-scheduler.cfapps.io/p/2019S' -H 'Accept: application/json, text/plain, */*' -H 'Referer: http://sitscheduler.com/' -H 'Origin: http://sitscheduler.com' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36' -H 'DNT: 1' --compressed`

Request Response:
```
[
  {
    callNumber: "10598"
    coreqs: ""
    credits: 1
    currentEnrollment: "11"
    daysTimeLocation:
      [{
        building: "BC"
        day: "F"
        endTime: "10:50:00Z"
        room: "320"
        site: "Castle Point"
        startTime: "9:00:00Z"
        instructor: "Nastasi J"
        maxEnrollment: "20"
        prereqs: ""
        section: "E 120A"
        status: "O"
        title: "Engineering Graphics"
      }, {...}, ...]
  }
],
[...],
[...],
...
```
<!-- TODO: format all of this better for later -->
