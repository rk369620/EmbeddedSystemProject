#Vehicle Accident Detection System

Road accidents are sudden, unexpected events that can cause serious harm to people and property. Being able to detect accidents as they happen on video can help alert authorities quickly and provide useful logs for analysis. This project builds a system that automatically monitors video footage of roads and detects accidents in real-time.

The system works by analyzing the motion of vehicles in the video. It looks for sudden, strong movements in the road area, which are typical when a vehicle collides or loses control. To avoid To avoid false alarms, it only triggers an alert if this unusual motion persists over multiple consecutive frames, ensuring that normal traffic or camera shakes do not cause a false detection.
When an accident is detected, the system:

Updates a visual interface, showing the status of the system in real-time

Sends an alert (simulated for demonstration, can be extended to devices like Raspberry Pi)

Logs the event with timestamp and motion confidence into a JSON file for record-keeping

The project also displays the video while monitoring, allowing users to see the accident happen and verify detection. It includes a status panel that turns green when the system is idle and red when an accident is detected. Once the video ends, the system automatically closes the interface and stops monitoring.
