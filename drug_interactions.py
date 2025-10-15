"""
Drug Interaction Checker (Enhanced Version)
Author: Joe Bou Khalil
License: MIT
Description:
    Type one or more medicine names and get a detailed list
    of known drug interactions and warnings using the OpenFDA API.
"""

import requests
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def get_interactions(drug_name):
    """Fetch drug interaction info from OpenFDA API."""
    url = f"https://api.fda.gov/drug/label.json?search=openfda.brand_name:{drug_name}+openfda.generic_name:{drug_name}&limit=3"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if "results" not in data:
            console.print(f"[yellow]⚠️ No data found for '{drug_name}'.[/yellow]")
            return

        drug_info = data["results"][0]
        console.print(Panel.fit(f"[bold cyan]{drug_name.upper()}[/bold cyan]", title="🔍 Drug Info", style="cyan"))

        # Display drug interactions
        if "drug_interactions" in drug_info:
            table = Table(title="💊 Known Drug Interactions", show_lines=True)
            table.add_column("Drugs That Interact", style="magenta")
            for interaction in drug_info["drug_interactions"]:
                table.add_row(interaction.strip())
            console.print(table)
        else:
            console.print("[green]✅ No specific drug interactions listed in FDA data.[/green]")

        # Display warnings
        if "warnings" in drug_info:
            warning_table = Table(title="⚠️ Warnings", show_lines=True)
            warning_table.add_column("Warning Details", style="red")
            for warning in drug_info["warnings"]:
                warning_table.add_row(warning.strip())
            console.print(warning_table)

    except requests.exceptions.RequestException as e:
        console.print(f"[bold red]❌ Network Error:[/bold red] {e}")
    except Exception as e:
        console.print(f"[bold red]⚠️ Unexpected Error:[/bold red] {e}")

def main():
    console.print(Panel.fit("[bold white]=== Drug Interaction Checker (OpenFDA) ===[/bold white]", style="blue"))
    console.print("[italic yellow]Tip: You can enter multiple drugs separated by commas (e.g., aspirin, ibuprofen)[/italic yellow]")

    while True:
        user_input = console.input("\n[bold cyan]Enter a drug name (or 'exit' to quit): [/bold cyan]").strip()
        if user_input.lower() == "exit":
            console.print("[bold green]Goodbye 👋[/bold green]")
            break

        drugs = [d.strip() for d in user_input.split(",") if d.strip()]
        for drug in drugs:
            get_interactions(drug)
            console.print("\n" + "-"*60 + "\n")

if __name__ == "__main__":
    main()
