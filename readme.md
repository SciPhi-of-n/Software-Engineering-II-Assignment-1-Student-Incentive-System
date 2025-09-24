# General Commands

_Initialize the database_
```bash
$ flask init
```

_Roll back to previous stae_
```bash
$ flask rollback
```

_View student leaderboard_
```bash
$ flask leaderboard
```

# Student Commands

_Create a new student_
```bash
$ flask student create student_username student_password hours
```
(Note: Inputting hours is optional. If not done, students hours will be set to 0)

_Display a list of students_
```bash
$ flask student list
```

_Make a request to confirm hours_
```bash
$ flask student request student_id
```

_View the status of a request made by a student_
```bash
$ flask student status student_id
```

_View the accolades of a student_
```bash
$ flask student accolades student_id
```

# Staff Commands

_Create a new member of staff_
```bash
$ flask staff create staff_username staff_password
```

_Display a list of staff members_
```bash
$ flask staff list
```

_Log hours to a student_
```bash
$ flask staff log student_id hours
```
(Note: Logging hours sets the student's hours to the hours inputted. It does not add hours to any existing within a student)

_View all requests made_
```bash
$ flask staff view
```

_Respond to a request with "approved" or "denied"_
```bash
$ flask staff respond request_id response
```
(Note: responses can be in double quotes or no quotes)
