#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from dotenv import load_dotenv

from ai_marketing_crew.crew import AiMarketingCrew

# Lade Umgebungsvariablen aus .env
load_dotenv()

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Führt die Marketing Crew aus mit Produkt-Informationen.
    """
    # Produkt-Informationen gemäß PRD
    inputs = {
        'product_name': 'AutoSheet IQ – AI-powered Excel automation',
        'product_description': (
            'AutoSheet IQ ist eine innovative SaaS-Lösung, die künstliche Intelligenz nutzt, '
            'um Excel-Arbeitsabläufe zu automatisieren. Das Produkt ermöglicht es Nutzern, '
            'komplexe Datenanalyse-Aufgaben durch intelligente Automatisierung zu vereinfachen, '
            'Formeln automatisch zu generieren, Daten zu bereinigen und Insights zu extrahieren.'
        ),
        'target_audience': (
            'Geschäftsführer, Datenanalysten und Office-Manager in kleinen bis mittelgroßen '
            'Unternehmen, die regelmäßig mit Excel arbeiten und ihre Produktivität steigern möchten. '
            'Zielgruppe: 25-55 Jahre, technikaffin, aber keine Programmiererfahrung nötig.'
        ),
        'budget': '€15.000 pro Quartal',
        'current_date': datetime.now().strftime('%Y-%m-%d'),
    }

    try:
        print("=" * 80)
        print("Marketing Crew AI - Starte vollständigen Marketing-Workflow")
        print("=" * 80)
        print(f"Produkt: {inputs['product_name']}")
        print(f"Zielgruppe: {inputs['target_audience'][:80]}...")
        print(f"Budget: {inputs['budget']}")
        print(f"Datum: {inputs['current_date']}")
        print("=" * 80)
        print()

        result = AiMarketingCrew().crew().kickoff(inputs=inputs)
        
        print()
        print("=" * 80)
        print("Marketing Crew AI - Workflow abgeschlossen!")
        print("=" * 80)
        print("Generierte Dateien befinden sich in resources/ und resources/drafts/")
        
        return result
    except Exception as e:
        raise Exception(f"Ein Fehler ist beim Ausführen der Crew aufgetreten: {e}")


def train():
    """
    Trainiert die Crew für eine bestimmte Anzahl von Iterationen.
    """
    inputs = {
        'product_name': 'AutoSheet IQ – AI-powered Excel automation',
        'product_description': (
            'AutoSheet IQ ist eine innovative SaaS-Lösung, die künstliche Intelligenz nutzt, '
            'um Excel-Arbeitsabläufe zu automatisieren.'
        ),
        'target_audience': (
            'Geschäftsführer, Datenanalysten und Office-Manager in kleinen bis mittelgroßen '
            'Unternehmen.'
        ),
        'budget': '€15.000 pro Quartal',
        'current_date': datetime.now().strftime('%Y-%m-%d'),
    }
    
    try:
        AiMarketingCrew().crew().train(
            n_iterations=int(sys.argv[1]),
            filename=sys.argv[2],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"Ein Fehler ist beim Training der Crew aufgetreten: {e}")


def replay():
    """
    Wiederholt die Crew-Ausführung ab einer bestimmten Task.
    """
    try:
        AiMarketingCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"Ein Fehler ist beim Wiederholen der Crew aufgetreten: {e}")


def test():
    """
    Testet die Crew-Ausführung und gibt die Ergebnisse zurück.
    """
    inputs = {
        'product_name': 'AutoSheet IQ – AI-powered Excel automation',
        'product_description': (
            'AutoSheet IQ ist eine innovative SaaS-Lösung, die künstliche Intelligenz nutzt, '
            'um Excel-Arbeitsabläufe zu automatisieren.'
        ),
        'target_audience': (
            'Geschäftsführer, Datenanalysten und Office-Manager in kleinen bis mittelgroßen '
            'Unternehmen.'
        ),
        'budget': '€15.000 pro Quartal',
        'current_date': datetime.now().strftime('%Y-%m-%d'),
    }

    try:
        AiMarketingCrew().crew().test(
            n_iterations=int(sys.argv[1]),
            eval_llm=sys.argv[2],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"Ein Fehler ist beim Testen der Crew aufgetreten: {e}")


def run_with_trigger():
    """
    Führt die Crew mit Trigger-Payload aus.
    """
    import json

    if len(sys.argv) < 2:
        raise Exception("Kein Trigger-Payload bereitgestellt. Bitte JSON-Payload als Argument angeben.")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Ungültiger JSON-Payload als Argument bereitgestellt")

    inputs = {
        "crewai_trigger_payload": trigger_payload,
        'product_name': '',
        'product_description': '',
        'target_audience': '',
        'budget': '',
        'current_date': datetime.now().strftime('%Y-%m-%d'),
    }

    try:
        result = AiMarketingCrew().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"Ein Fehler ist beim Ausführen der Crew mit Trigger aufgetreten: {e}")
