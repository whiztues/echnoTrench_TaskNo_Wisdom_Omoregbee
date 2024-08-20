import random

# Define the different types of incidents
class Incident:
    def __init__(self, name, description, attack_vector):
        self.name = name
        self.description = description
        self.attack_vector = attack_vector
        self.is_detected = False
        self.is_contained = False
        self.is_erased = False
        self.is_recovered = False

class System:
    def __init__(self, name):
        self.name = name
        self.is_compromised = False

class Scenario:
    def __init__(self, name, incident, systems):
        self.name = name
        self.incident = incident
        self.systems = systems

    def start(self):
        print(f"Starting scenario: {self.name}")
        compromised_system = random.choice(self.systems)
        compromised_system.is_compromised = True
        print(f"System {compromised_system.name} is compromised by {self.incident.name}")

class IncidentResponse:
    def detect(self, scenario):
        if not scenario.incident.is_detected:
            scenario.incident.is_detected = True
            print(f"Incident '{scenario.incident.name}' detected.")
        else:
            print("Incident already detected.")

    def contain(self, scenario):
        if scenario.incident.is_detected and not scenario.incident.is_contained:
            scenario.incident.is_contained = True
            print(f"Incident '{scenario.incident.name}' contained.")
        else:
            print("Incident not detected or already contained.")

    def eradicate(self, scenario):
        if scenario.incident.is_contained and not scenario.incident.is_erased:
            scenario.incident.is_erased = True
            compromised_system = [sys for sys in scenario.systems if sys.is_compromised][0]
            compromised_system.is_compromised = False
            print(f"Incident '{scenario.incident.name}' eradicated from system '{compromised_system.name}'.")
        else:
            print("Incident not contained or already eradicated.")

    def recover(self, scenario):
        if scenario.incident.is_erased and not scenario.incident.is_recovered:
            scenario.incident.is_recovered = True
            print(f"System recovery complete for incident '{scenario.incident.name}'.")
        else:
            print("Incident not eradicated or already recovered.")

# Example usage
systems = [System("Web Server"), System("Database Server"), System("Email Server")]
incident = Incident("Ransomware Attack", "Encrypts files and demands ransom", "Phishing Email")
scenario = Scenario("Ransomware Simulation", incident, systems)

response = IncidentResponse()

scenario.start()
response.detect(scenario)
response.contain(scenario)
response.eradicate(scenario)
response.recover(scenario)
