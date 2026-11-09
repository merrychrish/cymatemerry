"""Example script: print the number of SmartLead campaigns.

Copy this file to start a new task script.
"""

from cymate.integrations.smartlead import SmartLead


def main():
    campaigns = SmartLead().list_campaigns()
    print(f"Found {len(campaigns)} campaigns")


if __name__ == "__main__":
    main()
