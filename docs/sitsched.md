# SIT Scheduler API Docs

## Navigation
- [Home](home.md)
- [SIT Scheduler API Documentation](sitsched.md)
- [Course Signup System API Documentation](signup.md)

## Course information

To get information on the courses, [SITScheduler](http://sitscheduler.com/) uses
a get request to URL `https://stevens-scheduler.cfapps.io/p/{SEM}`, where `{SEM}`
is the semester code, like 2019F, or 2018S.

### Example Response:
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
[](TODO: format this shit better)
