# PRD – Marketing Crew AI (based on Crew AI crash course)

## 1. Purpose & Context

This document specifies the requirements for a **multi-agent, agentic marketing system** built with **Crew AI**. The goal is to orchestrate several specialized agents (Marketing Lead, Social Media Writer, Blog Writer, SEO Specialist) to automatically produce marketing assets for a SaaS product called **“AutoSheet IQ – AI-powered Excel automation”**.

The system should:
1. perform market & competitor research,
2. derive a marketing strategy,
3. generate a content/posting calendar,
4. create concrete social media drafts, blog drafts, and SEO helper assets,
5. persist the results to disk in a structured layout.

The implementation follows the architecture shown in the original tutorial: **agents + tasks + crew + tools**, but we will use **OpenAI** (e.g. `gpt-4o` / `gpt-4.1` or newer) as the LLM, not Google Gemini.

---

## 2. Goals (Objectives)

1. **Single-run content generation**  
   A single crew run should generate *all* relevant marketing artifacts for a given product input (research → strategy → calendar → drafts).

2. **Role-based & extensible**  
   Each marketing subtask is handled by its own agent (Head of Marketing, Social Media Writer, Blog Writer, SEO Specialist), so new roles can be added without rewriting the orchestration logic.

3. **Tool-augmented & up-to-date**  
   The research agent should be able to call a web search tool (e.g. Serper) so the output can reflect current market conditions and competitors.

4. **Config-driven, not hard-coded**  
   Prompts, roles, goals, and task descriptions must live in **YAML** files, not in Python code, so prompt updates don’t require code changes.

5. **Reusable artifacts**  
   All generated content should be written to the local filesystem (e.g. `resources/drafts/`) so a human marketer can review, edit, and publish it.

---

## 3. Non-Goals (Out of Scope)

- No publishing to real social networks (LinkedIn, X, Meta) – drafts only.
- No user/role authorization system.
- No fully-fledged retry/distributed scheduling.
- No UI/UX delivery (CLI / notebook is enough).
- No cost optimization beyond a basic rate limit.

---

## 4. Target Users & Personas

1. **Reena – Head of Marketing**  
   - Enters product name, description, target audience, budget, date  
   - Needs: market research report, marketing strategy, content plan

2. **Tony – Social Media Content Writer**  
   - Needs: ready-to-polish drafts for LinkedIn, X/Twitter, maybe Instagram/Reel  
   - Wants tone, hook, and relevant hashtags

3. **Nancy – Blog Author**  
   - Needs: blog draft from strategy/research  
   - Wants SEO keywords inserted or at least suggested

4. **Vin – SEO Specialist**  
   - Needs: keyword list, competitor keywords, suggested topics  
   - Wants: file output to feed into CMS/workflow

---

## 5. Use Cases / User Stories

1. **UC1 – Run full marketing crew**  
   > As a marketing lead, I want to provide a product (name, description, audience, budget, date) and have the crew generate all marketing assets for me.

2. **UC2 – Get current market research**  
   > As a marketing lead, I want a current market/competitor research report for “AI-powered Excel automation” so I can position the product.

3. **UC3 – Derive marketing strategy**  
   > As a marketing lead, I want the system to derive a marketing strategy (channels, positioning, cadence, budget split) from the research.

4. **UC4 – Build content calendar**  
   > As a social media writer, I want a content calendar with date/time/channel/topic so I know what to post when.

5. **UC5 – Generate social drafts**  
   > As a social media writer, I want the crew to write channel-specific drafts (LinkedIn, X/Twitter, optional IG/Reels) based on the calendar entries.

6. **UC6 – Generate blog draft**  
   > As a blog author, I want a blog skeleton/draft that uses the research insights and target audience so I can edit and publish.

7. **UC7 – Generate SEO assets**  
   > As an SEO specialist, I want a keyword list (including competitor keywords) so I can optimize landing pages and content.

---

## 6. Functional Requirements

### 6.1 Crew Orchestration

- **FR1**: The system MUST create a **Crew** with at least these 4 agents:
  1. `head_of_marketing`
  2. `content_creator_social`
  3. `content_writer_blog`
  4. `seo_specialist`
- **FR2**: The crew MUST run in **sequential** mode (`Process.sequential`), i.e. each task can consume previous task output.
- **FR3**: The crew MUST support **planning/reasoning** (`reasoning=True` or equivalent) so that a plan is formed before executing the tasks.

### 6.2 Agents (Roles)

1. **Head of Marketing**
   - **FR4**: MUST perform market & competitor research.
   - **FR5**: MUST derive a marketing strategy from the research.
   - **FR6**: MUST be allowed to delegate to other agents (`allow_delegation=True`).
   - **FR7**: MUST use **OpenAI** LLM (e.g. `gpt-4o`) defined in YAML.

2. **Content Creator Social Media**
   - **FR8**: MUST generate social drafts per channel (LinkedIn, X/Twitter, optional IG/Reel script).
   - **FR9**: SHOULD use channel-appropriate tone and length.
   - **FR10**: MUST use **OpenAI** LLM defined in YAML.

3. **Content Writer Blog**
   - **FR11**: MUST generate a blog draft (short demo version ~100–300 words or extended version 600–1,200 words).
   - **FR12**: SHOULD insert or at least list relevant SEO keywords if provided.
   - **FR13**: MUST use **OpenAI** LLM defined in YAML.

4. **SEO Specialist**
   - **FR14**: MUST generate a keyword list with: product keywords, problem keywords, and competitor keywords (e.g. “Microsoft 365 Copilot”, “Zapier”, “Numerous AI”) observed in research.
   - **FR15**: MUST write the keyword list to disk as `resources/keywords.txt`.
   - **FR16**: MUST use **OpenAI** LLM defined in YAML.

### 6.3 Tasks

The YAML-based task file MUST define at least the following tasks:

1. **T1 – Market Research**
   - **Input**: `{product_name, product_description, target_audience, current_date}`
   - **Description**: “Conduct market research to identify current trends, opportunities, and competition for {product_name} as of {current_date}.”
   - **Expected Output**: research report with: industry snapshot, customer pains, competitor list (incl. Microsoft, Zapier, Excel automation tools)
   - **Tools**: `SerperTool`, `ScrapeWebsiteTool`

2. **T2 – Build Marketing Strategy**
   - **Input**: output of T1
   - **Description**: “Create a marketing strategy based on research, tailored to {target_audience} and {budget}.”
   - **Expected Output**: channels, messaging, positioning, content types, rough budget allocation

3. **T3 – Build Content Calendar**
   - **Input**: output of T2
   - **Description**: “Create a content calendar for the upcoming weeks for LinkedIn, X/Twitter, and possibly Instagram/Reels.”
   - **Expected Output**: list of entries with `date`, `time`, `channel`, `topic`, `goal`
   - **Output File**: `resources/drafts/content_calendar.json|md`

4. **T4 – Generate Social Posts**
   - **Input**: output of T3
   - **Description**: “Generate actual post drafts for each calendar item.”
   - **Expected Output**: per-post files such as:
     - `resources/drafts/linkedin_post_01.md`
     - `resources/drafts/twitter_post_01.txt`
     - optionally: `resources/drafts/reel_script_01.md`

5. **T5 – Generate Blog Draft**
   - **Input**: output of T1 and T2
   - **Expected Output**: `resources/drafts/blog_post_autosheetiq.md` (with intro, value, CTA)

6. **T6 – Generate SEO Keywords**
   - **Input**: output of T1
   - **Expected Output**: `resources/keywords.txt` (one keyword per line, grouped by type)

*(In the original tutorial there were even more tasks like budget allocation; these can be added as optional tasks with the same pattern.)*

### 6.4 Tools / Integrations

- **FR17**: The system MUST support Crew AI standard tools:
  - `SerperDevTool` (web search)
  - `ScrapeWebsiteTool`
  - `DirectoryReadTool` (for `resources/drafts/`)
  - `FileReadTool`, `FileWriteTool`
- **FR18**: The system MUST load API keys from an **.env** file:
  - `OPENAI_API_KEY`
  - `SERPER_API_KEY`
- **FR19**: The code MUST be written so that switching the LLM is done in YAML, e.g.:

  ```yaml
  llm:
    provider: openai
    model: gpt-4o
    temperature: 0.4
  ```

- **FR20**: If a tool fails (e.g. no Serper key), the agent SHOULD fall back to LLM-only reasoning and log the error.

### 6.5 Configuration (YAML)

- **FR21**: Agents MUST be declared in `config/agents.yaml` with:
  - `role`
  - `goal`
  - `backstory`
  - `llm`
  - `tools`
  - `verbose`
  - `max_iter`
- **FR22**: Tasks MUST be declared in `config/tasks.yaml` with:
  - `description`
  - `expected_output`
  - placeholders: `{product_name}`, `{product_description}`, `{target_audience}`, `{budget}`, `{current_date}`
- **FR23**: Python code MUST read these YAMLs via a `@CrewBase`-decorated class:

  ```python
  from crewai import CrewBase

  @CrewBase
  class MarketingCrew:
      agents_config = "config/agents.yaml"
      tasks_config = "config/tasks.yaml"
  ```

### 6.6 File Output

- **FR24**: On first run, if not present, the system MUST create:
  - `resources/`
  - `resources/drafts/`
- **FR25**: Each long-form output MUST be written to a file.
- **FR26**: Filenames MUST be meaningful:
  - `market_research.md`
  - `marketing_strategy.md`
  - `content_calendar.md` or `.json`
  - `linkedin_post_YYYYMMDD.md`
  - `blog_post_autosheetiq.md`
  - `keywords.txt`

---

## 7. Non-functional Requirements

1. **NFR1 – Performance**: A full crew run can take several minutes (multiple OpenAI calls). A configurable `max_rpm` MUST be supported.
2. **NFR2 – Observability**: `verbose=True` MUST print tool calls, intermediate thoughts, and final answers to console.
3. **NFR3 – Portability**: The project MUST be installable via `uv` (preferred) or plain `pip`.
4. **NFR4 – Editor**: PyCharm (Windows) is a primary environment but the project MUST NOT rely on PyCharm-specific features.
5. **NFR5 – Reproducibility**: Dependencies MUST be defined in `pyproject.toml`.

---

## 8. Technical Constraints

- **Language**: Python 3.11+
- **Package Manager**: `uv` (preferred) or `pip`
- **Main libs**: `crewai`, `crewai-tools`, `python-dotenv`, `pydantic`
- **LLM**: **OpenAI** (`OPENAI_API_KEY` from `.env`)
- **Directory layout**:

  ```text
  project-root/
  ├─ marketing_crew/
  │  ├─ crew.py
  │  └─ __init__.py
  ├─ config/
  │  ├─ agents.yaml
  │  └─ tasks.yaml
  ├─ resources/
  │  └─ drafts/
  ├─ .env
  └─ pyproject.toml
  ```

---

## 9. Acceptance Criteria

1. **AC1**: Running the crew (e.g. `python marketing_crew/crew.py`) creates `resources/drafts/` and populates it with:
   - `market_research.md`
   - `marketing_strategy.md`
   - `content_calendar.*`
   - ≥1 social post draft
   - `keywords.txt`
2. **AC2**: Outputs reference the product name and target audience passed to the kickoff.
3. **AC3**: Console output shows at least one **tool execution**.
4. **AC4**: Editing `config/agents.yaml` (e.g. tone change) changes the output **without** changing Python code.
5. **AC5**: If `SERPER_API_KEY` is missing, the run still finishes and logs a clear error/warning.

---

## 10. Risks & Assumptions

- **Assumption**: User has valid `OPENAI_API_KEY` and optionally `SERPER_API_KEY`.
- **Assumption**: Internet access is available for the host machine.
- **Risk**: Long reasoning chains can consume many OpenAI tokens → keep `max_iter` low.
- **Risk**: Web search results can vary by time/location → outputs can vary between runs.
- **Risk**: Generated content must be reviewed by a human before publishing.

---

## 11. Possible Extensions

- Multi-language content generation (EN/DE)
- “Human in the loop” step between calendar and post generation
- Export to Google Sheets / Notion
- Basic web UI using Crew AI Studio

---

## 12. Glossary

- **Agent** – autonomous LLM program with a role, goal, backstory, tools
- **Crew** – orchestrated set of agents that collaborate to reach a goal
- **Tool** – external capability (search, scrape, file I/O)
- **Task** – unit of work tied to an agent
- **YAML Config** – external prompt & task definition
