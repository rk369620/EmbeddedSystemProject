# **Vehicle Accident Detection System**

The system analyzes the **motion of vehicles** in the video. It looks for **sudden, strong movements** in the road area, typical of a vehicle collision or loss of control.  

To prevent false alarms, it only triggers an alert if the unusual motion persists over **multiple consecutive frames**, ensuring normal traffic or camera shake does not generate false detection.

When an accident is detected:

- **Updates a visual interface** showing system status in real-time
- **Sends an alert** (simulated for demonstration; can be extended to devices like Raspberry Pi)
- **Logs the event** with timestamp and confidence into a JSON file

The project also **displays the video while monitoring**, allowing users to **see accidents occur** and verify detection. The status panel:

- **Green** → System Idle
- **Red** → Accident Detected

Once the video ends, the system automatically closes the interface and stops monitoring.

## **Key Features**

- ✅ Real-time accident detection from video  
- ✅ Visual status interface with alerts  
- ✅ Motion-based detection for sudden impacts  
- ✅ Logs accident events for later analysis  
- ✅ Automatically stops when video ends  


