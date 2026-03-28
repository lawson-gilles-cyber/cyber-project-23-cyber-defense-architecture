# Cyber Defense Architecture Simulation

from components.ids import detect_intrusion
from components.siem import correlate_events
from components.threat_intel import enrich_data
from components.soar import respond_to_threat

# Load logs
with open("data/logs.txt", "r") as file:
    logs = file.readlines()

print("=== Cyber Defense Architecture ===\n")

# Step 1: IDS detection
alerts = detect_intrusion(logs)

# Step 2: SIEM correlation
correlated = correlate_events(alerts)

# Step 3: Threat intelligence enrichment
enriched = enrich_data(correlated)

# Step 4: SOAR response
respond_to_threat(enriched)
