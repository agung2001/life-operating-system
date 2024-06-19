# YouTrack - Team Board

The YouTrack team dashboard is a YouTrack custom dashboard that provides a centralized, customizable interface for teams to monitor and manage their projects and tasks. It is designed to give a comprehensive overview of the project's status, helping team members stay informed and aligned.
Benefits of Using a YouTrack Team Dashboard
1. Enhanced Visibility:
   - Teams gain a clear and comprehensive view of their projects, helping to ensure that everyone is on the same page.
   - Managers and team members can easily track progress and identify potential issues before they become critical. 
2. Better Decision Making:
   - Access to up-to-date information helps teams make informed decisions.
   - Visual representations of data (e.g., charts and graphs) make it easier to interpret trends and patterns.
3. Streamlined Communication:
   - The dashboard serves as a central point for project updates, reducing the need for constant status meetings and check-ins.
   - Team members can post comments and updates directly on the dashboard, fostering better communication.
4. Customization for Specific Needs:
   - Teams can tailor the dashboard to fit their specific workflows and preferences.
   - Different teams within the organization can have their own customized dashboards that cater to their unique needs and objectives.

## Query

### 🗓️ Schedule
```text
has:{Due Date} state: -Verified tag: -discussed tag: team
```
- Change the `tag:` with your team tag

### 😱 Overdue
```text
state: -Verified tag: -discussed and Due Date: 2020-01-01 .. Today and tag: team 
```
- Change the `tag:` with your team tag

### 🚀 Work in Progress (WIP)
```text
state: -Verified -Fixed tag: -discussed order by: updated desc tag: team
```
- Change the `tag:` with your team tag

### 🕰️ non-deadline issues
```text
state: -Verified -Fixed tag: -discussed has: -{Due Date} order by: updated desc tag: team 
```
- Change the `tag:` with your team tag

### 🤷‍️ Waiting for feedback
```text
state: -Verified -Fixed order by: updated desc and (tag: discussed and tag: team ) 
```
- Change the `tag:` with your team tag

### 👀 To be evaluated
```text
state: -Verified order by: updated desc has: Evaluator tag: team 
```

### 🫣 Unresolved
```text
State: -Verified tag: team 
```
