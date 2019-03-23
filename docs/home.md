# Home

## Navigation
- Pages
    - [Home](home.md)
    - [SIT Scheduler API Documentation](sitsched.md)
    - [Stevens.edu Web Scheduler API Documentation](stevens-scheduler.md)
    - [Course Signup System API Documentation](signup.md)
- Sections
    - [Intro / Lay of the Land](#intro--lay-of-the-land)
    - [Our Code](#our-code)
        - [Term and Section Data](#term-and-section-data)
            - [Term Spec](#term-spec)
            - [Section Spec](#section-spec)
            - [Meeting Spec](#meeting-spec)
            - [Requirement Spec](#requirement-spec) 

## Intro / Lay of the Land
This is probably gonna be the worst documentation you've read in your entire life, so bear with me here.

At the top of every page, there'll be a list of pages (should be updated) and a list of sections in the current page 
(definitely should be updated). If at any time you want to read any other pages, you can use that.

This whole folder will just be me writing things down that I want to remember, and that are generally important to the project.
Right now, there are 4 pages: this one, [one about the website sitscheduler.com](sitsched.md), 
[one about web.stevens.edu/scheduler](stevens-scheduler.md), and finally [one about the official stevens signup portal](signup.md).
Documentation about sitscheduler was included because it was thought to be the best / easiest source of class information, but 
recent findings have revealed that web.stevens.edu/scheduler is a more reliable and official source of class information.
<!-- TODO: Document actual code and what it give back -->

## Our Code
### Term and Section Data
The file `/src/term_and_section_data.py`, there are n functions of note.

| Python Function | Description |
|---|---|
| `terms()` | Gets a list of python dictionaries describing terms that [stevens web server](https://web.stevens.edu/scheduler/core) knows about. |
| `sections(term_code)` | Gets a list of python dictionaries describing course sections that are in a term. `term_code` is the api code for a specific term, as given by `terms()` |

#### Term Spec
A single term will have only two keys: `code`, and `description`. 

`code` is a string that is used used in `sections(term_code)`. 

`description` is a string with a short description of the term in question.

__**Examples:**__
```python
{'code': '2018F', 'description': '2018 Fall Catalog'}
``` 
```python
{'code': '2019B', 'description': '2019 Summer II Catalog'}
``` 
```python
{'code': '2016W', 'description': '2016 Intersession Catalog'}
``` 

#### Section Spec
A single section will have one of the items in the following table:

| Key | Description |
|---|---|
| `section` | The name of the section (e.g. `"CS 284A"`) |
| `title` | A human readable name of the course (e.g. `"Data Structures"`) |
| `call_number` | A String representing the course call number as used by the stevens course sign-up porta;. (e.g. `"10511"`) |
| `min_credits` | An integer representing the smallest amount of credits you can get from this course (e.g. `4`) |
| `max_credits` | An integer representing the largest amount of credits you can get from this course (e.g. `4`) |
| `max_enrollment` | An integer representing the most people that can be enrolled in the class (e.g. `50`) |
| `current_enrollment` | An integer representing the most people that are currently enrolled in the class (e.g. `50`) |
| `status` | A string representing the status of the class (possible values include `"open"`, `"closed"`, `"hold"`, and `"cancelled"`. |
| `date_span` | A tuple with two date objects, where the first element is the starting date, and the last element is the ending-date. Represents the date the section starts being offered and stops being offered. Representation of tuple:`(start_date, end_date)`|
| `instructor_1` | The name of the first instructor teaching the class, in a string. (e.g. `"Bonelli E'"`)|
| `term` | The term code representing the term that this section belongs to. (e.g. `"2019F"`)|
| `meetings` | A list of python dictionaries representing information about the section's meetings, like location, time, and site information. For information about meetings, see the [Meeting Spec](#meeting-spec) section. |
| `requirements` | A list of python dictionaries representing information about section requirements. For more information about section requirements, see the [Requirement Spec](#requirement-spec) section. |

##### Meeting Spec
Every individual meeting will be described by a python dictionary with six keys: 
`"day"`, `"time_span"`, `"site"`, `"building"`, `"room"`, and `"activity"`. The six keys are described in the table below.

<!-- TODO -->
| Key | Description |
|---|---|
| `day` |  |
| `time_span` |  |
| `site` |  |
| `building` |  |
| `room` |  |
| `activity` |  |

##### Requirement Spec
Every individual requirement will be a python dictionary with two keys: `"description"`, and `"code_list"`. 
The two keys are described in the table below.

| Key | Description |
|---|---|
| `description` | A brief human readable description of the requirement. (e.g. `"Prerequisite course required: CS  115"`) |
| `code_list` | A list of strings representing API codes and values that pertain to then. Will generally be in the form of `[control, value1, value2. ..., valuen]`. For more information about what control and value means here, see the [Course Requirement Designators](stevens-scheduler.md#course-requirements-designators) and [Control Designators](stevens-scheduler.md#control-designators) sections in the [page about the stevens web server](stevens-scheduler.md). |
