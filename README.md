# Cat CI

This is a Python based CI framework for those, who are lazy as a cats.

Requirements
============

# web based interface:
- MVC based implementation
- Rest interfaces, and HTTP(S) service
- Interactive, dynamic web pages
# users:
- Possible to add, delete, modify users
- Different user groups (administrator, developer, tester, other)
- Group or user based permission definition
# runnable pipelines:
- Easy definition of the pipeline task
- Extendable tasks and pipelines
- One-Click starting
# detailed views:
- Full flow in pipeline and task views
- Running log in pipeline and task views
- Detail view for all pipelines
# separate result and building flow:
- Downloadable results of the jobs
- Archived full results of jobs (gathered and saved)
- Small storage required
# reachable resource information:
- Rest API for every possible elements
- Detail and listing requests for building elements
- Easy create and delete possibility
# global configuration for common usage:
- Global configuration table for common variables
- Possible credential saving and usage
- Permission settings for common groups
# easy flow definition:
- Web based building environment for pipelines and tasks
- Block based definitions, and restructure
- Reusable blocks in other tasks.
# permission based usage:
- Permissions for seeing pipelines and tasks
- Permission for changing pipelines and tasks
- Permission for running piplines and tasks
# database based data storage:
- Save building elements in database
- Use database to store information about results
- Use database for reusability
# separate building environment:
- Separate building environments on filesystem level (Different directory)
- Separate building environments on program level (Different virtenv???)
- Separate building environments on system level (Different OS??? Docker maybe)

Specification
=============

MVC architecture:

Model:
- User
- Pipeline
- Task
- Block ?
- Command
- View
- Permission
View:
- Main pages
- Settings pages
- Listing views
- Detailed views
- Rest API
- Resource management
Control:
- Database Control
- Block building Control
- Permission Control
- User Control
- Running Control
- Result Control
- Environment Control
