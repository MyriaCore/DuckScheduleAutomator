# SIT Scheduler API Docs

## Navigation
- Pages
    - [Home](home.md)
    - [SIT Scheduler API Documentation](sitsched.md)
    - [Stevens.edu Web Scheduler API Documentation](stevens-scheduler.md)
    - [Course Signup System API Documentation](signup.md)
- Sections
	- [Navigation](#navigation)
	- [Intro / Lay of the land](#intro--lay-of-the-land)
	- [Available Term Codes](#available-term-codes)
		- [Example Response](#example-response)
	- [Per-Term Section Info](#per-term-section-info)
		- [Example Response](#example-response)

## Intro / Lay of the land
The main site that [SITScheduler](http://sitscheduler.com/) seems to be using for information is
[https://stevens-scheduler.cfapps.io/](https://stevens-scheduler.cfapps.io/), which seems to have
its most get request endpoints located at [https://stevens-scheduler.cfapps.io](https://stevens-scheduler.cfapps.io/p/).

| Request Type | Request URL | Response Description |
|--------------|-------------|----------------------|
| N/A | https://stevens-scheduler.cfapps.io/ | Root URL |
| Get | https://stevens-scheduler.cfapps.io/p/terms | Available Terms |
| Get | https://stevens-scheduler.cfapps.io/p/`{term code}` | Class Information for all classes in a given Term, where `{term code}` is a valid term code, like `2019F`. |

## Available Term Codes
To get a list of valid term codes, do a GET request with request URL `https://stevens-scheduler.cfapps.io/p/terms`. It will give you a list of strings, all of which are valid term codes.

### Example Response
Request cURL:
```
curl 'https://stevens-scheduler.cfapps.io/p/terms' -H 'Accept: application/json, text/plain, */*' -H 'Referer: http://sitscheduler.com/' -H 'Origin: http://sitscheduler.com' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36' -H 'DNT: 1' --compressed`
```

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
Request cURL:

```
curl 'https://stevens-scheduler.cfapps.io/p/2019S' -H 'Accept: application/json, text/plain, */*' -H 'Referer: http://sitscheduler.com/' -H 'Origin: http://sitscheduler.com' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36' -H 'DNT: 1' --compressed
```

Request Response:
```
[
  {
    callNumber: "10600"
    coreqs: ""
    credits: 2
    currentEnrollment: "24"
    daysTimeLocation:
    {
      building: "E"
      day: "R"
      endTime: "11:50:00Z"
      room: "011"
      site: "Castle Point"
      startTime: "9:00:00Z"
    }
    instructor: "Calhoun S"
    maxEnrollment: "24"
    prereqs: "Prerequisite: E   121"
    section: "E 122A"
    status: "C"
    title: "Engineering Design II"
  },
  {...},
  {...},
  ...]
```
### Prerequisites and Corequisites
Pre and Co requisites are sorta weird in this API. They seem to be tailor made for displaying on sitscheduler, as when they 
become too large, they have `<br>` tags, like they were a rich text field. It is unknown whether or not `or`'s after a `<br>` 
tag are meant to be read as if the `<br>` wasn't there, or if it's the start of a new set of Pre-requisites.

It is very likely that a deep text search will have to be employed to programmatically find pre and co-requisites.

Listed below are a few examples. from a query for 2019S.

#### Pre and Co Requisite Examples
```json
{
    "section": "CS 370A",
    "title": "Creative Prob. Solv & Team Prog.",
    "callNumber": "10458",
    "credits": 3,
    "maxEnrollment": "36",
    "currentEnrollment": "36",
    "status": "C",
    "instructor": "Borowski B",
    "daysTimeLocation": [
      {
        "day": "M",
        "startTime": "13:15:00Z",
        "endTime": "15:45:00Z",
        "site": "Castle Point",
        "building": "NB",
        "room": "105"
      }
    ],
    "prereqs": "Prerequisite: CS  385 or CS  182<br>or Prerequisite: CS  590 or CPE 590<br>or Prerequisite: CPE 385",
    "coreqs": ""
}
```
```json
{
    "section": "CS 385RA",
    "title": "Algorithms",
    "callNumber": "10460",
    "credits": 0,
    "maxEnrollment": "27",
    "currentEnrollment": "25",
    "status": "O",
    "instructor": "Zamlynny W",
    "daysTimeLocation": [
      {
        "day": "F",
        "startTime": "10:00:00Z",
        "endTime": "10:50:00Z",
        "site": "Castle Point",
        "building": "NB",
        "room": "102"
      }
    ],
    "prereqs": "Prerequisite: CS  284 or CS  181",
    "coreqs": "Corequisite: LEC"
}
```
```json
{
    "section": "MA 123A",
    "title": "Series,Vectors,Functns & Surface",
    "callNumber": "11022",
    "credits": 2,
    "maxEnrollment": "50",
    "currentEnrollment": "56",
    "status": "C",
    "instructor": "Serbin D",
    "daysTimeLocation": [
      {
        "day": "MWF",
        "startTime": "4:00:00Z",
        "endTime": "4:50:00Z",
        "site": "Castle Point",
        "building": "K",
        "room": "360"
      }
    ],
    "prereqs": "Prerequisite: MA  122 or MA  115",
    "coreqs": "Corequisite: RCT<br>--- and D   110A<br>--- and MA  124AA"
}
```
<!-- TODO: format all of this better for later -->
