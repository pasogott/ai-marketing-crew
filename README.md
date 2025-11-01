# AI Marketing Crew

Ein Multi-Agent Marketing-System basierend auf CrewAI, das automatisch Marketing-Assets für SaaS-Produkte generiert.

## Übersicht

Dieses System orchestriert vier spezialisierte AI-Agenten, um einen vollständigen Marketing-Workflow durchzuführen:

1. **Head of Marketing** - Marktforschung und Strategieentwicklung
2. **Social Media Content Creator** - Social Media Posts und Content-Kalender
3. **Blog Content Writer** - Blog-Artikel-Entwürfe
4. **SEO Specialist** - Keyword-Listen und SEO-Assets

## Features

- ✅ Automatische Markt- und Wettbewerbsforschung (mit Web-Suche via Serper)
- ✅ Detaillierte Marketing-Strategie basierend auf Forschungsergebnissen
- ✅ Content-Kalender für Social Media Kanäle
- ✅ Kanalspezifische Social Media Post-Entwürfe (LinkedIn, X/Twitter, Instagram)
- ✅ SEO-optimierte Blog-Artikel-Entwürfe
- ✅ Umfassende Keyword-Listen (Produkt-, Problem- und Wettbewerber-Keywords)
- ✅ YAML-basierte Konfiguration (keine Code-Änderungen für Prompt-Updates)
- ✅ Strukturierte Dateiausgabe in `resources/` Verzeichnis

## Installation

Stelle sicher, dass Python >=3.11 installiert ist. Dieses Projekt nutzt [UV](https://docs.astral.sh/uv/) für das Dependency-Management.

### 1. UV installieren

```bash
pip install uv
```

### 2. Dependencies installieren

```bash
crewai install
```

oder

```bash
uv sync
```

### 3. Umgebungsvariablen konfigurieren

Erstelle eine `.env` Datei im Projekt-Root:

```bash
# OpenAI API Key (erforderlich)
OPENAI_API_KEY=your_openai_api_key_here

# Serper API Key (optional, für Web-Suche)
# Erhalte einen Key von: https://serper.dev/api-key
SERPER_API_KEY=your_serper_api_key_here
```

**Hinweis**: Ohne `SERPER_API_KEY` wird die Crew nur LLM-basierte Recherche durchführen (keine aktuelle Web-Suche).

## Verwendung

### Standard-Ausführung

Führe die Marketing Crew mit den vorkonfigurierten Produkt-Informationen aus:

```bash
crewai run
```

oder

```bash
python -m ai_marketing_crew.main
```

### Produkt anpassen

Editiere `src/ai_marketing_crew/main.py`, um andere Produkt-Informationen zu verwenden:

```python
inputs = {
    'product_name': 'Dein Produktname',
    'product_description': 'Produktbeschreibung...',
    'target_audience': 'Zielgruppenbeschreibung...',
    'budget': '€15.000 pro Quartal',
    'current_date': datetime.now().strftime('%Y-%m-%d'),
}
```

## Generierte Ausgaben

Nach der Ausführung findest du alle generierten Assets in folgenden Verzeichnissen:

```
resources/
├── market_research.md              # Marktforschungsbericht
├── marketing_strategy.md            # Marketing-Strategie
├── keywords.txt                     # SEO Keywords
└── drafts/
    ├── content_calendar.md          # Social Media Content-Kalender
    ├── linkedin_post_*.md           # LinkedIn Post-Entwürfe
    ├── twitter_post_*.txt           # X/Twitter Post-Entwürfe
    ├── reel_script_*.md             # Instagram Reels Scripts (optional)
    └── blog_post_*.md               # Blog-Artikel-Entwürfe
```

## Konfiguration

### Agents anpassen

Editiere `src/ai_marketing_crew/config/agents.yaml`, um Agent-Rollen, Goals, Backstories oder LLM-Einstellungen zu ändern.

### Tasks anpassen

Editiere `src/ai_marketing_crew/config/tasks.yaml`, um Task-Beschreibungen, Expected Outputs oder Output-Dateien zu ändern.

**Wichtig**: Änderungen an den YAML-Dateien erfordern keine Code-Änderungen!

## Projekt-Struktur

```
project-root/
├── src/
│   └── ai_marketing_crew/
│       ├── __init__.py
│       ├── main.py                 # Einstiegspunkt
│       ├── crew.py                 # Crew-Definition
│       ├── config/
│       │   ├── agents.yaml         # Agent-Konfigurationen
│       │   └── tasks.yaml          # Task-Konfigurationen
│       └── tools/
│           └── custom_tool.py      # Optionale Custom Tools
├── resources/                       # Generierte Assets
│   └── drafts/
├── docs/
│   └── marketing_crew_prd.md       # Product Requirements Document
├── .env                             # Umgebungsvariablen (nicht in Git)
├── pyproject.toml                   # Projekt-Konfiguration
└── README.md                        # Diese Datei
```

## Technische Details

- **Framework**: CrewAI 1.2.1
- **LLM**: OpenAI GPT-4o (konfigurierbar in `agents.yaml`)
- **Tools**: SerperDevTool (Web-Suche), ScrapeWebsiteTool, FileReadTool, FileWriteTool
- **Prozess**: Sequential (sequenzielle Task-Ausführung)
- **Python**: >=3.11

## Fehlerbehebung

### Serper API Key fehlt

Wenn `SERPER_API_KEY` nicht gesetzt ist, erscheint eine Warnung. Die Crew wird trotzdem funktionieren, nutzt aber nur LLM-basierte Recherche ohne aktuelle Web-Suche.

### OpenAI API Errors

Stelle sicher, dass:
1. `OPENAI_API_KEY` korrekt in `.env` gesetzt ist
2. Du ausreichend API-Credits hast
3. Das Rate-Limit nicht überschritten wurde

### Import Errors

Falls Import-Fehler auftreten:

```bash
uv sync
```

oder

```bash
pip install -e .
```

## Support

- [CrewAI Dokumentation](https://docs.crewai.com)
- [CrewAI GitHub](https://github.com/joaomdmoura/crewai)
- [CrewAI Discord](https://discord.com/invite/X4JWnZnxPb)

## Lizenz

Dieses Projekt ist Teil eines internen Marketing-Tools.
