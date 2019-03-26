# Stevens.edu Web Scheduler API Docs
## Navigation
- Pages
    - [Home](home.md)
    - [SIT Scheduler API Documentation](sitsched.md)
    - [Stevens.edu Web Scheduler API Documentation](stevens-scheduler.md)
    - [Course Signup System API Documentation](signup.md)
- Sections
    - [Intro / Lay of the Land](#intro--lay-of-the-land)
    - [Directory Structure](#directory-structure)
    - [API Commands](#api-commands)
    - [Help Page](#help-page)
        - [Term Designators](#term-designators)
        - [Session Designators](#session-designators)
        - [Section Status Designators](#section-status-designators)
        - [Site Designators](#site-designators)
        - [Building Designators](#building-designators)
        - [Activity Designators](#activity-designators)
        - [Course Requirements Designators](#course-requirements-designators)
            - [Control Designators](#control-designators)
            - [Argument Designators](#argument-designators)

## Intro / Lay of the Land

## Directory Structure
[Removing the php file from the endpoint](https://web.stevens.edu/scheduler/core/) gives us what seems to be a
directory structure. Going further back to `web.stevens.edu/scheduler` only gives us the actual application, which
isn't relevant for reverse engineering purposes.

In what we'll consider the root directory (`web.stevens.edu/scheduler/core/`), there are many files and folders of note. 
It's imporant to observe that first of all, every term code (i.e. `2018F`, `2019S`, etc.) is updated with its own folder
(not meant to be public facing, I assume). I have yet to discern what is doing the updating, but the information from here
moves faster than from [sitscheduler.com](http://sitscheduler.com/), so it can be reasonably assumed that it's some API 
listener close to the official course sign up source.

In the root directory, the files of interest are `/calendar.php`, `/core.php`, `/test.php`, `/redirect.php`, `/terms.xml`, 
`/webevents.html`, and `/webevents.php`. `/core.php` is obviously the core application, which serves up data to the scheduler in 
xml form when given specific queries. `/terms.xml` seems to be an exhaustive list of term codes and their meanings. 
`/webevents.html` and `/webevents.php` are interesting, because `/webevents.html` just seems to be a file to search for information about
web courses, with `/webevents.php` presumably being a backend for that. `/redirect.php`, `/test.php`, and `/calendar.php` 
still need to be investigated, although it is known that `/calendar.php` seems to download an ics text file with an error message in it.
`/core.php` and `/test.php` will be covered in their own sections.

<!-- TODO: talk about the following link. It relates to `/calendar.php`!: -->
<!-- webcal://www.stevens.edu/scheduler/core/calendar.php?2019F=10528,10523,10529,12215,10567,10577&format=3 -- >

Aside from the folders for each term, there are a few other folders (`/debug terms`, `/designators`, `/export`, `/includes`, and `/php_cache`). 
`/debug terms` seems to just have some text files in them with extra information, presumably used as a bandaid for debugging purposes.
`/designators` has some text files that seem to have been used in the creation of the help website, but it also has a file 
`/designators/designators.xml`, which seems to be an exhaustive list of all designators in xml format. IT can be assumed that these are relatively up to date.
At the time of writing this, `/export` was just an empty folder. `/includes`, however, seems to be a big dumping ground for testing,
l1braries, etc. 

## API Commands
<!-- TODO: document `core.php` commands -->

## Help Page
This section contains information given by visiting [this](https://web.stevens.edu/scheduler/core/core.php?cmd=help) API enpoint.
You can even point your web browser at it. The information displayed in this section is updated as of
3/21/2019 (M/DD/YYY). Enjoy.

---

This contains all the information needed to interpret all information provided by this program.
The first section is about asking for terms.
In order to get a term, format the request with `/cgi-bin/cgiwrap/w3u_scheduler/scheduler/core/core.php?cmd=getxml&term=<the term you want>`
The term you want should be put in the form of a 4 digit year followed by a term designator

### Term Designators
| Designator | Description         |
|------------|---------------------|
| A          | Summer Session 1    |
| B          | Sumer Session 2     |
| F          | Fall                |
| W          | Winter Intersession |
| S          | Spring              |

### Session Designators
| Designator | Description          |
|------------|----------------------|
| (BLANK)    | Normal Academic Term |
| S          | Special offering     |
| O          | Off Campus           |
| T          | Trimester            |
| 2          | Second Spring        |
| M          | Math (STAMP)         |
| B          | Beijing              |
| C          | Computer Science     |
| D          | SDOE Module          |
| H          | Humanities           |
| X          | Chemistry            |
| W          | WebCampus            |
Session Designators found: 12 

### Section Status Designators
| Designator | Description |
|------------|-------------|
| O          | Open        |
| C          | Closed      |
| H          | Hold        |
| X          | Cancelled   |
Section Status Designators found: 4 

### Site Designators
| Designator | Description                                         |
|------------|-----------------------------------------------------|
| (BLANK)    | Hoboken Campus                                      |
| I          | US Army ARDEC Open Site (Picatinny Arsenal, NJ)     |
| J          | NECA Open Site (Whippany, NJ)                       |
| K          | Glaxo SmithKline Open Site (Parsippany, NJ)         |
| M          | Florham Park Open Site (Florham, NJ)                |
| N          | Hanover Marriott Open Site (Whippany, NJ)           |
| O          | ADP Open Site (99 Jefferson Rd., Parsippany, NJ)    |
| Q          | Smith Middle School (Ramsey, NJ)                    |
| R          | EMCORE Open Site (Somerset, NJ)                     |
| S          | Intel Open Site (Parsippany, NJ)                    |
| T          | BAE Systems Open Site (Wayne, NJ)                   |
| U          | Unilever Bestfoods Open Site (Englewood Cliffs, NJ) |
| W          | Foster Wheeler Open Site (Clinton, NJ)              |
| V          | U.S. Navy Open Site (Lakehurst, NJ)                 |
| Y          | Fort Monmonth Open Site (Ft. Monmouth, NJ)          |
| X          | Raritan Valley Comm. Col. (North Branch, NJ)        |
| Z          | Loral Skynet Open Site                              |
| AC         | Air Cruiser's Company (Belmar, NJ)                  |
| AE         | Allied Signal (Teterboro, NJ)                       |
| AH         | American Home Products (Madison, NJ)                |
| AG         | American General Info Services                      |
| AN         | ANSWER (Arlington, VA)                              |
| AO         | AT&T Solutions (Florham Park, NJ)                   |
| AP         | ADP (99 Jefferson Rd., Parsippany, NJ)              |
| AR         | US Army ARDEC (Picatinny Arsenal, NJ)               |
| AT         | AT&T                                                |
| A2         | ADP (15 Waterview Blvd., Parsippany,NJ)             |
| A3         | ADP (15 Waterview Blvd., Parsippany, NJ)            |
| BD         | Bellcore Distance Learning                          |
| BE         | Unilever Bestfoods (Englewood Cliffs, NJ)           |
| BF         | BASF (Mt. Olive, NJ)                                |
| BG         | Bangalore MS/IS Program (Bangalore, India)          |
| BJ         | BIT Telecomm. Program (Beijing, China)              |
| BK         | Brookdale Comm. College (Lincroft, NJ)              |
| BL         | Lucent Bell Labs (Whippany, NJ)                     |
| BO         | Boeing (St. Louis, MO)                              |
| BR         | AT&T (Bridgewater, NJ)                              |
| BS         | Bristol Myers Squibb (Skillman, NJ)                 |
| BT         | Verizon                                             |
| BU         | Bulgaria MS/IS Program (Sophia, Bulgaria)           |
| B1         | Bristol Myers Squibb (Skillman, NJ)                 |
| B2         | Cent. Univ. Fin. & Econ. (Beijing, China)           |
| CD         | Cendant (Parsippany, NJ)                            |
| CE         | US Army CECOM (Fort Monmouth, NJ)                   |
| CH         | Chubb/Avaya                                         |
| CN         | Cardinal Health                                     |
| CU         | CUFE Program (Beijing, China)                       |
| C1         | Cendant Open Site (Parsippany, NJ)                  |
| DC         | Washington, DC                                      |
| DL         | Distance Learning                                   |
| DR         | Dominican Republic                                  |
| DS         | Datascope (Paramus, NJ)                             |
| DV         | NSA (Denver, CO)                                    |
| EC         | Englehard Corp. (Iselin, NJ)                        |
| EG         | EG&G/NAVSEA (Washington, DC)                        |
| EM         | EMCORE (Somerset, NJ)                               |
| ES         | Essex Community College                             |
| ET         | Ethicon (Somerville, NJ)                            |
| E1         | Ethicon Open Site (Somerville, NJ)                  |
| FA         | Federal Aviation Admin. (Atlantic City, NJ)         |
| FR         | Paris MS/IS Program (Paris, France)                 |
| FW         | Foster Wheeler (Clinton, NJ)                        |
| GD         | General Dynamics (Florham Park, NJ)                 |
| G0         | General Dynamics Open Site (Florham Park, NJ)       |
| GV         | General Dynamics (Burlington, VT)                   |
| IM         | ImClone (Branchburg, NJ)                            |
| IN         | Intel (Parsippany, NJ)                              |
| IP         | IBM (Poughkeepsie, NY)                              |
| IR         | ITT Night Vision (Roanoke, VA)                      |
| IS         | ISO Corporation (Jersey City, NJ)                   |
| IT         | ITT Industries (Clifton, NJ)                        |
| JJ         | Johnson & Johnson (Raritan, NJ)                     |
| KO         | Buskerud University (Kongsberg, Norway)             |
| LC         | Liz Claiborne (North Bergen, NJ)                    |
| LD         | Lucent (Various Sites)                              |
| LE         | Langan Engineering (Elmwood Park, NJ)               |
| LH         | Lucent Technologies (Holmdel, NJ)                   |
| LP         | Lucent Technologies (Piscataway, NJ)                |
| LS         | Loral Skynet                                        |
| L3         | L3 Communications (Greenville, TX)                  |
| MA         | BAE System, CNI (Wayne, NJ)                         |
| MB         | MTM (Woodbridge, NJ)                                |
| MC         | MTM (Hanover Courtyard, Whippany, NJ)               |
| MD         | Middletown                                          |
| MF         | MTM (Florham Park, NJ)                              |
| MH         | MTM (Holmdel, NJ)                                   |
| MI         | MTM (Middletown/Freehold, NJ)                       |
| ML         | Lockheed Martin (Moorestown, NJ)                    |
| MM         | MTM (Morristown, NJ)                                |
| MN         | MTM (Navesink, NJ)                                  |
| MO         | MTM (Fort Monmouth, NJ)                             |
| MP         | MTM (Piscataway, NJ)                                |
| MR         | Merck (Rahway, NJ)                                  |
| MT         | Mgmt of Technology                                  |
| MU         | Murray Hill                                         |
| MW         | Merck (Whitehouse Station, NJ)                      |
| MY         | MTM (Holiday Inn, Tinton, NJ)                       |
| NC         | NECA (Whippany, NJ)                                 |
| NE         | Northrop-Grumman/Educational (Bethpage, NY)         |
| NG         | Northrop-Grumman (Bethpage, NY)                     |
| NL         | U.S. Navy (Lakehurst, NJ)                           |
| NM         | NASA Marshall Space Flight Center (Huntsville, AL)  |
| NO         | Northrop-Grumman (El Segundo, CA)                   |
| NS         | National Starch (Bridgewater, NJ)                   |
| O1         | Hanover Marriott Courtyard (Hanover, NJ)            |
| O2         | Ramada (East Hanover, NJ)                           |
| O3         | ADP Open Site (15 Waterview Blvd., Parsippany,NJ)   |
| PF         | Pfizer (Brooklyn, NY)                               |
| PG         | PSE&G (Newark, NJ)                                  |
| PH         | Prudential (Holmdel, NJ)                            |
| PI         | AT&T (HUFA), Somerset                               |
| PX         | Pax River, MD                                       |
| P2         | Pfizer (Manhattan, NY)                              |
| RA         | Ramsey Middle School                                |
| SA         | Baltimore, MD                                       |
| SB         | Salomon/Smith-Barney (Manhattan, NY)                |
| SC         | Schering Plough (Kenilworth, NJ)                    |
| SE         | Saturday MS/IS                                      |
| SI         | AT&T Local Services (Staten Island, NY)             |
| SK         | GlaxoSmithKline (Parsippany, NJ)                    |
| SL         | Sandia National Laboratories (Albuquerque, NM)      |
| SO         | AT&T (Somerset, NJ)                                 |
| SP         | Prudential (Newark/Roseland, NJ)                    |
| SS         | Pearson Education (Upper Saddle River, NJ)          |
| ST         | Saturday MS/IS (Hoboken, NJ)                        |
| SV         | SAIC (McLean, VA)                                   |
| TP         | AT&T Local Services (Dayton, NJ)                    |
| UB         | UBS (Weehawken, NJ)                                 |
| VB         | Verizon Wireless (Bedminster, NJ)                   |
| VO         | Verizon Wireless (Orangeburg, NY)                   |
| VW         | Verizon Wireless (Warren, NJ)                       |
| WH         | Whippany                                            |
| WS         | Web Campus                                          |
| WX         | Woodbridge, NJ Open Site                            |
| ZU         | Switzerland MS/IS Program (Zurich, Switzerland)     |
Designators found: 135

### Building Designators
| Designator | Description                                         |
|------------|-----------------------------------------------------|
| (BLANK)    | NOT SPECIFIED                                       |
| B          | Burchard Building                                   |
| C          | Carnegie Laboratory                                 |
| D          | Davidson Laboratory                                 |
| E          | Edwin A. Stevens Hall                               |
| G          | Earl L. Griffith Building                           |
| K          | Kidde Complex                                       |
| L          | Lieb Building                                       |
| M          | Morton Complex                                      |
| N          | Nicoll Environmental Lab                            |
| P          | Peirce Complex                                      |
| S          | Wesley J. Howe Center                               |
| W          | Walker Gymnasium                                    |
| X          | McLean Chemical Sciences Building                   |
| AH         | Alexander C. Humphreys Hall                         |
| BC         | Babbio Center for Technology Management             |
| CH         | Charles Hayden Hall                                 |
| DJ         | Jacobus Student Center                              |
| EP         | Edgar Palmer Hall                                   |
| GH         | Gatehouse                                           |
| GR         | Graduate Residence Halls                            |
| HD         | Harvey N. Davis Hall                                |
| TH         | Jonas Hall                                          |
| MS         | Married Students' Apartments                        |
| WR         | Undergraduate Women's Halls                         |
| SL         | Samuel C. Williams Library                          |
| OFF        | Off Campus                                          |
| SCH        | Schaefer Athletic Center                            |
| 110WA      | 110 Washington Street                               |
| 600RS      | 600 River Street                                    |
| 602RS      | 602 River Street                                    |
| 604RS      | 604 River Street                                    |
| 606RS      | 606 River Street                                    |
| 616RS      | 616 River Street                                    |
| 802CP      | Lore El Center for Women in Engineering and Science |
| 831CP      | 831 Castle Point Terrace                            |
| 835CP      | 835 Castle Point Terrace                            |
| 1036P      | 1036 Park Avenue                                    |
| 253-3      | 253 3rd Street                                      |
Designators found: 39

### Activity Designators
| Designator | Description                         |
|------------|-------------------------------------|
| LEC        | lecture                             |
| L/L        | lecture/lab                         |
| LAB        | laboratory                          |
| PSI        | personalized self-paced instruction |
| QUZ        | quiz                                |
| RCT        | recitation                          |
| SEM        | seminar                             |
| PRA        | practicum                           |
| HSG        | housing (dorm)                      |
| MCE        | Multiple Course Entry base course   |
| WSP        | Work Shop                           |
Activity Designators found: 11

### Course Requirements Designators
#### Control Designators
| Designator | Description                                 |
|------------|---------------------------------------------|
| (BLANK)    |                                             |
| CC         | Course corequisite required                 |
| CS         | Section corequisite required                |
| CA         | Activity corequisite required               |
| RQ         | Prerequisite course required                |
| R&         | (cont.) Prerequisite course reqd            |
| RQM        | Prereq course reqd w/ min grade             |
| RM&        | (cont.) Prereq reqd w/ min grade            |
| RQT        | Prerequisite test required                  |
| RT&        | (cont.) Prerequisite test required          |
| NQ         | Concurrent Prereq course required           |
| N&         | (cont.) Concur Prereq course reqd           |
| NQM        | Concur Prereq reqd w/ min grade             |
| NM&        | (cont.) Concur Prereq w/ min grade          |
| MB         | By Application Only                         |
| MP         | Prerequisite Required                       |
| MC         | Corequisite Required                        |
| ML         | Lab Fee Required                            |
| MA         | Permission of Advisor Required              |
| MI         | Permission of Instructor Required           |
| MH         | Department Head Approval Required           |
| MN         | No Credit Course for Departmental Majors    |
| MS         | Studio course; No general Humanities credit |
| MW         | Women Only                                  |
| PAU        | Auditors need instructor permission         |
| PCG        | Permission needed from Continuing ED        |
| PDP        | Permission needed from department           |
| PIN        | Permission needed from instructor           |
| PUN        | Undergrads need instructor permission       |
| PUA        | UGs need permission of Dean of UG Academics |
Control Designators found: 30

#### Argument Designators
| Designator | Description                   |
|------------|-------------------------------|
| (BLANK)    |                               |
| COL        | Student College A 030         |
| DEG        | Student Degree A 042          |
| MAJ        | Student Major A 044           |
| CLASS      | Student Classification A 040  |
| SPCL       | Student Special Program A 050 |
| CERT       | Student Certificate A 045     |
| LEVEL      | Student Level AA615           |
| DEPT       | Student Department Code A 032 |
| MIN        | Student Minor A 044           |
| R01        | REPORT FLAG 1 (119) RT235     |
| R02        | REPORT FLAG 2 (119) RT236     |
| R03        | REPORT FLAG 3 (119) RT237     |
| R04        | REPORT FLAG 4 (119) RT238     |
| R05        | REPORT FLAG 5 (119) RT239     |
| R06        | REPORT FLAG 6 (119) RT240     |
| R07        | REPORT FLAG 7 (119) RT241     |
| R08        | REPORT FLAG 8 (119) RT242     |
| R09        | REPORT FLAG 9 (119) RT243     |
| R10        | REPORT FLAG 10 (119) RT244    |
| R11        | REPORT FLAG 11 (119) RT245    |
| R12        | REPORT FLAG 12 (119) RT246    |
| R13        | REPORT FLAG 13 (119) RT247    |
| R14        | REPORT FLAG 14 (119) RT248    |
| R15        | REPORT FLAG 15 (119) RT249    |
| R16        | REPORT FLAG 16 (119) RT25A    |
| R17        | REPORT FLAG 17 (119) RT25B    |
| R18        | REPORT FLAG 18 (119) RT25C    |
| R19        | REPORT FLAG 19 (119) RT25D    |
| R20        | REPORT FLAG 20 (119) RT25E    |
| A01        | ATHLETIC CODE 01 (119) RT25K  |
| A02        | ATHLETIC CODE 02 (119) RT25L  |
| A03        | ATHLETIC CODE 03 (119) RT25M  |
| A04        | ATHLETIC CODE 04 (119) RT25N  |
| A05        | ATHLETIC CODE 05 (119) RT25P  |
| SUBJ       | Subject Area Majors           |
Argument Designators found: 36
