# YouTrack - My Board

![](My%20Board.jpg)

The YouTrack "My Board" is a personalized, customizable interface designed to provide individual users with a comprehensive and real-time overview of their specific tasks, issues, and project statuses. This dashboard serves as a powerful tool for professionals to manage their work efficiently and stay updated on their individual responsibilities and progress.
Professional Benefits of Using YouTrack "My Dashboard"
1. Enhanced Productivity:
   - By consolidating all relevant information into a single, personalized view, the dashboard reduces the time spent searching for data.
   - Users can focus on their tasks with greater clarity and efficiency, leading to improved productivity.
2. Better Time Management:
   - The time tracking and progress monitoring features help users allocate their time effectively.
   - Individuals can track how much time they spend on different tasks, aiding in better time management and planning.
3. Informed Decision-Making:
   - Access to real-time data and comprehensive issue tracking allows users to make informed decisions regarding their work.
   - The visual representations of progress and status help in quickly identifying potential bottlenecks and areas needing attention.
4. Improved Accountability:
   - The personalized dashboard fosters a sense of ownership and accountability by clearly displaying individual tasks and responsibilities.
   - Users can monitor their own performance and ensure they are meeting their goals and deadlines.
5. Streamlined Communication:
   - The activity stream widget and real-time updates minimize the need for constant communication and status meetings.
   - Users can stay informed about the latest developments without interrupting their workflow.

## Query

### 🗓️ Schedule
```text
( ( Assignee: me or Evaluator: me ) or (Assignee: me and #{No evaluator}) ) and has: {Due Date} state: -Verified tag: -discussed
```
- Change the `tag:` with your team tag

### 😱 Overdue
```text
state: -Verified tag: -discussed and ( Assignee: me or Evaluator: me ) and ( tag: overdue or Due Date: 2020-01-01 .. Today )
```
- Change the `tag:` with your team tag

### 🚀 Work in Progress (WIP)
```text
Assignee: me state: -Verified -Fixed tag: -discussed Due Date: today .. {plus 6M} order by: updated desc
```
- The query is set to `{plus 6M}` due to make lists more manageable and not overwhelming for individual, you can change it to your need  
- Change the `tag:` with your team tag

### 🕰️ non-deadline issues
```text
Assignee: me state: -Verified -Fixed tag: -discussed has: -{Due Date} order by: updated desc 
```
- Change the `tag:` with your team tag

### 🤷‍️ Waiting for feedback
```text
Assignee: me state: -Verified -Fixed tag: discussed order by: updated desc  
```
- Change the `tag:` with your team tag

### 👀 To be evaluated
```text
Evaluator: me state: -Verified order by: updated desc  
```

## Contact
- Author : Agung Sundoro
- Website : https://agungsundoro.com