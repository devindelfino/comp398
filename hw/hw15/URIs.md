URIs
====

### *Service Name*: WheatonProfs
### *Address*: http://WheatonProfs/

BackgroundInformation
------------

*Resource*: OfficeHours

*URI*: http://WheatonProfs/Information/{ProfID}

*Format*: text/xml

|  Method  | Description |
|:--------:|:------------|
|   GET    | Read a professor's name, background info, research interests, and contact information |
| POST/PUT | Update or add background or contact information |
|  DELETE  | Delete outdated background or contact information |

Office Hours
------------

*Resource*: OfficeHours

*URI*: http://WheatonProfs/OfficeHours/{ProfID}

*Format*: text/xml

|  Method  | Description |
|:--------:|:------------|
|   GET    | Read a professor's office hours information |
| POST/PUT | Update or add new office hour information |
|  DELETE  | Delete outdated office hour information |

Office Location
------------

*Resource*: OfficeLocation

*URI*: http://WheatonProfs/OfficeLocation/{ProfID}

*Format*: text/xml

|  Method  | Description |
|:--------:|:------------|
|   GET    | Read a professor's office location information |
| POST/PUT | Update or add new office location information |
|  DELETE  | Delete outdated office location information |

Current Courses
------------

*Resource*: CurrentCourses

*URI*: http://WheatonProfs/CurrentCourses/{ProfID}

*Format*: text/xml

|  Method  | Description |
|:--------:|:------------|
|   GET    | Read the list of courses that the professor is teaching in the current semester|
| POST/PUT | Update or add information on a new course being taught by the professor |
|  DELETE  | Delete the professor's outdated courses from past semesters |

Current Courses
------------

*Resource*: Search

*URI*: http://WheatonProfs/Search?

*Format*: text/xml

|  Method  | Description |
|:--------:|:------------|
|   GET    | Read information regarding the searched professor|

|  Query Parameter |  Type  |  Optional?  | Description |
|:----------------:|:------:|:-----------:|:------------|
|   Last Name      | String |     Yes     | Last name of a professor |
|   Department     | String |     Yes     | Specific department to which the professor belongs |

