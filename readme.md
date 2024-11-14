# AI Twin
Multi-agent system based on a langchain.
Telegram is used as a user interface.

## System Overview
A multi-agent system consists of several specialized agents, each performing their role under supervisor guidance.

## Agents and Their Roles

### 1. Supervisor
- Coordinates all agents' work
- Determines necessary steps to fulfill requests
- Delegates tasks to appropriate agents
- Monitors execution process

### 2. Web Researcher
- Responsible for information search
- Processes and analyzes data
- Provides specific answers based on found information

### 3. Personal Info Agent
- Works with user's personal data
- Clarifies required information
- Provides context for other agents

### 4. Mimic
- Delivers information in a more natural, conversational manner
- Adds emotional coloring to responses
- Uses emojis and informal communication style

## Example of Agent Interaction

1. **User Request**: "What's the weather tomorrow?"

2. **Supervisor**: 
   ```
   Need to provide accurate weather information.
   Will require location data.
   Must coordinate other agents.
   ```

3. **Web Researcher**:
   ```
   To provide accurate forecast,
   need specific location.
   Ready to search once location is provided.
   ```

4. **Personal Info Agent**:
   ```
   Location: Lviv
   Context: User wants tomorrow's forecast
   ```

5. **Web Researcher** (after receiving location):
   ```
   Weather in Lviv tomorrow:
   - Temperature: 2-4°C night, 10-12°C day
   - Precipitation: Rain likely
   - Wind: Moderate, 5-7 m/s
   ```

6. **Mimic**:
   ```
   It'll be cool and rainy in Lviv tomorrow! 🌧️
   ```

## Interaction Features

### Parallel Processing
- Information flows through supervisor
- Each agent maintains focused responsibility
- Final result combines all agents' input

### System Benefits
1. **Specialization**
   - Each agent is domain-expert
   - Clear role separation
   - Focused expertise

2. **Flexibility**
   - Adapts to various requests
   - Dynamic task allocation
   - Scalable architecture

3. **Natural Interface**
   - User-friendly responses
   - Context-aware communication
   - Emotional intelligence


![output](https://github.com/user-attachments/assets/a8944490-f60c-496d-bdca-a73d302cc486)
