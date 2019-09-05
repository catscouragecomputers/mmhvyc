## Brainstorm
- Software system that analyzes open-source software metrics reflect:
    - How well collaboration is working on project
    - Health of the project for customers and streamlining business/engineer communication

### Requirements
(Practicality)(Priority)
- (1)(2) Metrics should be tracked with automated updates.
- (3)(3) Notifications should be relayed to people working on the project.
- (1)(2) Investors need a UI to visualize data.
- (2)(4) Developers need access to a database to store metrics data.
- Users:
    - ()() Should be able to implement the API into any part of the system
    - ()() Better visualizations of metrics
    - ()() System needs multiple user endpoints (API) to access specific metrics for their respective roles
    - ()() Users need version control implemented to track timestamps of commits, issues, pull requests, etc.
    
### Functional Requirements
- ()() Customer can monitor commits/pulls/forks over time, average size of commits, etc
- ()() Customer can monitor developer interaction (how often are people talking)
- ()() Customer can visit repositories to get metrics
- ()() Customer can sort projects by comparing metrics to successfuly projects
- ()() Customer can find and "rate" project similarity
- ()() Customer can UI system to display metrics in different ways

### System Requirements
- System needs a massive database system for developers.

Metrics are based on:
    - How often commits are made
    - Volume of commits
    - Time elapsed between commits
    - Number of people working on branches
    - Tracking code reuse in other projects
